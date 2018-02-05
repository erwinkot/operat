# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('realestate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dewelopr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('powierz_nieruchomosci', models.DecimalField(max_digits=12, blank=True, decimal_places=0, default=0)),
                ('ilosc_poczat', models.IntegerField(blank=True, default=0)),
            ],
            options={
                'ordering': ('nieruchomosc',),
            },
        ),
        migrations.CreateModel(
            name='Domy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('powierz_domu', models.DecimalField(max_digits=12, blank=True, decimal_places=0, default=0)),
                ('powierz_dzial', models.DecimalField(max_digits=12, blank=True, decimal_places=0, default=0)),
                ('status_dzial', models.CharField(choices=[('własność', 'własność'), ('dzierżawa wieczysta', 'dzierżawa wieczysta')], max_length=30, default='własność')),
                ('rodzaj_domu', models.CharField(choices=[('wolnostojący', 'wolnostojący'), ('bliźniak', 'bliźniak'), ('szeregówka', 'szeregówka'), ('kamienica', 'kamienica'), ('dworek', 'dworek/pałacyk'), ('gospodarstwo', 'gospodarstwo rolne')], max_length=30, blank=True)),
                ('rok_budowy', models.CharField(max_length=4, blank=True)),
                ('czynsz', models.DecimalField(max_digits=12, blank=True, decimal_places=0, default=0)),
                ('kaucja', models.DecimalField(max_digits=12, blank=True, decimal_places=0, default=0)),
                ('dostepne', models.CharField(max_length=30, blank=True)),
                ('rodz_materialu', models.CharField(choices=[('cegła', 'cegła'), ('silikat', 'silikat'), ('beton komórkowy', 'beton komórkowy'), ('pustak', 'pustak'), ('silikat', 'silikat'), ('keramzyt', 'keramzyt'), ('wielka płyta', 'wielka płyta'), ('beton', 'beton'), ('drewno', 'drewno'), ('inne', 'inne')], max_length=30, blank=True)),
                ('dach', models.CharField(choices=[('płaski', 'płaski'), ('skośny', 'skośny')], max_length=30, blank=True)),
                ('pokrycie_dach', models.CharField(choices=[('dachówka ceramiczna', 'dachówka ceramiczna'), ('blachodachówka', 'blachodachówka'), ('dachówka inna', 'dachówka inna'), ('eternit', 'eternit'), ('papa', 'papa'), ('gont', 'gont'), ('łupek', 'łupek'), ('strzecha', 'strzecha'), ('inne', 'inne')], max_length=30, blank=True)),
                ('stan_wykonczenia', models.CharField(choices=[('do zamieszkania', 'do zamieszkania'), ('do wykończenia', 'do wykończenia'), ('do remontu', 'do remontu'), ('stan surowy zamknięty', 'stan surowy zamknięty'), ('stan surowy otwarty', 'stan surowy otwarty'), ('inne', 'inne')], max_length=30, blank=True)),
                ('okna', models.CharField(choices=[('drewniane', 'drewniane'), ('plastikowe', 'plastikowe'), ('aluminiowe', 'aluminiowe')], max_length=30, blank=True)),
                ('ilosc_kond', models.PositiveIntegerField(default=0)),
                ('ilosc_pokoi', models.PositiveIntegerField(default=0)),
                ('ilosc_lazen', models.PositiveIntegerField(default=0)),
                ('ilosc_kuchni', models.PositiveIntegerField(default=0)),
                ('piwnice', models.BooleanField(default=False)),
                ('garaz', models.BooleanField(default=False)),
                ('poddasze', models.BooleanField(default=False)),
                ('basen', models.BooleanField(default=False)),
                ('klimatyzacja', models.BooleanField(default=False)),
                ('prad', models.BooleanField(default=False)),
                ('gaz', models.BooleanField(default=False)),
                ('woda', models.BooleanField(default=False)),
                ('kanalizacja', models.BooleanField(default=False)),
                ('szambo', models.BooleanField(default=False)),
                ('oczyszczalnia', models.BooleanField(default=False)),
                ('telefon', models.BooleanField(default=False)),
                ('internet', models.BooleanField(default=False)),
                ('tel_kablowa', models.BooleanField(default=False)),
                ('miejskie', models.BooleanField(default=False)),
                ('gazowe', models.BooleanField(default=False)),
                ('olejowe', models.BooleanField(default=False)),
                ('elektryczne', models.BooleanField(default=False)),
                ('weglowe', models.BooleanField(default=False)),
                ('piece_kaflowe', models.BooleanField(default=False)),
                ('kominkowe', models.BooleanField(default=False)),
                ('kolektor_sloneczny', models.BooleanField(default=False)),
                ('pompa_ciepla', models.BooleanField(default=False)),
                ('biomasa', models.BooleanField(default=False)),
                ('ogrodzenie', models.CharField(choices=[('drewniane', 'drewniane'), ('metalowe', 'metalowe'), ('betonowe', 'betonowe'), ('murowane', 'murowane'), ('siatka', 'siatka'), ('żywopłot', 'żywopłot'), ('inne', 'inne')], max_length=30, blank=True)),
                ('dojazd', models.CharField(choices=[('asfalt', 'asfalt'), ('utwardzony', 'utwardzony'), ('nieutwardzony', 'nieutwardzony')], max_length=30, blank=True)),
                ('teren_zamkniety', models.BooleanField(default=False)),
                ('monitoring', models.BooleanField(default=False)),
                ('alarm', models.BooleanField(default=False)),
                ('drzwi_anty', models.BooleanField(default=False)),
                ('rolety', models.BooleanField(default=False)),
                ('domofon', models.BooleanField(default=False)),
                ('las', models.BooleanField(default=False)),
                ('gory', models.BooleanField(default=False)),
                ('jezioro', models.BooleanField(default=False)),
                ('morze', models.BooleanField(default=False)),
                ('teren_otwarty', models.BooleanField(default=False)),
                ('meble', models.BooleanField(default=False)),
                ('meble_czesc', models.BooleanField(default=False)),
                ('kuchenka', models.BooleanField(default=False)),
                ('pralka', models.BooleanField(default=False)),
                ('lodowka', models.BooleanField(default=False)),
                ('zmywarka', models.BooleanField(default=False)),
                ('piekarnik', models.BooleanField(default=False)),
                ('mikrofala', models.BooleanField(default=False)),
                ('telewizor', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('nieruchomosc',),
            },
        ),
        migrations.CreateModel(
            name='Dzialki',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typ_dzialki', models.CharField(choices=[('budowlana', 'Działka budowlana'), ('rolna', 'Działka rolna'), ('rekreacyjna', 'Działka rekreacyjna'), ('inwestycyjna', 'Działka inwestycyjna'), ('leśna', 'Działka leśna'), ('siedliskowa', 'Działka siedliskowa')], max_length=30, default='budowlana')),
                ('powi_dzialki', models.DecimalField(max_digits=12, decimal_places=0, default=0)),
                ('status_dzial', models.CharField(choices=[('własność', 'własność'), ('dzierżawa wieczysta', 'dzierżawa wieczysta')], max_length=30, default='wlasność')),
                ('przeznaczenie_dzial', models.CharField(choices=[('jednorodzinne', 'mieszkaniowe jednorodzinne'), ('wielorodzinne', 'mieszkaniowe wielorodzinne'), ('wysokie', 'mieszkaniowe wysokie'), ('przemysłowe', 'przemysłowe'), ('usługi i handel', 'usługi i handel'), ('hotelowe', 'hotelowe'), ('medyczne', 'medyczne'), ('pozostałe', 'pozostałe')], max_length=30, default='wielorodzinne')),
                ('info_mpzp', models.TextField(blank=True)),
                ('dojazd', models.CharField(choices=[('asfalt', 'asfalt'), ('utwardzony', 'utwardzony'), ('nieutwardzony', 'nieutwardzony')], max_length=30, blank=True)),
                ('prad', models.BooleanField(default=False)),
                ('gaz', models.BooleanField(default=False)),
                ('woda', models.BooleanField(default=False)),
                ('kanalizacja', models.BooleanField(default=False)),
                ('szambo', models.BooleanField(default=False)),
                ('oczyszczalnia', models.BooleanField(default=False)),
                ('telefon', models.BooleanField(default=False)),
                ('las', models.BooleanField(default=False)),
                ('gory', models.BooleanField(default=False)),
                ('jezioro', models.BooleanField(default=False)),
                ('morze', models.BooleanField(default=False)),
                ('teren_otwarty', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('nieruchomosc',),
            },
        ),
        migrations.CreateModel(
            name='Garage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('powierz_garage', models.DecimalField(max_digits=12, blank=True, decimal_places=0, default=0)),
                ('rodzaj_zabud', models.CharField(choices=[('wolnostojący', 'wolnostojący'), ('w budynku', 'w budynku'), ('przy domu', 'przy domu')], max_length=30, blank=True)),
                ('konstr_garage', models.CharField(choices=[('murowany', 'murowany'), ('blaszany', 'blaszany'), ('drewniany', 'drewniany'), ('wiata', 'wiata'), ('inny', 'inny')], max_length=30, default='murowany')),
                ('czynsz', models.DecimalField(max_digits=12, blank=True, decimal_places=0, default=0)),
                ('kaucja', models.DecimalField(max_digits=12, blank=True, decimal_places=0, default=0)),
                ('dostepne', models.CharField(max_length=30, blank=True)),
                ('ogrzewanie', models.BooleanField(default=False)),
                ('oswietlenie', models.BooleanField(default=False)),
                ('woda', models.BooleanField(default=False)),
                ('kanalizacja', models.BooleanField(default=False)),
                ('szambo', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('nieruchomosc',),
            },
        ),
        migrations.CreateModel(
            name='ImageItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=65, blank=True)),
                ('image', models.ImageField(upload_to='images/%y/%m/%d')),
                ('opis', models.TextField(blank=True)),
                ('created', models.DateField(db_index=True, auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Komercyjne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('powierz_nieruchomosci', models.DecimalField(max_digits=12, blank=True, decimal_places=0, default=0)),
                ('powierz_dzialki', models.DecimalField(max_digits=12, blank=True, decimal_places=0, default=0)),
                ('status_dzial', models.CharField(choices=[('własność', 'własność'), ('dzierżawa wieczysta', 'dzierżawa wieczysta')], max_length=30, default='własność')),
                ('info_mpzp', models.TextField(blank=True)),
                ('rodzaj_nieruchom', models.CharField(choices=[('lokal usługowy', 'lokal usługowy'), ('lokal handlowy', 'lokal handlowy'), ('lokal biurowy', 'lokal biurowy'), ('lokal gastronomiczny', 'lokal gastronomiczny'), ('klub', 'klub'), ('hala magazynowa', 'hala magazynowa'), ('hala przemysłowa', 'hala przemysłowa'), ('biurowiec', 'biurowiec'), ('zakład przemysłowy', 'zakład przemysłowy'), ('hotel', 'hotel'), ('pensjonat', 'pensjonat'), ('dom seniora', 'dom seniora'), ('DPS', 'DPS'), ('klinika', 'klinika'), ('przychodnia', 'przychodnia'), ('gabinet stomatologiczny', 'gabinet stomatologiczny'), ('pałac', 'pałac')], max_length=30, blank=True)),
                ('pozycja_nieruchom', models.CharField(choices=[('nieruchomość samodzielna', 'nieruchomość samodzielna'), ('część nieruchomości', 'część nieruchomości')], max_length=30, blank=True)),
                ('rok_budowy', models.CharField(max_length=4, blank=True)),
                ('polozenie_lokalu', models.CharField(choices=[('odzielny obiekt', 'odzielny obiekt'), ('biurowiec', 'biurowiec'), ('centrum handlowe', 'centrum handlowe'), ('obiekt przemysłowy', 'obiekt przemysłowy'), ('hala magazynowa', 'hala magazynowa'), ('blok', 'blok'), ('kamienica', 'kamienica'), ('inny', 'inny')], max_length=30, blank=True)),
                ('rodz_materialu', models.CharField(choices=[('cegła', 'cegła'), ('silikat', 'silikat'), ('beton komórkowy', 'beton komórkowy'), ('konstrukcja stalowa', 'konstrukcja stalowa'), ('konstrukcja żel-betonowa', 'konstrukcja żel-betonowa'), ('silikat', 'silikat'), ('keramzyt', 'keramzyt'), ('wielka płyta', 'wielka płyta'), ('beton', 'beton'), ('drewno', 'drewno'), ('inne', 'inne')], max_length=30, blank=True)),
                ('dach', models.CharField(choices=[('płaski', 'płaski'), ('skośny', 'skośny')], max_length=30, blank=True)),
                ('pokrycie_dach', models.CharField(choices=[('dachówka ceramiczna', 'dachówka ceramiczna'), ('blachodachówka', 'blachodachówka'), ('dachówka inna', 'dachówka inna'), ('eternit', 'eternit'), ('papa', 'papa'), ('gont', 'gont'), ('łupek', 'łupek'), ('strzecha', 'strzecha'), ('inne', 'inne')], max_length=30, blank=True)),
                ('stan_wykonczenia', models.CharField(choices=[('do użytku', 'do użytku'), ('do adaptacji', 'do adaptacji'), ('do remontu', 'do remontu'), ('stan surowy zamknięty', 'stan surowy zamknięty'), ('stan surowy otwarty', 'stan surowy otwarty'), ('inne', 'inne')], max_length=30, blank=True)),
                ('okna', models.CharField(choices=[('drewniane', 'drewniane'), ('plastikowe', 'plastikowe'), ('aluminiowe', 'aluminiowe'), ('stalowe', 'stalowe')], max_length=30, blank=True)),
                ('posadzka', models.CharField(choices=[('pylna', 'pylna'), ('niepylna', 'niepylna'), ('specjalna', 'specjalna'), ('inna', 'inna')], max_length=30, blank=True)),
                ('parking', models.CharField(choices=[('asfalt', 'asfalt'), ('beton', 'beton'), ('kostka brukowa', 'kostka brukowa'), ('utwardzony', 'utwardzony'), ('nieutwardzony', 'nieutwardzony'), ('brak', 'brak'), ('inny', 'inny')], max_length=30, blank=True)),
                ('ilosc_kond', models.PositiveIntegerField(default=0)),
                ('ilosc_pokoi', models.PositiveIntegerField(default=0)),
                ('klimatyzacja', models.BooleanField(default=False)),
                ('prad', models.BooleanField(default=False)),
                ('gaz', models.BooleanField(default=False)),
                ('woda', models.BooleanField(default=False)),
                ('kanalizacja', models.BooleanField(default=False)),
                ('szambo', models.BooleanField(default=False)),
                ('telefon', models.BooleanField(default=False)),
                ('internet', models.BooleanField(default=False)),
                ('tel_kablowa', models.BooleanField(default=False)),
                ('monitoring', models.BooleanField(default=False)),
                ('oczyszczalnia', models.BooleanField(default=False)),
                ('ogrzewanie', models.CharField(choices=[('miejskie', 'miejskie'), ('gazowe', 'gazowe'), ('olejowe', 'olejowe'), ('węglowe', 'węglowe'), ('kolektory słoneczne', 'kolektory słoneczne'), ('inne', 'inne'), ('brak', 'brak')], max_length=30, blank=True)),
                ('ogrodzenie', models.CharField(choices=[('drewniane', 'drewniane'), ('metalowe', 'metalowe'), ('betonowe', 'betonowe'), ('murowane', 'murowane'), ('siatka', 'siatka'), ('żywopłot', 'żywopłot'), ('inne', 'inne')], max_length=30, blank=True)),
                ('dojazd', models.CharField(choices=[('asfalt', 'asfalt'), ('utwardzony', 'utwardzony'), ('nieutwardzony', 'nieutwardzony')], max_length=30, blank=True)),
                ('teren_przemyslowy', models.BooleanField(default=False)),
                ('teren_zdrojowy', models.BooleanField(default=False)),
                ('teren_turystyczny', models.BooleanField(default=False)),
                ('las', models.BooleanField(default=False)),
                ('gory', models.BooleanField(default=False)),
                ('jezioro', models.BooleanField(default=False)),
                ('morze', models.BooleanField(default=False)),
                ('teren_otwarty', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('nieruchomosc',),
            },
        ),
        migrations.CreateModel(
            name='Mieszkania',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('powierz_mieszkania', models.DecimalField(max_digits=12, blank=True, decimal_places=0, default=0)),
                ('rodzaj_zabud', models.CharField(choices=[('wolnostojący', 'wolnostojący'), ('bliźniak', 'bliźniak'), ('szeregówka', 'szeregówka'), ('kamienica', 'kamienica'), ('blok', 'blok'), ('apartamentowiec', 'apartamentowiec'), ('loft', 'loft')], max_length=30, blank=True)),
                ('rodzaj_mieszkania', models.CharField(choices=[('jednopoziomowe', 'jednopoziomowe'), ('dwupoziomowe', 'dwupoziomowe'), ('poddasze', 'poddasze'), ('loft', 'loft')], max_length=30, default='jednopoziomowe')),
                ('pietro', models.CharField(max_length=3)),
                ('rok_budowy', models.CharField(max_length=4, blank=True)),
                ('czynsz', models.DecimalField(max_digits=12, blank=True, decimal_places=0, default=0)),
                ('kaucja', models.DecimalField(max_digits=12, blank=True, decimal_places=0, default=0)),
                ('dostepne', models.CharField(max_length=30, blank=True)),
                ('rodz_materialu', models.CharField(choices=[('cegła', 'cegła'), ('silikat', 'silikat'), ('beton komórkowy', 'beton komórkowy'), ('pustak', 'pustak'), ('silikat', 'silikat'), ('keramzyt', 'keramzyt'), ('wielka płyta', 'wielka płyta'), ('beton', 'beton'), ('drewno', 'drewno'), ('inne', 'inne')], max_length=30, blank=True)),
                ('stan_wykonczenia', models.CharField(choices=[('do zamieszkania', 'do zamieszkania'), ('do wykończenia', 'do wykończenia'), ('do remontu', 'do remontu'), ('stan surowy zamknięty', 'stan surowy zamknięty'), ('stan surowy otwarty', 'stan surowy otwarty'), ('inne', 'inne')], max_length=30, blank=True)),
                ('okna', models.CharField(choices=[('drewniane', 'drewniane'), ('plastikowe', 'plastikowe'), ('aluminiowe', 'aluminiowe')], max_length=30, blank=True)),
                ('ilosc_kond', models.PositiveIntegerField(default=0)),
                ('ilosc_pokoi', models.PositiveIntegerField(default=0)),
                ('ilosc_lazen', models.PositiveIntegerField(default=0)),
                ('ilosc_kuchni', models.PositiveIntegerField(default=0)),
                ('winda', models.BooleanField(default=False)),
                ('garaz', models.BooleanField(default=False)),
                ('parking', models.BooleanField(default=False)),
                ('piwnica', models.BooleanField(default=False)),
                ('klimatyzacja', models.BooleanField(default=False)),
                ('balkon', models.BooleanField(default=False)),
                ('taras', models.BooleanField(default=False)),
                ('ogrodek', models.BooleanField(default=False)),
                ('prad', models.BooleanField(default=False)),
                ('gaz', models.BooleanField(default=False)),
                ('woda', models.BooleanField(default=False)),
                ('kanalizacja', models.BooleanField(default=False)),
                ('szambo', models.BooleanField(default=False)),
                ('oczyszczalnia', models.BooleanField(default=False)),
                ('telefon', models.BooleanField(default=False)),
                ('internet', models.BooleanField(default=False)),
                ('tel_kablowa', models.BooleanField(default=False)),
                ('miejskie', models.BooleanField(default=False)),
                ('gazowe', models.BooleanField(default=False)),
                ('olejowe', models.BooleanField(default=False)),
                ('elektryczne', models.BooleanField(default=False)),
                ('weglowe', models.BooleanField(default=False)),
                ('piece_kaflowe', models.BooleanField(default=False)),
                ('kominkowe', models.BooleanField(default=False)),
                ('kolektor_sloneczny', models.BooleanField(default=False)),
                ('pompa_ciepla', models.BooleanField(default=False)),
                ('biomasa', models.BooleanField(default=False)),
                ('dojazd', models.CharField(choices=[('asfalt', 'asfalt'), ('utwardzony', 'utwardzony'), ('nieutwardzony', 'nieutwardzony')], max_length=30, default='asfalt')),
                ('teren_zamkniety', models.BooleanField(default=False)),
                ('monitoring', models.BooleanField(default=False)),
                ('alarm', models.BooleanField(default=False)),
                ('drzwi_anty', models.BooleanField(default=False)),
                ('rolety', models.BooleanField(default=False)),
                ('domofon', models.BooleanField(default=False)),
                ('meble', models.BooleanField(default=False)),
                ('meble_czesc', models.BooleanField(default=False)),
                ('kuchenka', models.BooleanField(default=False)),
                ('pralka', models.BooleanField(default=False)),
                ('lodowka', models.BooleanField(default=False)),
                ('zmywarka', models.BooleanField(default=False)),
                ('piekarnik', models.BooleanField(default=False)),
                ('mikrofala', models.BooleanField(default=False)),
                ('telewizor', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('nieruchomosc',),
            },
        ),
        migrations.CreateModel(
            name='Nieruchomosc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profil', models.CharField(max_length=25, blank=True)),
                ('nazwa_opis', models.CharField(max_length=250)),
                ('rodzaj_transakcji', models.CharField(choices=[('sprzedaż', 'sprzedaż'), ('wynajem', 'wynajem')], max_length=20, default='sprzedaż')),
                ('ulica', models.CharField(max_length=60, blank=True)),
                ('numer', models.CharField(max_length=10, blank=True)),
                ('kod_pocztowy', models.CharField(max_length=6, blank=True)),
                ('image', models.ImageField(upload_to='images/%y/%m/%d', blank=True)),
                ('rynek', models.CharField(choices=[('pierwotny', 'pierwotny'), ('wtórny', 'wtórny')], max_length=12, default='wtórny')),
                ('oferent', models.CharField(choices=[('właściciel', 'właściciel'), ('biuro pośrednictwa', 'biuro pośrednictwa'), ('deweloper', 'deweloper')], max_length=30, default='właściciel')),
                ('status', models.CharField(choices=[('draft', 'Roboczy'), ('published', 'Opublikowana')], max_length=15, default='draft')),
                ('klient_docelowy', models.CharField(choices=[('dowolny', 'dowolny'), ('osoba fizyczna', 'osoba fizyczna'), ('firma', 'firma'), ('biuro pośrednictwa', 'biuro pośrednictwa'), ('student', 'student'), ('inwestor', 'inwestor')], max_length=30, default='dowolny')),
                ('opis_nieruchomosci', models.TextField(blank=True)),
                ('telefon', models.CharField(max_length=20, blank=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('cena', models.DecimalField(max_digits=12, blank=True, decimal_places=0, default=0)),
                ('cenamq', models.DecimalField(max_digits=12, blank=True, decimal_places=0, default=0)),
                ('link1', models.URLField(blank=True)),
                ('link2', models.URLField(blank=True)),
                ('link3', models.URLField(blank=True)),
                ('link4', models.URLField(blank=True)),
                ('rodzaj_oferty', models.CharField(choices=[('publiczna', 'publiczna'), ('bithouse', 'Bithouse')], max_length=30, default='publiczna')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('edytowalna', models.BooleanField(default=False)),
                ('dzielnica', models.ForeignKey(related_name='nieruchomosci', default=1, to='realestate.Dzielnica')),
                ('miejscowosc', models.ForeignKey(related_name='nieruchomosci', default=1, to='realestate.Miejscowosc')),
                ('user', models.ForeignKey(blank=True, related_name='nieruchomosci', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
        migrations.CreateModel(
            name='Nieruchomstaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stok', models.PositiveIntegerField(blank=True, default=0)),
                ('akcept', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('paid', models.BooleanField(default=False)),
                ('updatedpaid', models.CharField(max_length=20)),
                ('nieruchomosc', models.OneToOneField(related_name='linkusik', to='realestate.Nieruchomosc')),
            ],
            options={
                'ordering': ('updatedpaid',),
            },
        ),
        migrations.CreateModel(
            name='Pokoje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('powierz_mieszkania', models.DecimalField(max_digits=12, blank=True, decimal_places=0, default=0)),
                ('rodzaj_zabud', models.CharField(choices=[('wolnostojący', 'wolnostojący'), ('bliźniak', 'bliźniak'), ('szeregówka', 'szeregówka'), ('kamienica', 'kamienica'), ('blok', 'blok'), ('apartamentowiec', 'apartamentowiec'), ('loft', 'loft')], max_length=30, blank=True)),
                ('rodzaj_mieszkania', models.CharField(choices=[('jednopoziomowe', 'jednopoziomowe'), ('dwupoziomowe', 'dwupoziomowe'), ('poddasze', 'poddasze'), ('loft', 'loft')], max_length=30, default='jednopoziomowe')),
                ('pietro', models.CharField(max_length=3)),
                ('czynsz', models.DecimalField(max_digits=12, blank=True, decimal_places=0, default=0)),
                ('kaucja', models.DecimalField(max_digits=12, blank=True, decimal_places=0, default=0)),
                ('dostepne', models.CharField(max_length=30, blank=True)),
                ('ilosc_pokoi', models.PositiveIntegerField(default=0)),
                ('ilosc_osob', models.CharField(choices=[('jednoosobowy', 'jednoosobowy'), ('dwuosobowy', 'dwuosobowy'), ('trzyosobowy', 'trzyosobowy'), ('czteroosobowy', 'czteroosobowy'), ('wiecej', 'więcej')], max_length=3, default='jednoosobowy')),
                ('prad', models.BooleanField(default=False)),
                ('gaz', models.BooleanField(default=False)),
                ('woda', models.BooleanField(default=False)),
                ('kanalizacja', models.BooleanField(default=False)),
                ('szambo', models.BooleanField(default=False)),
                ('oczyszczalnia', models.BooleanField(default=False)),
                ('telefon', models.BooleanField(default=False)),
                ('internet', models.BooleanField(default=False)),
                ('tel_kablowa', models.BooleanField(default=False)),
                ('miejskie', models.BooleanField(default=False)),
                ('gazowe', models.BooleanField(default=False)),
                ('olejowe', models.BooleanField(default=False)),
                ('elektryczne', models.BooleanField(default=False)),
                ('weglowe', models.BooleanField(default=False)),
                ('piece_kaflowe', models.BooleanField(default=False)),
                ('kominkowe', models.BooleanField(default=False)),
                ('kolektor_sloneczny', models.BooleanField(default=False)),
                ('pompa_ciepla', models.BooleanField(default=False)),
                ('biomasa', models.BooleanField(default=False)),
                ('meble', models.BooleanField(default=False)),
                ('meble_czesc', models.BooleanField(default=False)),
                ('kuchenka', models.BooleanField(default=False)),
                ('pralka', models.BooleanField(default=False)),
                ('lodowka', models.BooleanField(default=False)),
                ('zmywarka', models.BooleanField(default=False)),
                ('piekarnik', models.BooleanField(default=False)),
                ('mikrofala', models.BooleanField(default=False)),
                ('telewizor', models.BooleanField(default=False)),
                ('nieruchomosc', models.OneToOneField(related_name='pokojes', to='realestate.Nieruchomosc')),
            ],
            options={
                'ordering': ('nieruchomosc',),
            },
        ),
        migrations.CreateModel(
            name='Powierzchnie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('powierz_nieruchomosci', models.DecimalField(max_digits=12, blank=True, decimal_places=0, default=0)),
                ('powierz_dzialki', models.DecimalField(max_digits=12, blank=True, decimal_places=0, default=0)),
                ('rodzaj_nieruchom', models.CharField(choices=[('lokal handlowy', 'lokal handlowy'), ('lokal gastronomiczny', 'lokal gastronomiczny'), ('klub', 'klub'), ('pub', 'pub'), ('powierzchnia handlowa', 'powierzchnia handlowa'), ('powierzchnia magazynowa', 'powierzchnia magazynowa'), ('hala magazynowa', 'hala magazynowa'), ('hala przemysłowa', 'hala przemysłowa'), ('powierzchnia biurowa', 'powierzchnia biurowa'), ('powierzchnia przemysłowa', 'powierzchnia przemysłowa'), ('powierzchnia hotelowa', 'powierzchnia hotelowa'), ('klinika', 'klinika'), ('przychodnia', 'przychodnia'), ('gabinet stomatologiczny', 'gabinet stomatologiczny')], max_length=30, blank=True)),
                ('pozycja_nieruchom', models.CharField(choices=[('nieruchomość samodzielna', 'nieruchomość samodzielna'), ('część nieruchomości', 'część nieruchomości')], max_length=30, blank=True)),
                ('rok_budowy', models.CharField(max_length=4, blank=True)),
                ('czynsz', models.DecimalField(max_digits=12, blank=True, decimal_places=0, default=0)),
                ('kaucja', models.DecimalField(max_digits=12, blank=True, decimal_places=0, default=0)),
                ('dostepne', models.CharField(max_length=30, blank=True)),
                ('polozenie_lokalu', models.CharField(choices=[('odzielny obiekt', 'odzielny obiekt'), ('biurowiec', 'biurowiec'), ('centrum handlowe', 'centrum handlowe'), ('obiekt przemysłowy', 'obiekt przemysłowy'), ('hala magazynowa', 'hala magazynowa'), ('blok', 'blok'), ('kamienica', 'kamienica'), ('inny', 'inny')], max_length=30, blank=True)),
                ('rodz_materialu', models.CharField(choices=[('cegła', 'cegła'), ('silikat', 'silikat'), ('beton komórkowy', 'beton komórkowy'), ('konstrukcja stalowa', 'konstrukcja stalowa'), ('konstrukcja żel-betonowa', 'konstrukcja żel-betonowa'), ('silikat', 'silikat'), ('keramzyt', 'keramzyt'), ('wielka płyta', 'wielka płyta'), ('beton', 'beton'), ('drewno', 'drewno'), ('inne', 'inne')], max_length=30, blank=True)),
                ('dach', models.CharField(choices=[('płaski', 'płaski'), ('skośny', 'skośny')], max_length=30, blank=True)),
                ('pokrycie_dach', models.CharField(choices=[('dachówka ceramiczna', 'dachówka ceramiczna'), ('blachodachówka', 'blachodachówka'), ('dachówka inna', 'dachówka inna'), ('eternit', 'eternit'), ('papa', 'papa'), ('gont', 'gont'), ('łupek', 'łupek'), ('strzecha', 'strzecha'), ('inne', 'inne')], max_length=30, blank=True)),
                ('stan_wykonczenia', models.CharField(choices=[('do użytku', 'do użytku'), ('do adaptacji', 'do adaptacji'), ('do remontu', 'do remontu'), ('inne', 'inne')], max_length=30, blank=True)),
                ('okna', models.CharField(choices=[('drewniane', 'drewniane'), ('plastikowe', 'plastikowe'), ('aluminiowe', 'aluminiowe'), ('stalowe', 'stalowe')], max_length=30, blank=True)),
                ('posadzka', models.CharField(choices=[('pylna', 'pylna'), ('niepylna', 'niepylna'), ('specjalna', 'specjalna'), ('inna', 'inna')], max_length=30, blank=True)),
                ('parking', models.CharField(choices=[('asfalt', 'asfalt'), ('beton', 'beton'), ('kostka brukowa', 'kostka brukowa'), ('utwardzony', 'utwardzony'), ('nieutwardzony', 'nieutwardzony'), ('brak', 'brak'), ('inny', 'inny')], max_length=30, blank=True)),
                ('ilosc_kond', models.PositiveIntegerField(default=0)),
                ('ilosc_pokoi', models.PositiveIntegerField(default=0)),
                ('klimatyzacja', models.BooleanField(default=False)),
                ('prad', models.BooleanField(default=False)),
                ('gaz', models.BooleanField(default=False)),
                ('woda', models.BooleanField(default=False)),
                ('kanalizacja', models.BooleanField(default=False)),
                ('szambo', models.BooleanField(default=False)),
                ('telefon', models.BooleanField(default=False)),
                ('internet', models.BooleanField(default=False)),
                ('tel_kablowa', models.BooleanField(default=False)),
                ('monitoring', models.BooleanField(default=False)),
                ('oczyszczalnia', models.BooleanField(default=False)),
                ('ogrzewanie', models.CharField(choices=[('miejskie', 'miejskie'), ('gazowe', 'gazowe'), ('olejowe', 'olejowe'), ('węglowe', 'węglowe'), ('kolektory słoneczne', 'kolektory słoneczne'), ('inne', 'inne'), ('brak', 'brak')], max_length=30, blank=True)),
                ('ogrodzenie', models.CharField(choices=[('drewniane', 'drewniane'), ('metalowe', 'metalowe'), ('betonowe', 'betonowe'), ('murowane', 'murowane'), ('siatka', 'siatka'), ('żywopłot', 'żywopłot'), ('inne', 'inne')], max_length=30, blank=True)),
                ('dojazd', models.CharField(choices=[('asfalt', 'asfalt'), ('utwardzony', 'utwardzony'), ('nieutwardzony', 'nieutwardzony')], max_length=30, blank=True)),
                ('teren_przemyslowy', models.BooleanField(default=False)),
                ('teren_zdrojowy', models.BooleanField(default=False)),
                ('teren_turystyczny', models.BooleanField(default=False)),
                ('las', models.BooleanField(default=False)),
                ('gory', models.BooleanField(default=False)),
                ('jezioro', models.BooleanField(default=False)),
                ('morze', models.BooleanField(default=False)),
                ('teren_otwarty', models.BooleanField(default=False)),
                ('nieruchomosc', models.OneToOneField(related_name='powierzchnies', to='realestate.Nieruchomosc')),
            ],
            options={
                'ordering': ('nieruchomosc',),
            },
        ),
        migrations.AddField(
            model_name='mieszkania',
            name='nieruchomosc',
            field=models.OneToOneField(related_name='mieszkanias', to='realestate.Nieruchomosc'),
        ),
        migrations.AddField(
            model_name='komercyjne',
            name='nieruchomosc',
            field=models.OneToOneField(related_name='komercyjnes', to='realestate.Nieruchomosc'),
        ),
        migrations.AddField(
            model_name='imageitem',
            name='nieruchomosc',
            field=models.ForeignKey(related_name='imageitems', to='realestate.Nieruchomosc'),
        ),
        migrations.AddField(
            model_name='garage',
            name='nieruchomosc',
            field=models.OneToOneField(related_name='garages', to='realestate.Nieruchomosc'),
        ),
        migrations.AddField(
            model_name='dzialki',
            name='nieruchomosc',
            field=models.OneToOneField(related_name='dzialki', to='realestate.Nieruchomosc'),
        ),
        migrations.AddField(
            model_name='domy',
            name='nieruchomosc',
            field=models.OneToOneField(related_name='domys', to='realestate.Nieruchomosc'),
        ),
        migrations.AddField(
            model_name='dewelopr',
            name='nieruchomosc',
            field=models.OneToOneField(related_name='dewelopers', to='realestate.Nieruchomosc'),
        ),
    ]