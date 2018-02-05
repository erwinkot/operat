from django import forms
from django.contrib.auth.models import User
from realestate.models import Nieruchomosc
from realestate.models import Miejscowosc
from realestate.models import Domy


class FiltrMiejscForm(forms.ModelForm):
	
	class Meta:
		model = Nieruchomosc
		fields = ('miejscowosc',)
		

class FiltrRynekForm(forms.Form):
	RYNEK_CHOICES = (('1', 'wtórny'), 
						('2', 'pierwotny'))
	rynek = forms.ChoiceField(choices=RYNEK_CHOICES, label='Rynek')
		
		

class FiltrOferentForm(forms.Form):
	OFERENT_CHOICES = (('1', 'właściciel'), 
						('2', 'biuro pośrednictwa'),
						('3', 'deweloper'))
						
	oferent = forms.ChoiceField(choices=OFERENT_CHOICES, label='Oferujący')
	
	
		

class FiltrIloscPokForm(forms.Form):
	
	POKOJE_CHOICES = (('0', '-------------'), 
						('1', '1'), 
						('2', '2'), 
						('3', '3'), 
						('4', '4'), 
						('5', '5'), 
						('6', '6'), 
						('7', '7'), 
						('8', '8'), 
						('9', '9'), 
						('10', '10'), 
						('11', '11'),
						('12', 'powyżej 11'))
	ilosc_pokoi = forms.ChoiceField(choices=POKOJE_CHOICES, label='ilość pokoi')
	
	
	
class FiltrCenaForm(forms.Form):
	
	CENA_CHOICES = (('0', '-------------'),
					('1', 'poniżej 250 000'),
					('2', '250 000 - 499 000'),
					('3', '500 000 - 999 000'), 
					('4', '1 000 000 - 1 999 000'), 
					('5', 'powyżej 2 000 000'))
	cena = forms.ChoiceField(initial=0, choices=CENA_CHOICES, label='cena')
		
		
	
	
class FiltrPowierzDomuForm(forms.Form):
	
	POWIERZ_DOMU_CHOICES = (('0', '-------------'),
							('1', 'poniżej 100'), 
							('2', '100 - 199'), 
							('3', '200 - 299'), 
							('4', '300 - 499'),
							('5', '500 - 999'),
							('6', 'powyżej 1 000'))
	powierz_domu = forms.ChoiceField(initial=0, choices=POWIERZ_DOMU_CHOICES, label='powierzchnia domu')
	

	
class FiltrPowierzDzialForm(forms.Form):
	
	POWIERZ_DZIALKI_CHOICES = (('0', '-------------'),
							('1', 'poniżej 200'), 
							('2', '200 - 399'), 
							('3', '400 - 799'), 
							('4', '800 - 1 199'),
							('5', '1 200 - 1 999'),
							('6', '2 000 - 3 999'),
							('7', 'powyżej 4 000'))
	powierz_dzial = forms.ChoiceField(initial=0, choices=POWIERZ_DZIALKI_CHOICES, label='powierzchnia działki')	
	
	
class FiltrRodzZabForm(forms.Form):
	
	RODZAJ_ZABUD_CHOICES = (('0', '-------------'),
							('1', 'wolnostojący'), 
							('2', 'bliźniak'), 
							('3', 'szeregówka'), 
							('4', 'kamienica'),
							('5', 'dworek/pałacyk'),
							('6', 'gospodarstwo'))
							
	rodzaj_domu = forms.ChoiceField(initial=0, choices=RODZAJ_ZABUD_CHOICES, label='rodzaj zabudowy')	



class FiltrCenaWynForm(forms.Form):
	
	CENA_CHOICES = (('0', '-------------'),
					('1', 'poniżej 2 000'), 
					('2', '2 000 - 3 999'), 
					('3', '4 000 - 5 999'), 
					('4', '6 000 - 9 999'),
					('5', 'powyżej 10 000'))
	cena = forms.ChoiceField(initial=0, choices=CENA_CHOICES, label='cena wynajmu')
	
	
class FiltrPrzezDzialForm(forms.Form):
	
	PRZEZN_DZIAL_CHOICES = (('0', '-------------'),
							('1', 'mieszkaniowe jednorodzinne'), 
							('2', 'mieszkaniowe wielorodzinne'), 
							('3', 'mieszkaniowe wysokie'), 
							('4', 'przemysłowe'),
							('5', 'usługi i handel'),
							('6', 'hotelowe'),
							('7', 'medyczne'),
							('8', 'pozostałe'))
							
	przeznaczenie_dzial = forms.ChoiceField(initial=0, choices=PRZEZN_DZIAL_CHOICES, label='przeznaczenie działki')		



class FiltrTypDzialkiForm(forms.Form):
	
	TYP_DZIALKI_CHOICES = (('0', '-------------'),
							('1', 'budowlana'), 
							('2', 'rolna'), 
							('3', 'rekreacyjna'),
							('4', 'inwestycyjna'),
							('5', 'leśna'),
							('6', 'siedliskowa'))
							
	typ_dzialki = forms.ChoiceField(initial=0, choices=TYP_DZIALKI_CHOICES, label='typ działki')

	
	
class FiltrPowMieForm(forms.Form):

	POWIERZ_MIESZK_CHOICES = (('0', '-------------'),
							('1', 'poniżej 25'), 
							('2', '25 - 39'), 
							('3', '40 - 55'), 
							('4', '56 - 69'),
							('5', '70 - 85'),
							('6', '86 - 99'),
							('7', '100 - 129'),
							('8', '130 - 159'),
							('9', 'powyżej 160'))
	powierz_mieszkania = forms.ChoiceField(initial=0, choices=POWIERZ_MIESZK_CHOICES, label='powierzchnia mieszkania')
	
	

class FiltrCenaMieSprzForm(forms.Form):

	CENA_MIESZK_SPRZ_CHOICES = (('0', '-------------'),
							('1', 'poniżej 100 000'), 
							('2', '100 000 - 149 999'), 
							('3', '150 000 - 199 999'), 
							('4', '200 000 - 299 999'),
							('5', '300 000 - 399 999'),
							('6', '400 000 - 499 999'),
							('7', '500 000 - 699 999'),
							('8', '700 000 - 999 999'),
							('9', 'powyżej 1 000 000'))
	cena = forms.ChoiceField(initial=0, choices=CENA_MIESZK_SPRZ_CHOICES, label='cena sprzedaży')
		
		
	
	
class FiltrCenaMieWynForm(forms.Form):

	CENA_MIESZK_WYN_CHOICES = (('0', '-------------'),
							('1', 'poniżej 1 000'), 
							('2', '1 000 - 1 499'), 
							('3', '1 500 - 1 999'), 
							('4', '2 000 - 2 999'),
							('5', '3 000 - 3 999'),
							('6', '4 000 - 4 999'),
							('7', '5 000 - 6 999'),
							('8', '7 000 - 9 999'),
							('9', 'powyżej 10 000'))
	cena = forms.ChoiceField(initial=0, choices=CENA_MIESZK_WYN_CHOICES, label='cena wynajmu')
	
	
	
class FiltrRodzZabMieForm(forms.Form):
	
	RODZ_ZABUD_CHOICES = (('0', '-------------'),
							('1', 'dom'), 
							('2', 'bliźniak'), 
							('3', 'szeregówka'), 
							('4', 'kamienica'),
							('5', 'blok'),
							('6', 'apartamentowiec'),
							('7', 'loft'))
													
	rodzaj_zabud = forms.ChoiceField(initial=0, choices=RODZ_ZABUD_CHOICES, label='rodzaj budynku')	


class FiltrRodzMieForm(forms.Form):

	RODZ_MIESZ_CHOICES = (('0', '-------------'),
							('1', 'jednopoziomowe'), 
							('2', 'dwupoziomowe'), 
							('3', 'poddasze'), 
							('4', 'loft'))
							
							
	rodzaj_mieszkania = forms.ChoiceField(initial=0, choices=RODZ_MIESZ_CHOICES, label='rodzaj mieszkania')	
	
	


class FiltrWykonczMieForm(forms.Form):

	WYKONCZ_MIESZ_CHOICES = (('0', '-------------'),
							('1', 'do zamieszkania'), 
							('2', 'do wykończenia'), 
							('3', 'do remontu'), 
							('4', 'stan surowy zamknięty'),
							('5', 'stan surowy otwarty'))
							
							
	stan_wykonczenia = forms.ChoiceField(initial=0, choices=WYKONCZ_MIESZ_CHOICES, label='stan wykończenia')
	
	
	
class FiltrMebleForm(forms.Form):

	MEBLE_CHOICES = (('0', '-------------'),
							('1', 'umeblowane'))
							
							
							
	meble = forms.ChoiceField(initial=0, choices=MEBLE_CHOICES, label='umeblowanie')
