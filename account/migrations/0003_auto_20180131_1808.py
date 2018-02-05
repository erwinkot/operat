# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20180131_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='firma',
            field=models.ForeignKey(null=True, related_name='account_profiles', blank=True, to='realestate.Profilefirm'),
        ),
    ]
