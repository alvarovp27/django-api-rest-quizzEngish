from django.db import models

# Create your models here.

class WordTranslations(models.Model):
	wordSP = models.CharField(max_length=100)
	typeSP = models.CharField(max_length=100)
	wordEN = models.CharField(max_length=100)
	typeEN = models.CharField(max_length=100)
	category = models.CharField(max_length=100)

class FavouritesEN(models.Model):
	wordEN = models.CharField(max_length=100)

class FavouritesSP(models.Model):
	wordSP = models.CharField(max_length=100)

class WordStats(models.Model):
	word = models.CharField(max_length=100)
	hits = models.CharField(max_length=100)
	fails = models.CharField(max_length=100)

class Categories(models.Model):
	name = models.CharField(max_length=100)