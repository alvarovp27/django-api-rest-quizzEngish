# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0002_auto_20150815_2049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wordtranslations',
            old_name='owner',
            new_name='user',
        ),
    ]
