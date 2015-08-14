from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import WordTranslations
from .serializers import WordSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


	@csrf_exempt
	def word_list(request):
		"""
   		List all code snippets, or create a new snippet.
    	"""
    	if request.method=='GET':
    		words = Word.objects().all()
    		serializer = WordSerializer(words, many = True)
    		return JSONResponse(serializer.data)
    	elif request.method=='POST':
    		data = JSONParser().parse(request)
    		serializer = WordSerializer(data=data)
    		if serializer.is_valid():
    			serializer.save()
    			return JSONResponse(serializer.data, status=201)
    		return JSONResponse(serializer.errors, status=400)

    def word_detail(request, pk):
    	"""
    	Retrieve, update or delete a code snippet.
    	"""
    	if 