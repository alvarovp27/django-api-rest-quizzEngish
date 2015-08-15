# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apprest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordtranslations',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='wordTranslations', default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='wordstats',
            name='fails',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='wordstats',
            name='hits',
            field=models.IntegerField(),
        ),
    ]
