# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0002_auto_20180130_2015'),
    ]

    operations = [
        migrations.AddField(
            model_name='dzielnica',
            name='slug',
            field=models.SlugField(blank=True, max_length=150),
        ),
    ]
