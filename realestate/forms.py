from django import forms
from django.contrib.auth.models import User
from .models import Profilefirm, Nieruchomosc, Nieruchomstaff, Dzialki, Domy, Mieszkania, Pokoje, Garage, Komercyjne, Powierzchnie, ImageItem


class ProfileFirmEditForm(forms.ModelForm):
	class Meta:
		model = Profilefirm
		fields = ('nazwa', 'adres_firmy', 'kod_pocztowy', 'miejscowosc', 'nip', 'nr_ewid', 'regon', 'profil', 'rodzaj_firmy')
		

class SprFirm(forms.Form):
	nip_firmy = forms.CharField(max_length=10)
	

class NieruchomoscEditForm(forms.ModelForm):
	class Meta:
		model = Nieruchomosc
		fields = (	'nazwa_opis',
					'ulica', 
					'numer',
					'kod_pocztowy',
					'miejscowosc',
					'image',
					'opis_nieruchomosci',
					'cena',
					'cenamq',
					'link1',
					'link2',
					'link3',
					'link4',
					'rodzaj_transakcji',
					'rynek',
					'oferent',
					'status',
					'klient_docelowy',
					'telefon',
					'email',
					'rodzaj_oferty',
					'publish',
					)
					
					

					
class NieruchomstaffEditForm(forms.ModelForm):
	class Meta:
		model = Nieruchomstaff
		fields = ('stok', 'akcept', 'active', 'paid', 'updatedpaid')
		


class DzialkiEditForm(forms.ModelForm):
	class Meta:
		model = Dzialki
		fields = ('typ_dzialki', 
					'powi_dzialki', 
					'status_dzial', 
					'przeznaczenie_dzial', 
					'info_mpzp', 'dojazd', 
					'prad', 
					'gaz', 
					'woda', 
					'kanalizacja', 
					'szambo', 
					'oczyszczalnia', 
					'telefon', 
					'las', 
					'gory', 
					'jezioro', 
					'morze', 
					'teren_otwarty')
					
					
					
class DomyEditForm(forms.ModelForm):
	class Meta:
		model = Domy
		fields = (	'powierz_domu', 
					'powierz_dzial', 
					'status_dzial', 
					'rodzaj_domu', 
					'rok_budowy',
					'czynsz',
					'kaucja',
					'dostepne', 
					'rodz_materialu', 
					'dach', 
					'pokrycie_dach', 
					'stan_wykonczenia', 
					'okna', 
					'ilosc_kond', 
					'ilosc_pokoi', 
					'ilosc_lazen', 
					'ilosc_kuchni', 
					'piwnice', 
					'garaz', 
					'poddasze', 
					'basen', 
					'klimatyzacja', 
					'prad', 
					'gaz', 
					'woda', 
					'kanalizacja', 
					'szambo', 
					'oczyszczalnia', 
					'telefon', 
					'internet', 
					'tel_kablowa', 
					'miejskie', 
					'gazowe', 
					'olejowe', 
					'elektryczne', 
					'weglowe', 
					'piece_kaflowe', 
					'kominkowe', 
					'kolektor_sloneczny', 
					'pompa_ciepla', 
					'biomasa', 
					'ogrodzenie', 
					'dojazd', 
					'teren_zamkniety', 
					'monitoring', 
					'alarm', 
					'drzwi_anty', 
					'rolety', 
					'domofon', 
					'las', 
					'gory', 
					'jezioro', 
					'morze', 
					'teren_otwarty',
					'meble', 
					'meble_czesc', 
					'kuchenka', 
					'pralka', 
					'lodowka', 
					'zmywarka', 
					'piekarnik', 
					'mikrofala', 
					'telewizor')

					
class MieszkaniaEditForm(forms.ModelForm):
	class Meta:
		model = Mieszkania
		fields = (	'powierz_mieszkania', 
					'rodzaj_zabud', 
					'rodzaj_mieszkania', 
					'pietro', 
					'rok_budowy', 
					'czynsz', 
					'kaucja', 
					'dostepne', 
					'rodz_materialu', 
					'stan_wykonczenia', 
					'okna', 
					'ilosc_kond', 
					'ilosc_pokoi', 
					'ilosc_lazen', 
					'ilosc_kuchni', 
					'winda', 
					'garaz', 
					'parking', 
					'piwnica', 
					'klimatyzacja', 
					'balkon', 
					'taras', 
					'ogrodek',  
					'prad', 
					'gaz', 
					'woda', 
					'kanalizacja', 
					'szambo', 
					'oczyszczalnia', 
					'telefon', 
					'internet', 
					'tel_kablowa', 
					'miejskie', 
					'gazowe', 
					'olejowe', 
					'elektryczne', 
					'weglowe', 
					'piece_kaflowe', 
					'kominkowe', 
					'kolektor_sloneczny', 
					'pompa_ciepla', 
					'biomasa', 
					'dojazd', 
					'teren_zamkniety', 
					'monitoring', 
					'alarm', 
					'drzwi_anty', 
					'rolety', 
					'domofon', 
					'meble', 
					'meble_czesc', 
					'kuchenka', 
					'pralka', 
					'lodowka', 
					'zmywarka', 
					'piekarnik', 
					'mikrofala', 
					'telewizor')
					
					
					
class PokojeEditForm(forms.ModelForm):
	class Meta:
		model = Pokoje
		fields = (	'powierz_mieszkania', 
					'rodzaj_zabud', 
					'rodzaj_mieszkania', 
					'pietro', 
					'czynsz', 
					'kaucja', 
					'dostepne', 
					'ilosc_pokoi', 
					'ilosc_osob', 
					'prad', 
					'gaz', 
					'woda', 
					'kanalizacja', 
					'szambo', 
					'oczyszczalnia', 
					'telefon', 
					'internet', 
					'tel_kablowa', 
					'miejskie', 
					'gazowe', 
					'olejowe', 
					'elektryczne', 
					'weglowe', 
					'piece_kaflowe', 
					'kominkowe', 
					'kolektor_sloneczny', 
					'pompa_ciepla', 
					'biomasa', 
					'meble', 
					'meble_czesc', 
					'kuchenka', 
					'pralka', 
					'lodowka', 
					'zmywarka', 
					'piekarnik', 
					'mikrofala', 
					'telewizor')
					
					
					
class GarageEditForm(forms.ModelForm):
	class Meta:
		model = Garage
		fields = (	'powierz_garage', 
					'rodzaj_zabud', 
					'konstr_garage', 
					'czynsz', 
					'kaucja', 
					'dostepne', 
					'ogrzewanie', 
					'oswietlenie', 
					'woda', 
					'kanalizacja', 
					'szambo')
					
						


					
					
					
class KomercyjneEditForm(forms.ModelForm):
	class Meta:
		model = Komercyjne
		fields = (	'powierz_nieruchomosci', 
					'powierz_dzialki', 
					'status_dzial', 
					'info_mpzp', 
					'rodzaj_nieruchom', 
					'pozycja_nieruchom', 
					'rok_budowy', 
					'rodz_materialu', 
					'dach', 
					'pokrycie_dach',  
					'stan_wykonczenia', 
					'okna', 
					'posadzka', 
					'parking', 
					'ilosc_kond', 
					'ilosc_pokoi', 
					'klimatyzacja',  
					'prad', 
					'gaz', 
					'woda', 
					'kanalizacja', 
					'szambo', 
					'oczyszczalnia',
					'telefon', 
					'internet', 
					'tel_kablowa', 
					'monitoring', 
					'oczyszczalnia', 
					'ogrzewanie', 
					'ogrodzenie', 
					'dojazd', 
					'teren_przemyslowy', 
					'teren_zdrojowy', 
					'teren_turystyczny', 
					'las', 
					'gory', 
					'jezioro', 
					'morze', 
					'teren_otwarty')
					
					
class PowierzchnieEditForm(forms.ModelForm):
	class Meta:
		model = Powierzchnie
		fields = (	'powierz_nieruchomosci', 
					'powierz_dzialki', 
					'rodzaj_nieruchom', 
					'pozycja_nieruchom', 
					'rok_budowy', 'czynsz', 
					'kaucja', 'dostepne', 
					'polozenie_lokalu', 
					'rodz_materialu', 
					'dach', 
					'pokrycie_dach',  
					'stan_wykonczenia', 
					'okna', 
					'posadzka', 
					'parking', 
					'ilosc_kond', 
					'ilosc_pokoi', 
					'klimatyzacja',  
					'prad', 
					'gaz', 
					'woda', 
					'kanalizacja', 
					'szambo', 
					'oczyszczalnia',
					'telefon', 
					'internet', 
					'tel_kablowa', 
					'monitoring', 
					'oczyszczalnia', 
					'ogrzewanie', 
					'ogrodzenie', 
					'dojazd', 
					'teren_przemyslowy', 
					'teren_zdrojowy', 
					'teren_turystyczny', 
					'las', 
					'gory', 
					'jezioro', 
					'morze', 
					'teren_otwarty')
					
					
class ImageItemEditForm(forms.ModelForm):
	class Meta:
		model = ImageItem
		fields = ('title', 'image', 'opis')	