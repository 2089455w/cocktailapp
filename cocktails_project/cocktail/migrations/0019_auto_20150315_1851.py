# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocktail', '0018_auto_20150315_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cocktail',
            name='taste_palette',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
