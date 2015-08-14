# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FavouritesEN',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('wordEN', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FavouritesSP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('wordSP', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WordStats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('word', models.CharField(max_length=100)),
                ('hits', models.CharField(max_length=100)),
                ('fails', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WordTranslations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('wordSP', models.CharField(max_length=100)),
                ('typeSP', models.CharField(max_length=100)),
                ('wordEN', models.CharField(max_length=100)),
                ('typeEN', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
            ],
        ),
    ]
