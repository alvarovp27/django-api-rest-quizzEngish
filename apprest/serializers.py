from .models import WordTranslations, FavouritesEN, FavouritesSP, WordStats, Categories
from rest_framework import serializers

class WordTranslationsSerializer(serializers.Serializer):
	wordSP = serializers.CharField(max_length=100)
	typeSP = serializers.CharField(max_length=100)
	wordEN = serializers.CharField(max_length=100)
	typeEN = serializers.CharField(max_length=100)
	category = serializers.CharField(max_length=100)

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

