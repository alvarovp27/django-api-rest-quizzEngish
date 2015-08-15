from .models import WordTranslations, FavouritesEN, FavouritesSP, WordStats, Categories
from rest_framework import serializers
from django.contrib.auth.models import User
"""
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username','email','password')
		read_only_fields=('password')
"""
class UserSerializer(serializers.Serializer):
	username = serializers.CharField(max_length=30)
	password = serializers.CharField(max_length=100)

	def create(self, validated_data):
		user = User(username=validated_data['username'])
		user.set_password(validated_data['password'])
		user.save()
		return user


class WordTranslationsSerializer(serializers.Serializer):
	wordSP = serializers.CharField(max_length=100)
	typeSP = serializers.CharField(max_length=100)
	wordEN = serializers.CharField(max_length=100)
	typeEN = serializers.CharField(max_length=100)
	category = serializers.CharField(max_length=100)
	#user = serializers.IntegerField()

	#Los siguientes dos métodos definen cómo se van a crear
	#o modificar instancias al llamar al serializer.save()
	def create(self, validated_data):
		return WordTranslations.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.wordSP = validated_data.get('wordSP',instance.wordSP)
		instance.typeSP = validated_data.get('typeSP',instance.typeSP)
		instance.wordEN = validated_data.get('wordEN',instance.wordEN)
		instance.typeEN = validated_data.get('typeEN',instance.typeEN)
		instance.category = validated_data.get('category',instance.category)
		instance.save()
		return instance



class FavouritesEN(serializers.Serializer):
	wordEN = serializers.CharField(max_length=100)

	def create(self, validated_data):
		return FavouritesEN.object.create(**validated_data)

	def update(self, instance, validated_data):
		instsance.wordEN = validated_data.get('wordEN', instance.wordEN)
		instance.save()
		return instance

class FavouritesSP(serializers.Serializer):
	wordSP = serializers.CharField(max_length=100)

	def create(self, validated_data):
		return FavouritesSP.object.create(**validated_data)

	def update(self, instance, validated_data):
		instsance.wordSP = validated_data.get('wordSP', instance.wordSP)
		instance.save()
		return instance

class WordStats(serializers.Serializer):
	word = serializers.CharField(max_length=100)
	hits = serializers.IntegerField()
	fails = serializers.IntegerField()

	def create(self, validated_data):
		return WordStats.object.create(**validated_data)

	def update(self, instance, validated_data):
		instance.word = validated_data.get('word',instance.word)
		instance.hits = validated_data.get('hits',instance.hits)
		instance.fails = validated_data.get('fails',instance.fails)
		instance.save()
		return instance

class Categories(serializers.Serializer):
	name = serializers.CharField(max_length=100)

	def create(self, validated_data):
		return Categories.object.create(**validated_data)

	def update(self, instance, validated_data):
		instance.name = validated_data.get('name',instance.name)
		instance.save()
		return instance