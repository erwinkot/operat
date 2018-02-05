# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('adres', models.CharField(max_length=60)),
                ('kod_pocztowy', models.CharField(max_length=6)),
                ('telefon', models.CharField(null=True, blank=True, max_length=30)),
                ('data_urodzenia', models.DateField(null=True, blank=True)),
                ('status', models.CharField(choices=[('fizyczna', 'Osoba fizyczna'), ('firmap', 'Przedstawiciel firmy'), ('biurop', 'Przedstawiciel biura')], default='fizyczna', max_length=20)),
                ('firma', models.ForeignKey(to='realestate.Profilefirm', default=2, related_name='account_profiles')),
                ('miejscowosc', models.ForeignKey(to='realestate.Miejscowosc', default=1, related_name='account_profiles')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
