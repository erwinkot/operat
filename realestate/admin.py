from django.contrib import admin
from .models import Profilefirm, Wojewodztwo, Powiat, Gmina, Miejscowosc, Dzielnica, Nieruchomosc, Nieruchomstaff, Dzialki, Domy, Mieszkania, Komercyjne, Powierzchnie, ImageItem

class WojewodztwoAdmin(admin.ModelAdmin):
	list_display = ['nazwa', 'slug', 'wojewoda']
	prepopulated_fields = {'slug': ('nazwa',)}

admin.site.register(Wojewodztwo, WojewodztwoAdmin)


class PowiatAdmin(admin.ModelAdmin):
	list_display = ['nazwa', 'slug', 'starosta', 'wojewodztwo']
	prepopulated_fields = {'slug': ('nazwa',)}

admin.site.register(Powiat, PowiatAdmin)



class GminaAdmin(admin.ModelAdmin):
	list_display = ['nazwa', 'slug', 'wojt', 'powiat']
	prepopulated_fields = {'slug': ('nazwa',)}

admin.site.register(Gmina, GminaAdmin)



class MiejscowoscAdmin(admin.ModelAdmin):
	list_display = ['id', 'nazwa', 'slug', 'profil', 'gmina']
	prepopulated_fields = {'slug': ('nazwa',)}

admin.site.register(Miejscowosc, MiejscowoscAdmin)


class DzielnicaAdmin(admin.ModelAdmin):
	list_display = ['id', 'nazwa', 'slug', 'miejscowosc']
	prepopulated_fields = {'slug': ('nazwa',)}

admin.site.register(Dzielnica, DzielnicaAdmin)




class ProfilefirmAdmin(admin.ModelAdmin):
	list_display = ['id', 'nazwa', 'adres_firmy', 'kod_pocztowy', 'miejscowosc', 'nip', 'nr_ewid','regon', 'profil', 'rodzaj_firmy']

admin.site.register(Profilefirm, ProfilefirmAdmin)



class ImageItemInline(admin.TabularInline):
	model = ImageItem



class NieruchomoscAdmin(admin.ModelAdmin):
	list_display = ['id', 'user', 'profil', 'nazwa_opis', 'rodzaj_transakcji', 'ulica', 'numer', 'kod_pocztowy', 'miejscowosc', 'image', 'rynek', 'oferent','status', 'klient_docelowy', 'opis_nieruchomosci', 'telefon', 'email', 'cena', 'cenamq', 'rodzaj_oferty', 'publish', 'created', 'updated', 'edytowalna']
	inlines = [ImageItemInline]
	
admin.site.register(Nieruchomosc, NieruchomoscAdmin)



class NieruchomstaffAdmin(admin.ModelAdmin):
	list_display = ['id', 'nieruchomosc', 'stok', 'akcept', 'active', 'paid', 'updatedpaid']

admin.site.register(Nieruchomstaff, NieruchomstaffAdmin)


class DzialkiAdmin(admin.ModelAdmin):
	list_display = ['id', 'nieruchomosc', 'typ_dzialki', 'powi_dzialki', 'status_dzial', 'przeznaczenie_dzial', 'info_mpzp', 'dojazd', 'prad', 'gaz', 'woda', 'kanalizacja', 'szambo', 'oczyszczalnia', 'telefon', 'las', 'gory', 'jezioro', 'morze', 'teren_otwarty']

admin.site.register(Dzialki, DzialkiAdmin)



class DomyAdmin(admin.ModelAdmin):
	list_display = ['nieruchomosc', 'powierz_domu', 'powierz_dzial', 'status_dzial', 'rodzaj_domu', 'rok_budowy', 'czynsz', 'dostepne', 'rodz_materialu', 'dach', 'pokrycie_dach', 'stan_wykonczenia', 'okna', 'ilosc_kond', 'ilosc_pokoi', 'ilosc_lazen', 'ilosc_kuchni', 'piwnice', 'garaz', 'poddasze', 'basen', 'klimatyzacja', 'prad', 'gaz', 'woda', 'kanalizacja', 'szambo', 'oczyszczalnia', 'telefon', 'internet', 'tel_kablowa', 'miejskie', 'gazowe', 'olejowe', 'elektryczne', 'weglowe', 'piece_kaflowe', 'kominkowe', 'kolektor_sloneczny', 'pompa_ciepla', 'biomasa', 'ogrodzenie', 'dojazd', 'teren_zamkniety', 'monitoring', 'alarm', 'drzwi_anty', 'rolety', 'domofon', 'las', 'gory', 'jezioro', 'morze', 'teren_otwarty']

admin.site.register(Domy, DomyAdmin)



class MieszkaniaAdmin(admin.ModelAdmin):
	list_display = ['nieruchomosc', 'powierz_mieszkania', 'rodzaj_zabud', 'rodzaj_mieszkania', 'pietro', 'rok_budowy', 'czynsz', 'kaucja', 'dostepne', 'rodz_materialu', 'stan_wykonczenia', 'okna', 'ilosc_kond', 'ilosc_pokoi', 'ilosc_lazen', 'ilosc_kuchni', 'winda', 'garaz', 'parking', 'piwnica', 'klimatyzacja', 'balkon', 'taras', 'ogrodek',  'prad', 'gaz', 'woda', 'kanalizacja', 'szambo', 'oczyszczalnia', 'telefon', 'internet', 'tel_kablowa', 'miejskie', 'gazowe', 'olejowe', 'elektryczne', 'weglowe', 'piece_kaflowe', 'kominkowe', 'kolektor_sloneczny', 'pompa_ciepla', 'biomasa', 'dojazd', 'teren_zamkniety', 'monitoring', 'alarm', 'drzwi_anty', 'rolety', 'domofon', 'meble', 'meble_czesc', 'kuchenka', 'pralka', 'lodowka', 'zmywarka', 'piekarnik', 'mikrofala', 'telewizor']

admin.site.register(Mieszkania, MieszkaniaAdmin)



class KomercyjneAdmin(admin.ModelAdmin):
	list_display = ['nieruchomosc', 'powierz_nieruchomosci', 'powierz_dzialki', 'status_dzial', 'info_mpzp', 'rodzaj_nieruchom', 'pozycja_nieruchom', 'rok_budowy', 'polozenie_lokalu', 'rodz_materialu', 'dach', 'pokrycie_dach',  'stan_wykonczenia', 'okna', 'posadzka', 'parking', 'ilosc_kond', 'ilosc_pokoi', 'klimatyzacja',  'prad', 'gaz', 'woda', 'kanalizacja', 'szambo', 'telefon', 'internet', 'tel_kablowa', 'monitoring', 'oczyszczalnia', 'ogrzewanie', 'ogrodzenie', 'dojazd', 'teren_przemyslowy', 'teren_zdrojowy', 'teren_turystyczny', 'las', 'gory', 'jezioro', 'morze', 'teren_otwarty']

admin.site.register(Komercyjne, KomercyjneAdmin)



class PowierzchnieAdmin(admin.ModelAdmin):
	list_display = ['nieruchomosc', 'powierz_nieruchomosci', 'powierz_dzialki', 'rodzaj_nieruchom', 'pozycja_nieruchom', 'rok_budowy', 'czynsz', 'kaucja', 'dostepne', 'polozenie_lokalu', 'rodz_materialu', 'dach', 'pokrycie_dach',  'stan_wykonczenia', 'okna', 'posadzka', 'parking', 'ilosc_kond', 'ilosc_pokoi', 'klimatyzacja',  'prad', 'gaz', 'woda', 'kanalizacja', 'szambo', 'telefon', 'internet', 'tel_kablowa', 'monitoring', 'oczyszczalnia', 'ogrzewanie', 'ogrodzenie', 'dojazd', 'teren_przemyslowy', 'teren_zdrojowy', 'teren_turystyczny', 'las', 'gory', 'jezioro', 'morze', 'teren_otwarty']

admin.site.register(Powierzchnie, PowierzchnieAdmin)