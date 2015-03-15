# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cocktail', '0017_auto_20150217_0600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='date_added',
            field=models.DateField(default=datetime.date(2015, 3, 15), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bartender',
            name='sign_up_date',
            field=models.DateField(default=datetime.date(2015, 3, 15), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bartender',
            name='time_last_used',
            field=models.DateTimeField(default=datetime.date(2015, 3, 15), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cocktail',
            name='image',
            field=models.ImageField(upload_to=b'cocktail_images', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateField(default=datetime.date(2015, 3, 15), auto_now_add=True),
            preserve_default=True,
        ),
    ]
