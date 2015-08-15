from django.shortcuts import render

# Create your views here.
from apprest.models import WordTranslations
from apprest.serializers import WordTranslationsSerializer, UserSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from rest_framework import permissions

class Usuario(APIView):
	serializer_class = UserSerializer
	def get(self,request,format=None):
		users= User.objects.all()
		response = self.serializer_class(users,many=True)
		return Response(response.data)

	def post(self, request, format = None):
		serializer = UserSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class WordTranslationsList(APIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	#Así desactivo la interfaz de usuario por defecto de la API
	renderer_classes = [JSONRenderer]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)
	
	def get(self, request, format=None):
		words = WordTranslations.objects.all()
		serializer = WordTranslationsSerializer(words, many=True)
		#print(request.user.__str__()) #Para probar la autenticación por cookie
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = WordTranslationsSerializer(data = request.data)
		if serializer.is_valid():
			self.perform_create(serializer)
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class WordTranslationsFromEnglish(APIView):

	renderer_classes=[JSONRenderer]

	def get_objects(self, wordEN):
		try:
			return WordTranslations.objects.filter(wordEN=wordEN)
		except WordTranslations.DoesNotExist:
			raise Http404

	def get(self, request, wordEN, format=None):
		words = self.get_objects(wordEN)
		serializer = WordTranslationsSerializer(words, many=True)
		return Response(serializer.data)


class WordTranslationUpdateDelete(APIView):
	renderer_classes=[JSONRenderer]
	def get_object(self, wordEN,wordSP,typeEN,typeSP,category):
		try:
			return WordTranslations.objects.get(wordEN=wordEN, wordSP=wordSP, typeEN=typeEN, typeSP=typeSP, category=category)
		except WordTranslations.DoesNotExist:
			raise Http404

	def put(self, request, wordEN, typeEN, wordSP, typeSP, category, format=None):
		word = self.get_object(wordEN,wordSP,typeEN,typeSP,category)
		serializer = WordTranslationsSerializer(word, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
	def delete(self, request, wordEN, typeEN, wordSP, typeSP, category, format=None):
		word = self.get_object(wordEN,wordSP,typeEN,typeSP,category)
		word.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)