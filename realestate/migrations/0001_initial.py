# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dzielnica',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nazwa', models.CharField(max_length=150)),
            ],
            options={
                'ordering': ('nazwa',),
            },
        ),
        migrations.CreateModel(
            name='Gmina',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nazwa', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True, max_length=150)),
                ('wojt', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'ordering': ('nazwa',),
            },
        ),
        migrations.CreateModel(
            name='Miejscowosc',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nazwa', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True, max_length=150)),
                ('profil', models.CharField(choices=[('miasto', 'Miasto'), ('wieś', 'Wieś')], default='miasto', max_length=30)),
                ('gmina', models.ForeignKey(to='realestate.Gmina', related_name='miejscowosci')),
            ],
            options={
                'ordering': ('nazwa',),
            },
        ),
        migrations.CreateModel(
            name='Powiat',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nazwa', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True, max_length=150)),
                ('starosta', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'ordering': ('nazwa',),
            },
        ),
        migrations.CreateModel(
            name='Profilefirm',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nazwa', models.CharField(max_length=250)),
                ('adres_firmy', models.CharField(max_length=60)),
                ('kod_pocztowy', models.CharField(max_length=6)),
                ('nip', models.CharField(max_length=10)),
                ('nr_ewid', models.CharField(blank=True, max_length=10)),
                ('regon', models.CharField(blank=True, max_length=10)),
                ('profil', models.CharField(choices=[('firma', 'Firma'), ('pośrednik', 'Pośrednik nieruchomości')], default='firma', max_length=30)),
                ('rodzaj_firmy', models.CharField(choices=[('deweloper', 'Deweloper'), ('pośrednik', 'Pośrednictwo nieruchomości'), ('właściciel', 'Właściciel nieruchomości')], default='właściciel', max_length=30)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('miejscowosc', models.ForeignKey(to='realestate.Miejscowosc', blank=True, default=1, related_name='profilefirmos')),
            ],
            options={
                'ordering': ('nazwa',),
            },
        ),
        migrations.CreateModel(
            name='Wojewodztwo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nazwa', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True, max_length=150)),
                ('wojewoda', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'ordering': ('nazwa',),
            },
        ),
        migrations.AddField(
            model_name='powiat',
            name='wojewodztwo',
            field=models.ForeignKey(to='realestate.Wojewodztwo', related_name='powiatos'),
        ),
        migrations.AddField(
            model_name='gmina',
            name='powiat',
            field=models.ForeignKey(to='realestate.Powiat', related_name='gminas'),
        ),
        migrations.AddField(
            model_name='dzielnica',
            name='miejscowosc',
            field=models.ForeignKey(to='realestate.Miejscowosc', related_name='dzielnicas'),
        ),
    ]
