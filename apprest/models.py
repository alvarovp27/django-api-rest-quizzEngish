from django.db import models

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

# Create your models here.

class WordTranslations(models.Model):
	wordSP = models.CharField(max_length=100)
	typeSP = models.CharField(max_length=100)
	wordEN = models.CharField(max_length=100)
	typeEN = models.CharField(max_length=100)
	category = models.CharField(max_length=100)
	user = models.ForeignKey('auth.User', related_name='wordTranslations')

class FavouritesEN(models.Model):
	wordEN = models.CharField(max_length=100)

class FavouritesSP(models.Model):
	wordSP = models.CharField(max_length=100)

class WordStats(models.Model):
	word = models.CharField(max_length=100)
	hits = models.IntegerField()
	fails = models.IntegerField()

class Categories(models.Model):
	name = models.CharField(max_length=100)