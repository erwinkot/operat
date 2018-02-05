from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
#from .models import 
from .forms import FiltrMiejscForm, FiltrIloscPokForm, FiltrCenaForm, FiltrPowierzDomuForm, FiltrRynekForm, FiltrOferentForm, FiltrPowierzDzialForm, FiltrRodzZabForm, FiltrCenaWynForm, FiltrPrzezDzialForm, FiltrTypDzialkiForm, FiltrPowMieForm, FiltrCenaMieSprzForm, FiltrWykonczMieForm, FiltrCenaMieWynForm, FiltrMebleForm
from realestate.models import Nieruchomosc, Dzialki, Domy, Mieszkania, Komercyjne, Miejscowosc, ImageItem



def bithouse_start(request):
		
	return render(request, 'bithouse/presentbit/startbit.html',)
	

def bithouse_home(request):
		
	return render(request, 'bithouse/presentbit/home.html')
	


	



def ogloszenia(request):
	
	nieruchomoscs = Nieruchomosc.objects.all()
	
					
	return render(request, 'bithouse/presentbit/ogloszenia.html')
			

			
			
def ogloszenia_dzialki(request, nieruchomoscs=None):
	
	if request.method == 'POST':
	
		filtrmiejsc_form = FiltrMiejscForm(request.POST)
		filtroferent_form = FiltrOferentForm(request.POST)
		filtrcena_form = FiltrCenaForm(request.POST)
		filtrpowdzial_form = FiltrPowierzDzialForm(request.POST)
		filtrtypdzialki_form = FiltrTypDzialkiForm(request.POST)
		filtrprzezndzial_form = FiltrPrzezDzialForm(request.POST)
		if filtrmiejsc_form.is_valid():
			cd = filtrmiejsc_form.cleaned_data
			nieruchomoscs = Nieruchomosc.objects.filter(profil='dzialka', rodzaj_transakcji='sprzedaż', miejscowosc=cd['miejscowosc'])
			
			if filtroferent_form.is_valid():
				of = filtroferent_form.cleaned_data
			if of['oferent'] == '1':
				nieruchomoscs = nieruchomoscs.filter(oferent='właściciel')
			if of['oferent'] == '2':
				nieruchomoscs = nieruchomoscs.filter(oferent='biuro pośrednictwa')
			if of['oferent'] == '3':
				nieruchomoscs = nieruchomoscs.filter(oferent='deweloper')
			if filtrcena_form.is_valid():
				cc = filtrcena_form.cleaned_data
			if cc['cena'] == '0':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(0, 99999999))
			if cc['cena'] == '1':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(0, 499999))
			if cc['cena'] == '2':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(500000, 999999))
			if cc['cena'] == '3':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(1000000, 1999999))
			if cc['cena'] == '4':
				nieruchomoscs = nieruchomoscs.filter(cena__gte=(2000000))
			if filtrpowdzial_form.is_valid():
				pd = filtrpowdzial_form.cleaned_data
			if pd['powierz_dzial'] == '0':
				nieruchomoscs = nieruchomoscs.filter(dzialki__powi_dzialki__range=(1, 9999999))
			if pd['powierz_dzial'] == '1':
				nieruchomoscs = nieruchomoscs.filter(dzialki__powi_dzialki__range=(1, 199))
			if pd['powierz_dzial'] == '2':
				nieruchomoscs = nieruchomoscs.filter(dzialki__powi_dzialki__range=(200, 399))
			if pd['powierz_dzial'] == '3':
				nieruchomoscs = nieruchomoscs.filter(dzialki__powi_dzialki__range=(400, 799))
			if pd['powierz_dzial'] == '4':
				nieruchomoscs = nieruchomoscs.filter(dzialki__powi_dzialki__range=(800, 1199))
			if pd['powierz_dzial'] == '5':
				nieruchomoscs = nieruchomoscs.filter(dzialki__powi_dzialki__range=(1200, 1999))
			if pd['powierz_dzial'] == '6':
				nieruchomoscs = nieruchomoscs.filter(dzialki__powi_dzialki__range=(2000, 3999))
			if pd['powierz_dzial'] == '7':
				nieruchomoscs = nieruchomoscs.filter(dzialki__powi_dzialki__gte=(4000))
			if filtrtypdzialki_form.is_valid():
				tdz = filtrtypdzialki_form.cleaned_data
			if tdz['typ_dzialki'] == '1':
				nieruchomoscs = nieruchomoscs.filter(dzialki__typ_dzialki='budowlana')
			if tdz['typ_dzialki'] == '2':
				nieruchomoscs = nieruchomoscs.filter(dzialki__typ_dzialki='rolna')
			if tdz['typ_dzialki'] == '3':
				nieruchomoscs = nieruchomoscs.filter(dzialki__typ_dzialki='rekreacyjna')
			if tdz['typ_dzialki'] == '4':
				nieruchomoscs = nieruchomoscs.filter(dzialki__typ_dzialki='inwestycyjna')
			if tdz['typ_dzialki'] == '5':
				nieruchomoscs = nieruchomoscs.filter(dzialki__typ_dzialki='leśna')
			if tdz['typ_dzialki'] == '6':
				nieruchomoscs = nieruchomoscs.filter(dzialki__typ_dzialki='siedliskowa')
			if filtrprzezndzial_form.is_valid():
				pdz = filtrprzezndzial_form.cleaned_data
			if pdz['przeznaczenie_dzial'] == '1':
				nieruchomoscs = nieruchomoscs.filter(dzialki__przeznaczenie_dzial='jednorodzinne')
			if pdz['przeznaczenie_dzial'] == '2':
				nieruchomoscs = nieruchomoscs.filter(dzialki__przeznaczenie_dzial='wielorodzinne')
			if pdz['przeznaczenie_dzial'] == '3':
				nieruchomoscs = nieruchomoscs.filter(dzialki__przeznaczenie_dzial='wysokie')
			if pdz['przeznaczenie_dzial'] == '4':
				nieruchomoscs = nieruchomoscs.filter(dzialki__przeznaczenie_dzial='usługi i handel')
			if pdz['przeznaczenie_dzial'] == '5':
				nieruchomoscs = nieruchomoscs.filter(dzialki__przeznaczenie_dzial='hotelowe')
			if pdz['przeznaczenie_dzial'] == '6':
				nieruchomoscs = nieruchomoscs.filter(dzialki__przeznaczenie_dzial='medyczne')
			if pdz['przeznaczenie_dzial'] == '6':
				nieruchomoscs = nieruchomoscs.filter(dzialki__przeznaczenie_dzial='pozostałe')
			
						
			return render(request, 'bithouse/presentbit/dzialki.html', {'nieruchomoscs': nieruchomoscs, 
																					'filtrmiejsc_form': filtrmiejsc_form,
																					'filtroferent_form': filtroferent_form,
																					'filtrcena_form': filtrcena_form,
																					'filtrpowdzial_form': filtrpowdzial_form,
																					'filtrtypdzialki_form': filtrtypdzialki_form,
																					'filtrprzezndzial_form': filtrprzezndzial_form})
			
			
	else:
		nieruchomoscs = Nieruchomosc.objects.filter(profil='dzialka', rodzaj_transakcji='sprzedaż')
		filtrmiejsc_form = FiltrMiejscForm()
		filtroferent_form = FiltrOferentForm()
		filtrcena_form = FiltrCenaForm()
		filtrpowdzial_form = FiltrPowierzDzialForm()
		filtrtypdzialki_form = FiltrTypDzialkiForm()
		filtrprzezndzial_form = FiltrPrzezDzialForm()
					
		return render(request, 'bithouse/presentbit/dzialki.html', {'nieruchomoscs': nieruchomoscs, 
																				'filtrmiejsc_form': filtrmiejsc_form,
																				'filtroferent_form': filtroferent_form,
																				'filtrcena_form': filtrcena_form,
																				'filtrpowdzial_form': filtrpowdzial_form,
																				'filtrtypdzialki_form': filtrtypdzialki_form,
																				'filtrprzezndzial_form': filtrprzezndzial_form})


		
def ogloszenia_dzialki_wy(request, nieruchomosc=None):
	
	if request.method == 'POST':
	
		filtrmiejsc_form = FiltrMiejscForm(request.POST)
		filtroferent_form = FiltrOferentForm(request.POST)
		filtrpowdzial_form = FiltrPowierzDzialForm(request.POST)
		
		if filtrmiejsc_form.is_valid():
			cd = filtrmiejsc_form.cleaned_data
			nieruchomoscs = Nieruchomosc.objects.filter(profil='działka', rodzaj_transakcji='wynajem', miejscowosc=cd['miejscowosc'])
			
			if filtroferent_form.is_valid():
				of = filtroferent_form.cleaned_data
			if of['oferent'] == '1':
				nieruchomoscs = nieruchomoscs.filter(oferent='właściciel')
			if of['oferent'] == '2':
				nieruchomoscs = nieruchomoscs.filter(oferent='biuro pośrednictwa')
			if of['oferent'] == '3':
				nieruchomoscs = nieruchomoscs.filter(oferent='deweloper')
			if filtrpowdzial_form.is_valid():
				pd = filtrpowdzial_form.cleaned_data
			if pd['powierz_dzial'] == '0':
				nieruchomoscs = nieruchomoscs.filter(dzialki__powi_dzialki__range=(1, 9999999))
			if pd['powierz_dzial'] == '1':
				nieruchomoscs = nieruchomoscs.filter(dzialki__powi_dzialki__range=(1, 199))
			if pd['powierz_dzial'] == '2':
				nieruchomoscs = nieruchomoscs.filter(dzialki__powi_dzialki__range=(200, 399))
			if pd['powierz_dzial'] == '3':
				nieruchomoscs = nieruchomoscs.filter(dzialki__powi_dzialki__range=(400, 799))
			if pd['powierz_dzial'] == '4':
				nieruchomoscs = nieruchomoscs.filter(dzialki__powi_dzialki__range=(800, 1199))
			if pd['powierz_dzial'] == '5':
				nieruchomoscs = nieruchomoscs.filter(dzialki__powi_dzialki__range=(1200, 1999))
			if pd['powierz_dzial'] == '6':
				nieruchomoscs = nieruchomoscs.filter(dzialki__powi_dzialki__range=(2000, 3999))
			if pd['powierz_dzial'] == '7':
				nieruchomoscs = nieruchomoscs.filter(dzialki__powi_dzialki__gte=(4000))
				
						
			return render(request, 'bithouse/presentbit/dzialki_wy.html', {'nieruchomoscs': nieruchomoscs, 
																				'filtrmiejsc_form': filtrmiejsc_form,
																				'filtroferent_form': filtroferent_form,
																				'filtrpowdzial_form': filtrpowdzial_form})
																				
	else:
		nieruchomoscs = Nieruchomosc.objects.filter(profil='działka', rodzaj_transakcji='wynajem')
		filtrmiejsc_form = FiltrMiejscForm()
		filtroferent_form = FiltrOferentForm()
		filtrpowdzial_form = FiltrPowierzDzialForm()
					
		return render(request, 'bithouse/presentbit/dzialki_wy.html', {'nieruchomoscs': nieruchomoscs, 
																				'filtrmiejsc_form': filtrmiejsc_form,
																				'filtroferent_form': filtroferent_form,
																				'filtrpowdzial_form': filtrpowdzial_form})
		
		
	

def ogloszenia_domy(request, nieruchomoscs=None):
	
	if request.method == 'POST':
			
		filtrmiejsc_form = FiltrMiejscForm(request.POST)
		filtrrynk_form = FiltrRynekForm(request.POST)
		filtroferent_form = FiltrOferentForm(request.POST)
		filtrinn_form = FiltrIloscPokForm(request.POST)
		filtrcena_form = FiltrCenaForm(request.POST)
		filtrpowdomu_form = FiltrPowierzDomuForm(request.POST)
		filtrpowdzial_form = FiltrPowierzDzialForm(request.POST)
		filtrrodzzab_form = FiltrRodzZabForm(request.POST)
		if filtrmiejsc_form.is_valid(): 
			cd = filtrmiejsc_form.cleaned_data
			nieruchomoscs = Nieruchomosc.objects.filter(profil='dom', rodzaj_transakcji='sprzedaż', miejscowosc=cd['miejscowosc'])
			
			if filtrrynk_form.is_valid():
				ry = filtrrynk_form.cleaned_data
			if ry['rynek'] == '1':
				nieruchomoscs = nieruchomoscs.filter(rynek='wtórny')	
			if ry['rynek'] == '2':
				nieruchomoscs = nieruchomoscs.filter(rynek='pierwotny')
			if filtroferent_form.is_valid():
				of = filtroferent_form.cleaned_data
			if of['oferent'] == '1':
				nieruchomoscs = nieruchomoscs.filter(oferent='właściciel')
			if of['oferent'] == '2':
				nieruchomoscs = nieruchomoscs.filter(oferent='biuro pośrednictwa')
			if of['oferent'] == '3':
				nieruchomoscs = nieruchomoscs.filter(oferent='deweloper')
			if filtrinn_form.is_valid():
				cl = filtrinn_form.cleaned_data
			if cl['ilosc_pokoi'] == '0':
				nieruchomoscs = nieruchomoscs.filter(domys__ilosc_pokoi__gte=(1))
			if cl['ilosc_pokoi'] != '0':
				nieruchomoscs = nieruchomoscs.filter(domys__ilosc_pokoi=cl['ilosc_pokoi'])
			if cl['ilosc_pokoi'] == '12':
				nieruchomoscs = nieruchomoscs.filter(domys__ilosc_pokoi__gte=(12))
			if filtrcena_form.is_valid():
				cc = filtrcena_form.cleaned_data
			if cc['cena'] == '0':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(0, 99999999))
			if cc['cena'] == '1':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(0, 249999))
			if cc['cena'] == '2':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(250000, 499999))
			if cc['cena'] == '3':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(500000, 999999))
			if cc['cena'] == '4':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(1000000, 1999999))
			if cc['cena'] == '5':
				nieruchomoscs = nieruchomoscs.filter(cena__gte=(2000000))
			if filtrpowdomu_form.is_valid():
				cp = filtrpowdomu_form.cleaned_data
			if cp['powierz_domu'] == '0':
				nieruchomoscs = nieruchomoscs.filter(domys__powierz_domu__range=(1, 9999))
			if cp['powierz_domu'] == '1':
				nieruchomoscs = nieruchomoscs.filter(domys__powierz_domu__range=(1, 99))
			if cp['powierz_domu'] == '2':
				nieruchomoscs = nieruchomoscs.filter(domys__powierz_domu__range=(100, 199))
			if cp['powierz_domu'] == '3':
				nieruchomoscs = nieruchomoscs.filter(domys__powierz_domu__range=(200, 299))
			if cp['powierz_domu'] == '4':
				nieruchomoscs = nieruchomoscs.filter(domys__powierz_domu__range=(300, 499))
			if cp['powierz_domu'] == '5':
				nieruchomoscs = nieruchomoscs.filter(domys__powierz_domu__range=(500, 999))
			if cp['powierz_domu'] == '6':
				nieruchomoscs = nieruchomoscs.filter(domys__powierz_domu__gte=(1000))
			if filtrpowdzial_form.is_valid():
				pd = filtrpowdzial_form.cleaned_data
			if pd['powierz_dzial'] == '0':
				nieruchomoscs = nieruchomoscs.filter(domys__powierz_dzial__range=(1, 99999))
			if pd['powierz_dzial'] == '1':
				nieruchomoscs = nieruchomoscs.filter(domys__powierz_dzial__range=(1, 199))
			if pd['powierz_dzial'] == '2':
				nieruchomoscs = nieruchomoscs.filter(domys__powierz_dzial__range=(200, 399))
			if pd['powierz_dzial'] == '3':
				nieruchomoscs = nieruchomoscs.filter(domys__powierz_dzial__range=(400, 799))
			if pd['powierz_dzial'] == '4':
				nieruchomoscs = nieruchomoscs.filter(domys__powierz_dzial__range=(800, 1199))
			if pd['powierz_dzial'] == '5':
				nieruchomoscs = nieruchomoscs.filter(domys__powierz_dzial__range=(1200, 1999))
			if pd['powierz_dzial'] == '6':
				nieruchomoscs = nieruchomoscs.filter(domys__powierz_dzial__range=(2000, 3999))
			if pd['powierz_dzial'] == '7':
				nieruchomoscs = nieruchomoscs.filter(domys__powierz_dzial__gte=(4000))
			if filtrrodzzab_form.is_valid():
				rz = filtrrodzzab_form.cleaned_data
			if rz['rodzaj_domu'] == '1':
				nieruchomoscs = nieruchomoscs.filter(domys__rodzaj_domu='wolnostojący')
			if rz['rodzaj_domu'] == '2':
				nieruchomoscs = nieruchomoscs.filter(domys__rodzaj_domu='bliźniak')
			if rz['rodzaj_domu'] == '3':
				nieruchomoscs = nieruchomoscs.filter(domys__rodzaj_domu='szeregówka')
			if rz['rodzaj_domu'] == '4':
				nieruchomoscs = nieruchomoscs.filter(domys__rodzaj_domu='kamienica')
			if rz['rodzaj_domu'] == '5':
				nieruchomoscs = nieruchomoscs.filter(domys__rodzaj_domu='dworek')
			if rz['rodzaj_domu'] == '6':
				nieruchomoscs = nieruchomoscs.filter(domys__rodzaj_domu='gospodarstwo')
				
								
			return render(request, 'bithouse/presentbit/domy.html', {'nieruchomoscs': nieruchomoscs, 
																					'filtrmiejsc_form': filtrmiejsc_form,
																					'filtrrynk_form': filtrrynk_form,
																					'filtroferent_form': filtroferent_form,
																					'filtrinn_form': filtrinn_form,
																					'filtrcena_form': filtrcena_form,
																					'filtrpowdomu_form': filtrpowdomu_form,
																					'filtrpowdzial_form': filtrpowdzial_form,
																					'filtrrodzzab_form': filtrrodzzab_form})
	else:
		nieruchomoscs = Nieruchomosc.objects.filter(profil='dom', rodzaj_transakcji='sprzedaż')
		filtrmiejsc_form = FiltrMiejscForm()
		filtrrynk_form = FiltrRynekForm()
		filtroferent_form = FiltrOferentForm()
		filtrinn_form = FiltrIloscPokForm()
		filtrcena_form = FiltrCenaForm()
		filtrpowdomu_form = FiltrPowierzDomuForm()
		filtrpowdzial_form = FiltrPowierzDzialForm()
		filtrrodzzab_form = FiltrRodzZabForm()
					
		return render(request, 'bithouse/presentbit/domy.html', {'nieruchomoscs': nieruchomoscs, 
																	'filtrmiejsc_form': filtrmiejsc_form,
																	'filtrrynk_form': filtrrynk_form,
																	'filtroferent_form': filtroferent_form,
																	'filtrinn_form': filtrinn_form,
																	'filtrcena_form': filtrcena_form,
																	'filtrpowdomu_form': filtrpowdomu_form,
																	'filtrpowdzial_form': filtrpowdzial_form,
																	'filtrrodzzab_form': filtrrodzzab_form})
																	



def ogloszenia_domy_wy(request, nieruchomoscs=None):
	
	if request.method == 'POST':
	
		filtrmiejsc_form = FiltrMiejscForm(request.POST)
		filtrrynk_form = FiltrRynekForm(request.POST)
		filtroferent_form = FiltrOferentForm(request.POST)
		filtrinn_form = FiltrIloscPokForm(request.POST)
		filtrcenawy_form = FiltrCenaWynForm(request.POST)
		filtrpowdomu_form = FiltrPowierzDomuForm(request.POST)
		filtrpowdzial_form = FiltrPowierzDzialForm(request.POST)
		filtrrodzzab_form = FiltrRodzZabForm(request.POST)
		if filtrmiejsc_form.is_valid(): 
			cd = filtrmiejsc_form.cleaned_data
			nieruchomoscs = Nieruchomosc.objects.filter(profil='dom', rodzaj_transakcji='wynajem', miejscowosc=cd['miejscowosc'])
			
			if filtrrynk_form.is_valid():
				ry = filtrrynk_form.cleaned_data
			if ry['rynek'] == '1':
				nieruchomoscs = nieruchomoscs.filter(rynek='wtórny')	
			if ry['rynek'] == '2':
				nieruchomoscs = nieruchomoscs.filter(rynek='pierwotny')
			if filtroferent_form.is_valid():
				of = filtroferent_form.cleaned_data
			if of['oferent'] == '1':
				nieruchomoscs = nieruchomoscs.filter(oferent='właściciel')
			if of['oferent'] == '2':
				nieruchomoscs = nieruchomoscs.filter(oferent='biuro pośrednictwa')
			if of['oferent'] == '3':
				nieruchomoscs = nieruchomoscs.filter(oferent='deweloper')
			if filtrinn_form.is_valid():
				cl = filtrinn_form.cleaned_data
			if cl['ilosc_pokoi'] == '0':
				nieruchomoscs = nieruchomoscs.filter(domys__ilosc_pokoi__gte=(1))
			if cl['ilosc_pokoi'] != '0':
				nieruchomoscs = nieruchomoscs.filter(domys__ilosc_pokoi=cl['ilosc_pokoi'])
			if cl['ilosc_pokoi'] == '12':
				nieruchomoscs = nieruchomoscs.filter(domys__ilosc_pokoi__gte=(12))
			if filtrcenawy_form.is_valid():
				cc = filtrcenawy_form.cleaned_data
			if cc['cena'] == '0':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(0, 99999999))
			if cc['cena'] == '1':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(0, 1999))
			if cc['cena'] == '2':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(2000, 3999))
			if cc['cena'] == '3':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(4000, 5999))
			if cc['cena'] == '4':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(6000, 9999))
			if cc['cena'] == '5':
				nieruchomoscs = nieruchomoscs.filter(cena__gte=(10000))
			if filtrpowdomu_form.is_valid():
				cp = filtrpowdomu_form.cleaned_data
			if cp['powierz_domu'] == '0':
				nieruchomoscs = nieruchomoscs.filter(domys__powierz_domu__range=(1, 9999))
			if cp['powierz_domu'] == '1':
				nieruchomoscs = nieruchomoscs.filter(domys__powierz_domu__range=(1, 99))
			if cp['powierz_domu'] == '2':
				nieruchomoscs = nieruchomoscs.filter(domys__powierz_domu__range=(100, 199))
			if cp['powierz_domu'] == '3':
				nieruchomoscs = nieruchomoscs.filter(domys__powierz_domu__range=(200, 299))
			if cp['powierz_domu'] == '4':
				nieruchomoscs = nieruchomoscs.filter(domys__powierz_domu__range=(300, 499))
			if cp['powierz_domu'] == '5':
				nieruchomoscs = nieruchomoscs.filter(domys__powierz_domu__range=(500, 999))
			if cp['powierz_domu'] == '6':
				nieruchomoscs = nieruchomoscs.filter(domys__powierz_domu__gte=(1000))
			if filtrpowdzial_form.is_valid():
				pd = filtrpowdzial_form.cleaned_data
			if pd['powierz_dzial'] == '0':
				nieruchomoscs = nieruchomoscs.filter(domys__powierz_dzial__range=(1, 99999))
			if pd['powierz_dzial'] == '1':
				nieruchomoscs = nieruchomoscs.filter(domys__powierz_dzial__range=(1, 199))
			if pd['powierz_dzial'] == '2':
				nieruchomoscs = nieruchomoscs.filter(domys__powierz_dzial__range=(200, 399))
			if pd['powierz_dzial'] == '3':
				nieruchomoscs = nieruchomoscs.filter(domys__powierz_dzial__range=(400, 799))
			if pd['powierz_dzial'] == '4':
				nieruchomoscs = nieruchomoscs.filter(domys__powierz_dzial__range=(800, 1199))
			if pd['powierz_dzial'] == '5':
				nieruchomoscs = nieruchomoscs.filter(domys__powierz_dzial__range=(1200, 1999))
			if pd['powierz_dzial'] == '6':
				nieruchomoscs = nieruchomoscs.filter(domys__powierz_dzial__range=(2000, 3999))
			if pd['powierz_dzial'] == '7':
				nieruchomoscs = nieruchomoscs.filter(domys__powierz_dzial__gte=(4000))
			if filtrrodzzab_form.is_valid():
				rz = filtrrodzzab_form.cleaned_data
			if rz['rodzaj_domu'] == '1':
				nieruchomoscs = nieruchomoscs.filter(domys__rodzaj_domu='wolnostojący')
			if rz['rodzaj_domu'] == '2':
				nieruchomoscs = nieruchomoscs.filter(domys__rodzaj_domu='bliźniak')
			if rz['rodzaj_domu'] == '3':
				nieruchomoscs = nieruchomoscs.filter(domys__rodzaj_domu='szeregówka')
			if rz['rodzaj_domu'] == '4':
				nieruchomoscs = nieruchomoscs.filter(domys__rodzaj_domu='kamienica')
			if rz['rodzaj_domu'] == '5':
				nieruchomoscs = nieruchomoscs.filter(domys__rodzaj_domu='dworek')
			if rz['rodzaj_domu'] == '6':
				nieruchomoscs = nieruchomoscs.filter(domys__rodzaj_domu='gospodarstwo')
						
			return render(request, 'bithouse/presentbit/domy_wy.html', {'nieruchomoscs': nieruchomoscs, 
																					'filtrmiejsc_form': filtrmiejsc_form,
																					'filtrrynk_form': filtrrynk_form,
																					'filtroferent_form': filtroferent_form,
																					'filtrinn_form': filtrinn_form,
																					'filtrcenawy_form': filtrcenawy_form,
																					'filtrpowdomu_form': filtrpowdomu_form,
																					'filtrpowdzial_form': filtrpowdzial_form,
																					'filtrrodzzab_form': filtrrodzzab_form})
																			
																			
	else:
		nieruchomoscs = Nieruchomosc.objects.filter(profil='dom', rodzaj_transakcji='wynajem')
		filtrmiejsc_form = FiltrMiejscForm()
		filtrrynk_form = FiltrRynekForm()
		filtroferent_form = FiltrOferentForm()
		filtrinn_form = FiltrIloscPokForm()
		filtrcenawy_form = FiltrCenaWynForm()
		filtrpowdomu_form = FiltrPowierzDomuForm()
		filtrpowdzial_form = FiltrPowierzDzialForm()
		filtrrodzzab_form = FiltrRodzZabForm()
					
		return render(request, 'bithouse/presentbit/domy_wy.html', {'nieruchomoscs': nieruchomoscs, 
																			'filtrmiejsc_form': filtrmiejsc_form,
																			'filtrrynk_form': filtrrynk_form,
																			'filtroferent_form': filtroferent_form,
																			'filtrinn_form': filtrinn_form,
																			'filtrcenawy_form': filtrcenawy_form,
																			'filtrpowdomu_form': filtrpowdomu_form,
																			'filtrpowdzial_form': filtrpowdzial_form,
																			'filtrrodzzab_form': filtrrodzzab_form})		
	


	
def ogloszenia_mieszkania(request, nieruchomoscs=None):
	
	if request.method == 'POST':
	
		filtrmiejsc_form = FiltrMiejscForm(request.POST)
		filtrrynk_form = FiltrRynekForm(request.POST)
		filtroferent_form = FiltrOferentForm(request.POST)
		filtrpowmie_form = FiltrPowMieForm(request.POST)
		filtrcenamiesp_form = FiltrCenaMieSprzForm(request.POST)
		filtrinn_form = FiltrIloscPokForm(request.POST)
		filtrwykonmie_form = FiltrWykonczMieForm(request.POST)
		if filtrmiejsc_form.is_valid():
			cd = filtrmiejsc_form.cleaned_data
			nieruchomoscs = Nieruchomosc.objects.filter(profil='mieszkanie', rodzaj_transakcji='sprzedaż', miejscowosc=cd['miejscowosc'])
			
			if filtrrynk_form.is_valid():
				ry = filtrrynk_form.cleaned_data
			if ry['rynek'] == '1':
				nieruchomoscs = nieruchomoscs.filter(rynek='wtórny')	
			if ry['rynek'] == '2':
				nieruchomoscs = nieruchomoscs.filter(rynek='pierwotny')
			if filtroferent_form.is_valid():
				of = filtroferent_form.cleaned_data
			if of['oferent'] == '1':
				nieruchomoscs = nieruchomoscs.filter(oferent='właściciel')
			if of['oferent'] == '2':
				nieruchomoscs = nieruchomoscs.filter(oferent='biuro pośrednictwa')
			if of['oferent'] == '3':
				nieruchomoscs = nieruchomoscs.filter(oferent='deweloper')
			if filtrpowmie_form.is_valid():
				pmi = filtrpowmie_form.cleaned_data
			if pmi['powierz_mieszkania'] == '0':
				nieruchomoscs = nieruchomoscs.filter(mieszkanias__powierz_mieszkania__range=(1, 99999))
			if pmi['powierz_mieszkania'] == '1':
				nieruchomoscs = nieruchomoscs.filter(mieszkanias__powierz_mieszkania__range=(1, 24))
			if pmi['powierz_mieszkania'] == '2':
				nieruchomoscs = nieruchomoscs.filter(mieszkanias__powierz_mieszkania__range=(25, 39))
			if pmi['powierz_mieszkania'] == '3':
				nieruchomoscs = nieruchomoscs.filter(mieszkanias__powierz_mieszkania__range=(40, 55))
			if pmi['powierz_mieszkania'] == '4':
				nieruchomoscs = nieruchomoscs.filter(mieszkanias__powierz_mieszkania__range=(56, 69))
			if pmi['powierz_mieszkania'] == '5':
				nieruchomoscs = nieruchomoscs.filter(mieszkanias__powierz_mieszkania__range=(70, 85))
			if pmi['powierz_mieszkania'] == '6':
				nieruchomoscs = nieruchomoscs.filter(mieszkanias__powierz_mieszkania__range=(86, 99))
			if pmi['powierz_mieszkania'] == '7':
				nieruchomoscs = nieruchomoscs.filter(mieszkanias__powierz_mieszkania__range=(100, 129))
			if pmi['powierz_mieszkania'] == '8':
				nieruchomoscs = nieruchomoscs.filter(mieszkanias__powierz_mieszkania__range=(130, 159))
			if pmi['powierz_mieszkania'] == '9':
				nieruchomoscs = nieruchomoscs.filter(mieszkanias__powierz_mieszkania__gte=(160))
			if filtrcenamiesp_form.is_valid():
				cms = filtrcenamiesp_form.cleaned_data
			if cms['cena'] == '0':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(0, 99999999))
			if cms['cena'] == '1':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(0, 99999))
			if cms['cena'] == '2':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(100000, 149999))
			if cms['cena'] == '3':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(150000, 199999))
			if cms['cena'] == '4':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(200000, 299999))
			if cms['cena'] == '5':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(300000, 399999))
			if cms['cena'] == '6':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(400000, 499999))
			if cms['cena'] == '7':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(500000, 699999))
			if cms['cena'] == '8':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(700000, 999999))
			if cms['cena'] == '9':
				nieruchomoscs = nieruchomoscs.filter(cena__gte=(1000000))
			if filtrinn_form.is_valid():
				cl = filtrinn_form.cleaned_data
			if cl['ilosc_pokoi'] == '0':
				nieruchomoscs = nieruchomoscs.filter(mieszkanias__ilosc_pokoi__gte=(1))
			if cl['ilosc_pokoi'] != '0':
				nieruchomoscs = nieruchomoscs.filter(mieszkanias__ilosc_pokoi=cl['ilosc_pokoi'])
			if cl['ilosc_pokoi'] == '12':
				nieruchomoscs = nieruchomoscs.filter(mieszkanias__ilosc_pokoi__gte=(12))
			if filtrwykonmie_form.is_valid():
				swm = filtrwykonmie_form.cleaned_data
			if swm['stan_wykonczenia'] == '1':
				nieruchomoscs = nieruchomoscs.filter(mieszkanias__stan_wykonczenia='do zamieszkania')
			if swm['stan_wykonczenia'] == '2':
				nieruchomoscs = nieruchomoscs.filter(mieszkanias__stan_wykonczenia='do wykończenia')
			if swm['stan_wykonczenia'] == '3':
				nieruchomoscs = nieruchomoscs.filter(mieszkanias__stan_wykonczenia='do remontu')
			if swm['stan_wykonczenia'] == '4':
				nieruchomoscs = nieruchomoscs.filter(mieszkanias__stan_wykonczenia='stan surowy zamknięty')
			if swm['stan_wykonczenia'] == '5':
				nieruchomoscs = nieruchomoscs.filter(mieszkanias__stan_wykonczenia='stan surowy otwarty')
			
						
			return render(request, 'bithouse/presentbit/mieszkania.html', {'nieruchomoscs': nieruchomoscs, 
																						'filtrmiejsc_form': filtrmiejsc_form,
																						'filtrrynk_form': filtrrynk_form,
																						'filtroferent_form': filtroferent_form,
																						'filtrpowmie_form': filtrpowmie_form,
																						'filtrcenamiesp_form': filtrcenamiesp_form,
																						'filtrinn_form': filtrinn_form,
																						'filtrwykonmie_form': filtrwykonmie_form})
			
			
	else:
		nieruchomoscs = Nieruchomosc.objects.filter(profil='mieszkanie', rodzaj_transakcji='sprzedaż')
		filtrmiejsc_form = FiltrMiejscForm()
		filtrrynk_form = FiltrRynekForm()
		filtroferent_form = FiltrOferentForm()
		filtrpowmie_form = FiltrPowMieForm()
		filtrcenamiesp_form = FiltrCenaMieSprzForm()
		filtrinn_form = FiltrIloscPokForm()
		filtrwykonmie_form = FiltrWykonczMieForm()
					
		return render(request, 'bithouse/presentbit/mieszkania.html', {'nieruchomoscs': nieruchomoscs, 
																					'filtrmiejsc_form': filtrmiejsc_form,
																					'filtrrynk_form': filtrrynk_form,
																					'filtroferent_form': filtroferent_form,
																					'filtrpowmie_form': filtrpowmie_form,
																					'filtrcenamiesp_form': filtrcenamiesp_form,
																					'filtrinn_form': filtrinn_form,
																					'filtrwykonmie_form': filtrwykonmie_form})


		
def ogloszenia_mieszkania_wy(request, nieruchomoscs=None):
	
	if request.method == 'POST':
	
		filtrmiejsc_form = FiltrMiejscForm(request.POST)
		filtrrynk_form = FiltrRynekForm(request.POST)
		filtroferent_form = FiltrOferentForm(request.POST)
		filtrpowmie_form = FiltrPowMieForm(request.POST)
		filtrinn_form = FiltrIloscPokForm(request.POST)
		filtrcenamiewy_form = FiltrCenaMieWynForm(request.POST)
		filtrmeble_form = FiltrMebleForm(request.POST)
		if filtrmiejsc_form.is_valid():
			cd = filtrmiejsc_form.cleaned_data
			nieruchomoscs = Nieruchomosc.objects.filter(profil='mieszkanie', rodzaj_transakcji='wynajem', miejscowosc=cd['miejscowosc'])
			
			if filtrrynk_form.is_valid():
				ry = filtrrynk_form.cleaned_data
			if ry['rynek'] == '1':
				nieruchomoscs = nieruchomoscs.filter(rynek='wtórny')	
			if ry['rynek'] == '2':
				nieruchomoscs = nieruchomoscs.filter(rynek='pierwotny')
			if filtroferent_form.is_valid():
				of = filtroferent_form.cleaned_data
			if of['oferent'] == '1':
				nieruchomoscs = nieruchomoscs.filter(oferent='właściciel')
			if of['oferent'] == '2':
				nieruchomoscs = nieruchomoscs.filter(oferent='biuro pośrednictwa')
			if of['oferent'] == '3':
				nieruchomoscs = nieruchomoscs.filter(oferent='deweloper')
			if filtrpowmie_form.is_valid():
				pmi = filtrpowmie_form.cleaned_data
			if pmi['powierz_mieszkania'] == '0':
				nieruchomoscs = nieruchomoscs.filter(mieszkanias__powierz_mieszkania__range=(1, 99999))
			if pmi['powierz_mieszkania'] == '1':
				nieruchomoscs = nieruchomoscs.filter(mieszkanias__powierz_mieszkania__range=(1, 24))
			if pmi['powierz_mieszkania'] == '2':
				nieruchomoscs = nieruchomoscs.filter(mieszkanias__powierz_mieszkania__range=(25, 39))
			if pmi['powierz_mieszkania'] == '3':
				nieruchomoscs = nieruchomoscs.filter(mieszkanias__powierz_mieszkania__range=(40, 55))
			if pmi['powierz_mieszkania'] == '4':
				nieruchomoscs = nieruchomoscs.filter(mieszkanias__powierz_mieszkania__range=(56, 69))
			if pmi['powierz_mieszkania'] == '5':
				nieruchomoscs = nieruchomoscs.filter(mieszkanias__powierz_mieszkania__range=(70, 85))
			if pmi['powierz_mieszkania'] == '6':
				nieruchomoscs = nieruchomoscs.filter(mieszkanias__powierz_mieszkania__range=(86, 99))
			if pmi['powierz_mieszkania'] == '7':
				nieruchomoscs = nieruchomoscs.filter(mieszkanias__powierz_mieszkania__range=(100, 129))
			if pmi['powierz_mieszkania'] == '8':
				nieruchomoscs = nieruchomoscs.filter(mieszkanias__powierz_mieszkania__range=(130, 159))
			if pmi['powierz_mieszkania'] == '9':
				nieruchomoscs = nieruchomoscs.filter(mieszkanias__powierz_mieszkania__gte=(160))
			if filtrinn_form.is_valid():
				cl = filtrinn_form.cleaned_data
			if cl['ilosc_pokoi'] == '0':
				nieruchomoscs = nieruchomoscs.filter(mieszkanias__ilosc_pokoi__gte=(1))
			if cl['ilosc_pokoi'] != '0':
				nieruchomoscs = nieruchomoscs.filter(mieszkanias__ilosc_pokoi=cl['ilosc_pokoi'])
			if cl['ilosc_pokoi'] == '12':
				nieruchomoscs = nieruchomoscs.filter(mieszkanias__ilosc_pokoi__gte=(12))
			if filtrcenamiewy_form.is_valid():
				cmw = filtrcenamiewy_form.cleaned_data
			if cmw['cena'] == '0':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(0, 99999999))
			if cmw['cena'] == '1':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(0, 999))
			if cmw['cena'] == '2':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(1000, 1499))
			if cmw['cena'] == '3':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(1500, 1999))
			if cmw['cena'] == '4':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(2000, 2999))
			if cmw['cena'] == '5':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(3000, 3999))
			if cmw['cena'] == '6':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(4000, 4999))
			if cmw['cena'] == '7':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(5000, 6999))
			if cmw['cena'] == '8':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(7000, 9999))
			if cmw['cena'] == '9':
				nieruchomoscs = nieruchomoscs.filter(cena__gte=(10000))
			if filtrmeble_form.is_valid():
				ry = filtrmeble_form.cleaned_data
			if ry['meble'] == '1':
				nieruchomoscs = nieruchomoscs.filter(mieszkanias__meble='True')	
			
			
						
			return render(request, 'bithouse/presentbit/mieszkania_wy.html', {'nieruchomoscs': nieruchomoscs, 
																							'filtrmiejsc_form': filtrmiejsc_form,
																							'filtrrynk_form': filtrrynk_form,
																							'filtroferent_form': filtroferent_form,
																							'filtrpowmie_form': filtrpowmie_form,
																							'filtrinn_form': filtrinn_form,
																							'filtrcenamiewy_form': filtrcenamiewy_form,
																							'filtrmeble_form': filtrmeble_form})
	else:
		nieruchomoscs = Nieruchomosc.objects.filter(profil='mieszkanie', rodzaj_transakcji='wynajem')
		filtrmiejsc_form = FiltrMiejscForm()
		filtrrynk_form = FiltrRynekForm()
		filtroferent_form = FiltrOferentForm()
		filtrpowmie_form = FiltrPowMieForm()
		filtrinn_form = FiltrIloscPokForm()
		filtrcenamiewy_form = FiltrCenaMieWynForm()
		filtrmeble_form = FiltrMebleForm()
					
		return render(request, 'bithouse/presentbit/mieszkania_wy.html', {'nieruchomoscs': nieruchomoscs, 
																						'filtrmiejsc_form': filtrmiejsc_form,
																						'filtrrynk_form': filtrrynk_form,
																						'filtroferent_form': filtroferent_form,
																						'filtrpowmie_form': filtrpowmie_form,
																						'filtrinn_form': filtrinn_form,
																						'filtrcenamiewy_form': filtrcenamiewy_form,
																						'filtrmeble_form': filtrmeble_form})





def ogloszenia_pokoje(request, nieruchomoscs=None):
	
	if request.method == 'POST':
	
		filtrmiejsc_form = FiltrMiejscForm(request.POST)
		filtroferent_form = FiltrOferentForm(request.POST)
		filtrpowmie_form = FiltrPowMieForm(request.POST)
		filtrinn_form = FiltrIloscPokForm(request.POST)
		filtrcenamiewy_form = FiltrCenaMieWynForm(request.POST)
		filtrmeble_form = FiltrMebleForm(request.POST)
		if filtrmiejsc_form.is_valid():
			cd = filtrmiejsc_form.cleaned_data
			nieruchomoscs = Nieruchomosc.objects.filter(profil='pokoje', rodzaj_transakcji='wynajem', miejscowosc=cd['miejscowosc'])
			
			if filtroferent_form.is_valid():
				of = filtroferent_form.cleaned_data
			if of['oferent'] == '1':
				nieruchomoscs = nieruchomoscs.filter(oferent='właściciel')
			if of['oferent'] == '2':
				nieruchomoscs = nieruchomoscs.filter(oferent='biuro pośrednictwa')
			if of['oferent'] == '3':
				nieruchomoscs = nieruchomoscs.filter(oferent='deweloper')
			if filtrpowmie_form.is_valid():
				pmi = filtrpowmie_form.cleaned_data
			if pmi['powierz_mieszkania'] == '0':
				nieruchomoscs = nieruchomoscs.filter(pokojes__powierz_mieszkania__range=(1, 99999))
			if pmi['powierz_mieszkania'] == '1':
				nieruchomoscs = nieruchomoscs.filter(pokojes__powierz_mieszkania__range=(1, 24))
			if pmi['powierz_mieszkania'] == '2':
				nieruchomoscs = nieruchomoscs.filter(pokojes__powierz_mieszkania__range=(25, 39))
			if pmi['powierz_mieszkania'] == '3':
				nieruchomoscs = nieruchomoscs.filter(pokojes__powierz_mieszkania__range=(40, 55))
			if pmi['powierz_mieszkania'] == '4':
				nieruchomoscs = nieruchomoscs.filter(pokojes__powierz_mieszkania__range=(56, 69))
			if pmi['powierz_mieszkania'] == '5':
				nieruchomoscs = nieruchomoscs.filter(pokojes__powierz_mieszkania__range=(70, 85))
			if pmi['powierz_mieszkania'] == '6':
				nieruchomoscs = nieruchomoscs.filter(pokojes__powierz_mieszkania__range=(86, 99))
			if pmi['powierz_mieszkania'] == '7':
				nieruchomoscs = nieruchomoscs.filter(pokojes__powierz_mieszkania__range=(100, 129))
			if pmi['powierz_mieszkania'] == '8':
				nieruchomoscs = nieruchomoscs.filter(pokojes__powierz_mieszkania__range=(130, 159))
			if pmi['powierz_mieszkania'] == '9':
				nieruchomoscs = nieruchomoscs.filter(pokojes__powierz_mieszkania__gte=(160))
			if filtrinn_form.is_valid():
				cl = filtrinn_form.cleaned_data
			if cl['ilosc_pokoi'] == '0':
				nieruchomoscs = nieruchomoscs.filter(pokojes__ilosc_pokoi__gte=(1))
			if cl['ilosc_pokoi'] != '0':
				nieruchomoscs = nieruchomoscs.filter(pokojes__ilosc_pokoi=cl['ilosc_pokoi'])
			if cl['ilosc_pokoi'] == '12':
				nieruchomoscs = nieruchomoscs.filter(pokojes__ilosc_pokoi__gte=(12))
			if filtrcenamiewy_form.is_valid():
				cmw = filtrcenamiewy_form.cleaned_data
			if cmw['cena'] == '0':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(0, 99999999))
			if cmw['cena'] == '1':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(0, 999))
			if cmw['cena'] == '2':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(1000, 1499))
			if cmw['cena'] == '3':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(1500, 1999))
			if cmw['cena'] == '4':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(2000, 2999))
			if cmw['cena'] == '5':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(3000, 3999))
			if cmw['cena'] == '6':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(4000, 4999))
			if cmw['cena'] == '7':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(5000, 6999))
			if cmw['cena'] == '8':
				nieruchomoscs = nieruchomoscs.filter(cena__range=(7000, 9999))
			if cmw['cena'] == '9':
				nieruchomoscs = nieruchomoscs.filter(cena__gte=(10000))
			if filtrmeble_form.is_valid():
				ry = filtrmeble_form.cleaned_data
			if ry['meble'] == '1':
				nieruchomoscs = nieruchomoscs.filter(pokojes__meble='True')	
			
			
						
			return render(request, 'bithouse/presentbit/pokoje.html', {'nieruchomoscs': nieruchomoscs, 
																							'filtrmiejsc_form': filtrmiejsc_form,
																							'filtroferent_form': filtroferent_form,
																							'filtrpowmie_form': filtrpowmie_form,
																							'filtrinn_form': filtrinn_form,
																							'filtrcenamiewy_form': filtrcenamiewy_form,
																							'filtrmeble_form': filtrmeble_form})
	else:
		nieruchomoscs = Nieruchomosc.objects.filter(profil='pokoje', rodzaj_transakcji='wynajem')
		filtrmiejsc_form = FiltrMiejscForm()
		filtroferent_form = FiltrOferentForm()
		filtrpowmie_form = FiltrPowMieForm()
		filtrinn_form = FiltrIloscPokForm()
		filtrcenamiewy_form = FiltrCenaMieWynForm()
		filtrmeble_form = FiltrMebleForm()
					
		return render(request, 'bithouse/presentbit/pokoje.html', {'nieruchomoscs': nieruchomoscs, 
																						'filtrmiejsc_form': filtrmiejsc_form,
																						'filtroferent_form': filtroferent_form,
																						'filtrpowmie_form': filtrpowmie_form,
																						'filtrinn_form': filtrinn_form,
																						'filtrcenamiewy_form': filtrcenamiewy_form,
																						'filtrmeble_form': filtrmeble_form})





def ogloszenia_garage(request, nieruchomoscs=None):
	
	if request.method == 'POST':
	
		filtrmiejsc_form = FiltrMiejscForm(request.POST)
		filtroferent_form = FiltrOferentForm(request.POST)
		
		if filtrmiejsc_form.is_valid():
			cd = filtrmiejsc_form.cleaned_data
			nieruchomoscs = Nieruchomosc.objects.filter(profil='garage', rodzaj_transakcji='sprzedaż', miejscowosc=cd['miejscowosc'])
			
			if filtroferent_form.is_valid():
				of = filtroferent_form.cleaned_data
			if of['oferent'] == '1':
				nieruchomoscs = nieruchomoscs.filter(oferent='właściciel')
			if of['oferent'] == '2':
				nieruchomoscs = nieruchomoscs.filter(oferent='biuro pośrednictwa')
			if of['oferent'] == '3':
				nieruchomoscs = nieruchomoscs.filter(oferent='deweloper')
						
			
						
			return render(request, 'bithouse/presentbit/garage.html', {'nieruchomoscs': nieruchomoscs, 
																							'filtrmiejsc_form': filtrmiejsc_form,
																							'filtroferent_form': filtroferent_form})
	else:
		nieruchomoscs = Nieruchomosc.objects.filter(profil='garage', rodzaj_transakcji='sprzedaż')
		filtrmiejsc_form = FiltrMiejscForm()
		filtroferent_form = FiltrOferentForm()
		
					
		return render(request, 'bithouse/presentbit/garage.html', {'nieruchomoscs': nieruchomoscs, 
																						'filtrmiejsc_form': filtrmiejsc_form,
																						'filtroferent_form': filtroferent_form})																						
																						
																						
																						
																						
	
def ogloszenia_komercyjne(request, nieruchomoscs=None):
	
	if request.method == 'POST':
	
		filtrmiejsc_form = FiltrMiejscForm(request.POST)
		filtrrynk_form = FiltrRynekForm(request.POST)
		filtroferent_form = FiltrOferentForm(request.POST)
		if filtrmiejsc_form.is_valid():
			cd = filtrmiejsc_form.cleaned_data
			nieruchomoscs = Nieruchomosc.objects.filter(profil='komercyjne', rodzaj_transakcji='sprzedaż', miejscowosc=cd['miejscowosc'])
			
			if filtrrynk_form.is_valid():
				ry = filtrrynk_form.cleaned_data
			if ry['rynek'] == '1':
				nieruchomoscs = nieruchomoscs.filter(rynek='wtórny')	
			if ry['rynek'] == '2':
				nieruchomoscs = nieruchomoscs.filter(rynek='pierwotny')
			if filtroferent_form.is_valid():
				of = filtroferent_form.cleaned_data
			if of['oferent'] == '1':
				nieruchomoscs = nieruchomoscs.filter(oferent='właściciel')
			if of['oferent'] == '2':
				nieruchomoscs = nieruchomoscs.filter(oferent='biuro pośrednictwa')
			if of['oferent'] == '3':
				nieruchomoscs = nieruchomoscs.filter(oferent='deweloper')
						
			return render(request, 'bithouse/presentbit/komercyjne.html', {'nieruchomoscs': nieruchomoscs, 
																						'filtrmiejsc_form': filtrmiejsc_form,
																						'filtrrynk_form': filtrrynk_form,
																						'filtroferent_form': filtroferent_form})
	else:
		nieruchomoscs = Nieruchomosc.objects.filter(profil='komercyjne', rodzaj_transakcji='sprzedaż')
		filtrmiejsc_form = FiltrMiejscForm()
		filtrrynk_form = FiltrRynekForm()
		filtroferent_form = FiltrOferentForm()
					
		return render(request, 'bithouse/presentbit/komercyjne.html', {'nieruchomoscs': nieruchomoscs, 
																					'filtrmiejsc_form': filtrmiejsc_form,
																					'filtrrynk_form': filtrrynk_form,
																					'filtroferent_form': filtroferent_form})



def ogloszenia_komercyjne_wy(request, nieruchomoscs=None):
	
	if request.method == 'POST':
	
		filtrmiejsc_form = FiltrMiejscForm(request.POST)
		filtrrynk_form = FiltrRynekForm(request.POST)
		filtroferent_form = FiltrOferentForm(request.POST)
		if filtrmiejsc_form.is_valid():
			cd = filtrmiejsc_form.cleaned_data
			nieruchomoscs = Nieruchomosc.objects.filter(profil='komercyjne', rodzaj_transakcji='wynajem', miejscowosc=cd['miejscowosc'])
			
			if filtrrynk_form.is_valid():
				ry = filtrrynk_form.cleaned_data
			if ry['rynek'] == '1':
				nieruchomoscs = nieruchomoscs.filter(rynek='wtórny')	
			if ry['rynek'] == '2':
				nieruchomoscs = nieruchomoscs.filter(rynek='pierwotny')
			if filtroferent_form.is_valid():
				of = filtroferent_form.cleaned_data
			if of['oferent'] == '1':
				nieruchomoscs = nieruchomoscs.filter(oferent='właściciel')
			if of['oferent'] == '2':
				nieruchomoscs = nieruchomoscs.filter(oferent='biuro pośrednictwa')
			if of['oferent'] == '3':
				nieruchomoscs = nieruchomoscs.filter(oferent='deweloper')
						
			return render(request, 'bithouse/presentbit/komercyjne_wy.html', {'nieruchomoscs': nieruchomoscs, 
																							'filtrmiejsc_form': filtrmiejsc_form,
																							'filtrrynk_form': filtrrynk_form,
																							'filtroferent_form': filtroferent_form})
																							
	else:
		nieruchomoscs = Nieruchomosc.objects.filter(profil='komercyjne', rodzaj_transakcji='wynajem')
		filtrmiejsc_form = FiltrMiejscForm()
		filtrrynk_form = FiltrRynekForm()
		filtroferent_form = FiltrOferentForm()
					
		return render(request, 'bithouse/presentbit/komercyjne_wy.html', {'nieruchomoscs': nieruchomoscs, 
																						'filtrmiejsc_form': filtrmiejsc_form,
																						'filtrrynk_form': filtrrynk_form,
																						'filtroferent_form': filtroferent_form})		
		


		
def ogloszenia_powierzch(request, nieruchomoscs=None):
	
	nieruchomoscs = Nieruchomosc.objects.filter(profil='powierzchnie')
	
					
	return render(request, 'bithouse/presentbit/komercyjne.html', {'nieruchomoscs': nieruchomoscs})	
	
	
	

def ogloszenia_deweloper(request, nieruchomoscs=None):
	
	if request.method == 'POST':
	
		filtrmiejsc_form = FiltrMiejscForm(request.POST)
		
		if filtrmiejsc_form.is_valid():
			cd = filtrmiejsc_form.cleaned_data
			nieruchomoscs = Nieruchomosc.objects.filter(profil='mieszkanie', oferent='deweloper', rodzaj_transakcji='sprzedaż', miejscowosc=cd['miejscowosc'])
						
			return render(request, 'bithouse/presentbit/deweloper.html', {'nieruchomoscs': nieruchomoscs, 'filtrmiejsc_form': filtrmiejsc_form})
	else:
		nieruchomoscs = Nieruchomosc.objects.filter(profil='mieszkanie', oferent='deweloper', rodzaj_transakcji='sprzedaż')
		filtrmiejsc_form = FiltrMiejscForm()
		
					
		return render(request, 'bithouse/presentbit/deweloper.html', {'nieruchomoscs': nieruchomoscs, 'filtrmiejsc_form': filtrmiejsc_form})	
	

def ogloszenia_deweloper_dom(request, nieruchomoscs=None):
	
	if request.method == 'POST':
	
		filtrmiejsc_form = FiltrMiejscForm(request.POST)
		filtroferent_form = FiltrOferentForm(request.POST)
		if filtrmiejsc_form.is_valid():
			cd = filtrmiejsc_form.cleaned_data
			nieruchomoscs = Nieruchomosc.objects.filter(profil='deweloper', rodzaj_transakcji='wynajem', miejscowosc=cd['miejscowosc'])
						
			return render(request, 'bithouse/presentbit/deweloper.html', {'nieruchomoscs': nieruchomoscs, 'filtrmiejsc_form': filtrmiejsc_form})
	else:
		nieruchomoscs = Nieruchomosc.objects.filter(profil='deweloper', rodzaj_transakcji='wynajem')
		filtrmiejsc_form = FiltrMiejscForm(request.POST)
		
					
		return render(request, 'bithouse/presentbit/deweloper.html', {'nieruchomoscs': nieruchomoscs, 'filtrmiejsc_form': filtrmiejsc_form})	
		
		
		
	
def detail_dzi(request, id):
	
	nieruchomosc = get_object_or_404(Nieruchomosc, id=id)
	imageitems = ImageItem.objects.filter(nieruchomosc=nieruchomosc)
	
	return render(request, 'bithouse/presentbit/detail_dzi.html', {'nieruchomosc': nieruchomosc, 'imageitems': imageitems})


def detail_dom(request, id):
	
	nieruchomosc = get_object_or_404(Nieruchomosc, id=id)
	imageitems = ImageItem.objects.filter(nieruchomosc=nieruchomosc)
	
	return render(request, 'bithouse/presentbit/detail_dom.html', {'nieruchomosc': nieruchomosc, 'imageitems': imageitems})
	

def detail_dom_wy(request, id):
	
	nieruchomosc = get_object_or_404(Nieruchomosc, id=id)
	imageitems = ImageItem.objects.filter(nieruchomosc=nieruchomosc)
	
	return render(request, 'bithouse/presentbit/detail_dom_wy.html', {'nieruchomosc': nieruchomosc, 'imageitems': imageitems})

	
	
def detail_mie(request, id):
	
	nieruchomosc = get_object_or_404(Nieruchomosc, id=id)
	imageitems = ImageItem.objects.filter(nieruchomosc=nieruchomosc)
	
	return render(request, 'bithouse/presentbit/detail_mie.html', {'nieruchomosc': nieruchomosc, 'imageitems': imageitems})

	

def detail_mie_wy(request, id):
	
	nieruchomosc = get_object_or_404(Nieruchomosc, id=id)
	imageitems = ImageItem.objects.filter(nieruchomosc=nieruchomosc)
	
	return render(request, 'bithouse/presentbit/detail_mie_wy.html', {'nieruchomosc': nieruchomosc, 'imageitems': imageitems})
	

	
def detail_kom(request, id):
	
	nieruchomosc = get_object_or_404(Nieruchomosc, id=id)
	imageitems = ImageItem.objects.filter(nieruchomosc=nieruchomosc)
	
	return render(request, 'bithouse/presentbit/detail_kom.html', {'nieruchomosc': nieruchomosc, 'imageitems': imageitems})



def detail_kom_wy(request, id):
	
	nieruchomosc = get_object_or_404(Nieruchomosc, id=id)
	imageitems = ImageItem.objects.filter(nieruchomosc=nieruchomosc)
	
	return render(request, 'bithouse/presentbit/detail_kom_wy.html', {'nieruchomosc': nieruchomosc, 'imageitems': imageitems})	
	
	
def detail_dew(request, id):
	
	nieruchomosc = get_object_or_404(Nieruchomosc, id=id)
	imageitems = ImageItem.objects.filter(nieruchomosc=nieruchomosc)
	
	return render(request, 'bithouse/presentbit/detail_dew.html', {'nieruchomosc': nieruchomosc, 'imageitems': imageitems})
	
	

def detail_pow(request, id):
	
	nieruchomosc = get_object_or_404(Nieruchomosc, id=id)
	imageitems = ImageItem.objects.filter(nieruchomosc=nieruchomosc)
	
	return render(request, 'bithouse/presentbit/detail_pow.html', {'nieruchomosc': nieruchomosc, 'imageitems': imageitems})

	
