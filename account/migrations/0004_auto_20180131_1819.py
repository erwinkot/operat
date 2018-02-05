# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20180131_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='firma',
            field=models.ForeignKey(default=2, to='realestate.Profilefirm', related_name='account_profiles'),
        ),
    ]
