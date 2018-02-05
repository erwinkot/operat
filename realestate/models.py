from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.text import slugify



class Wojewodztwo(models.Model):					
	nazwa = models.CharField(max_length=150)
	slug = models.SlugField(max_length=150, blank=True)
	wojewoda = models.CharField(max_length=50, blank=True)
						
	class Meta:
		ordering = ('nazwa',)
	
	def __str__(self):
			return self.nazwa	
			
			
class Powiat(models.Model):					
	nazwa = models.CharField(max_length=150)
	slug = models.SlugField(max_length=150, blank=True)
	starosta = models.CharField(max_length=50, blank=True)
	wojewodztwo = models.ForeignKey(Wojewodztwo, related_name='powiatos')
						
	class Meta:
		ordering = ('nazwa',)
	
	def __str__(self):
			return self.nazwa


class Gmina(models.Model):					
	nazwa = models.CharField(max_length=150)
	slug = models.SlugField(max_length=150, blank=True)
	wojt = models.CharField(max_length=50, blank=True)
	powiat = models.ForeignKey(Powiat, related_name='gminas')
						
	class Meta:
		ordering = ('nazwa',)
	
	def __str__(self):
			return self.nazwa			
			
class Miejscowosc(models.Model):
	MIASTO_CHOICES = (('miasto', 'Miasto'), ('wieś', 'Wieś'))
	nazwa = models.CharField(max_length=150)
	slug = models.SlugField(max_length=150, blank=True)
	profil = models.CharField(max_length=30, choices=MIASTO_CHOICES, default='miasto')
	gmina = models.ForeignKey(Gmina, related_name='miejscowosci')
	
	class Meta:
		ordering = ('nazwa',)
	
	def __str__(self):
			return self.nazwa
			
			
class Dzielnica(models.Model):
	nazwa = models.CharField(max_length=150)
	slug = models.SlugField(max_length=150, blank=True)
	miejscowosc = models.ForeignKey(Miejscowosc, related_name='dzielnicas')
	
	class Meta:
		ordering = ('nazwa',)
	
	def __str__(self):
			return self.nazwa

			
		
class Profilefirm(models.Model):
	PROFILE_CHOICES = (('firma', 'Firma'), ('pośrednik', 'Pośrednik nieruchomości'))
	RODZAJ_CHOICES = (('deweloper', 'Deweloper'), ('pośrednik', 'Pośrednictwo nieruchomości'), ('właściciel', 'Właściciel nieruchomości'))
	nazwa = models.CharField(max_length=250)
	adres_firmy = models.CharField(max_length=60)
	kod_pocztowy = models.CharField(max_length=6)
	miejscowosc = models.ForeignKey(Miejscowosc, related_name='profilefirmos', blank=True, default=1)
	nip = models.CharField(max_length=10)
	nr_ewid = models.CharField(max_length=10, blank=True)
	regon = models.CharField(max_length=10, blank=True)
	profil = models.CharField(max_length=30, choices=PROFILE_CHOICES, default='firma')
	rodzaj_firmy = models.CharField(max_length=30, choices=RODZAJ_CHOICES, default='właściciel')
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	
	
	class Meta:
		ordering = ('nazwa',)
	
	def __str__(self):
			return self.nazwa
			
	def get_absolute_url(self):
		return reverse('realestate:profilefirm_detail', 
						args=[self.nip])

						
						
class Nieruchomosc(models.Model):
	RODZAJ_CHOICES = (('sprzedaż', 'sprzedaż'), ('wynajem', 'wynajem'))
	RYNEK_CHOICES = (('pierwotny', 'pierwotny'), ('wtórny', 'wtórny'))
	KLIENT_CHOICES = (('dowolny', 'dowolny'), 
						('osoba fizyczna', 'osoba fizyczna'), 
						('firma', 'firma'), 
						('biuro pośrednictwa', 'biuro pośrednictwa'), 
						('student', 'student'), 
						('inwestor', 'inwestor'))
	OFERENT_CHOICES = (('właściciel', 'właściciel'), ('biuro pośrednictwa', 'biuro pośrednictwa'), ('deweloper', 'deweloper'))
	STATUS_CHOICES = (('draft', 'Roboczy'), ('published', 'Opublikowana'))
	OFERTA_CHOICES = (('publiczna', 'publiczna'), ('bithouse', 'Bithouse'))
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='nieruchomosci', blank=True)
	profil = models.CharField(max_length=25, blank=True)
	nazwa_opis = models.CharField(max_length=250)
	rodzaj_transakcji = models.CharField(max_length=20, choices=RODZAJ_CHOICES, default='sprzedaż')
	ulica = models.CharField(max_length=60, blank=True)
	numer = models.CharField(max_length=10, blank=True)
	kod_pocztowy = models.CharField(max_length=6, blank=True)
	miejscowosc = models.ForeignKey(Miejscowosc, related_name='nieruchomosci', default=1)
	dzielnica = models.ForeignKey(Dzielnica, related_name='nieruchomosci', default=1)
	image = models.ImageField(upload_to='images/%y/%m/%d', blank=True)
	rynek = models.CharField(max_length=12, choices=RYNEK_CHOICES, default='wtórny')
	oferent = models.CharField(max_length=30, choices=OFERENT_CHOICES, default='właściciel')
	status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='draft')
	klient_docelowy = models.CharField(max_length=30, choices=KLIENT_CHOICES, default='dowolny')
	opis_nieruchomosci = models.TextField(blank=True)
	telefon = models.CharField(max_length=20, blank=True)
	email = models.EmailField(blank=True)
	cena = models.DecimalField(max_digits=12, decimal_places=0, blank=True, default=0)
	cenamq = models.DecimalField(max_digits=12, decimal_places=0, blank=True, default=0)
	link1 = models.URLField(max_length=200, blank=True)
	link2 = models.URLField(max_length=200, blank=True)
	link3 = models.URLField(max_length=200, blank=True)
	link4 = models.URLField(max_length=200, blank=True)
	rodzaj_oferty = models.CharField(max_length=30, choices=OFERTA_CHOICES, default='publiczna')
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	edytowalna = models.BooleanField(default=False)
	
	
		
	class Meta:
		ordering = ('-publish',)
	
	def __str__(self):
			return self.nazwa_opis
			
	
			
	def get_absolute_url(self):
		return reverse('realestate:nieruchomosc_detail', 
						args=[self.id])
	
		
			

class Nieruchomstaff(models.Model):
	nieruchomosc = models.OneToOneField(Nieruchomosc, related_name='linkusik')
	stok = models.PositiveIntegerField(blank=True, default=0)
	akcept = models.BooleanField(default=False)
	active = models.BooleanField(default=True)
	paid = models.BooleanField(default=False)
	updatedpaid = models.CharField(max_length=20)
	
	class Meta:
		ordering = ('updatedpaid',)
		
		
		


class Dzialki(models.Model):
	NIERUCH_CHOICES = (('budowlana', 'Działka budowlana'), 
						('rolna', 'Działka rolna'), 
						('rekreacyjna', 'Działka rekreacyjna'),
						('inwestycyjna', 'Działka inwestycyjna'),
						('leśna', 'Działka leśna'),
						('siedliskowa', 'Działka siedliskowa'))
	STATUS_CHOICES = (('własność', 'własność'), ('dzierżawa wieczysta', 'dzierżawa wieczysta'))
	PRZEZNA_CHOICES = (('jednorodzinne', 'mieszkaniowe jednorodzinne'), 
						('wielorodzinne', 'mieszkaniowe wielorodzinne'), 
						('wysokie', 'mieszkaniowe wysokie'),
						('przemysłowe', 'przemysłowe'), 
						('usługi i handel', 'usługi i handel'),
						('hotelowe', 'hotelowe'), 
						('medyczne', 'medyczne'), 
						('pozostałe', 'pozostałe'))
	DOJAZD_CHOICES = (('asfalt', 'asfalt'), ('utwardzony', 'utwardzony'), ('nieutwardzony', 'nieutwardzony'))					
	nieruchomosc = models.OneToOneField(Nieruchomosc, related_name='dzialki')
	typ_dzialki = models.CharField(max_length=30, choices=NIERUCH_CHOICES, default='budowlana')
	powi_dzialki = models.DecimalField(max_digits=12, decimal_places=0, default=0)
	status_dzial = models.CharField(max_length=30, choices=STATUS_CHOICES, default='wlasność')
	przeznaczenie_dzial = models.CharField(max_length=30, choices=PRZEZNA_CHOICES, default='wielorodzinne')
	info_mpzp = models.TextField(blank=True)
	dojazd = models.CharField(max_length=30, choices=DOJAZD_CHOICES, blank=True)
	prad = models.BooleanField(default=False)
	gaz = models.BooleanField(default=False)
	woda = models.BooleanField(default=False)
	kanalizacja = models.BooleanField(default=False)
	szambo = models.BooleanField(default=False)
	oczyszczalnia = models.BooleanField(default=False)
	telefon = models.BooleanField(default=False)
	las = models.BooleanField(default=False)
	gory = models.BooleanField(default=False)
	jezioro = models.BooleanField(default=False)
	morze = models.BooleanField(default=False)
	teren_otwarty = models.BooleanField(default=False)
	
	class Meta:
		ordering = ('nieruchomosc',)
			

class Domy(models.Model):
	NIERUCH_CHOICES = (('wolnostojący', 'wolnostojący'),
						('bliźniak', 'bliźniak'),
						('szeregówka', 'szeregówka'),
						('kamienica', 'kamienica'),
						('dworek', 'dworek/pałacyk'),
						('gospodarstwo', 'gospodarstwo rolne'))
	STATUS_CHOICES = (('własność', 'własność'), ('dzierżawa wieczysta', 'dzierżawa wieczysta'))
	MATERIAL_CHOICES = (('cegła', 'cegła'),
						('silikat', 'silikat'), 
						('beton komórkowy', 'beton komórkowy'), 
						('pustak', 'pustak'), 
						('silikat', 'silikat'), 
						('keramzyt', 'keramzyt'), 
						('wielka płyta', 'wielka płyta'), 
						('beton', 'beton'), 
						('drewno', 'drewno'), 
						('inne', 'inne'))
	DACH_CHOICES = (('płaski', 'płaski'), ('skośny', 'skośny'))
	POKRYCIE_CHOICES = (('dachówka ceramiczna', 'dachówka ceramiczna'),
						('blachodachówka', 'blachodachówka'), 
						('dachówka inna', 'dachówka inna'), 
						('eternit', 'eternit'), 
						('papa', 'papa'), 
						('gont', 'gont'), 
						('łupek', 'łupek'), 
						('strzecha', 'strzecha'), 
						('inne', 'inne'))
	WYKONCZENIE_CHOICES = (('do zamieszkania', 'do zamieszkania'),
						('do wykończenia', 'do wykończenia'), 
						('do remontu', 'do remontu'), 
						('stan surowy zamknięty', 'stan surowy zamknięty'), 
						('stan surowy otwarty', 'stan surowy otwarty'), 
						('inne', 'inne'))
	OKNA_CHOICES = (('drewniane', 'drewniane'),
						('plastikowe', 'plastikowe'), 
						('aluminiowe', 'aluminiowe')) 
	DOJAZD_CHOICES = (('asfalt', 'asfalt'), ('utwardzony', 'utwardzony'), ('nieutwardzony', 'nieutwardzony'))
	OGRODZENIE_CHOICES = (('drewniane', 'drewniane'),
						('metalowe', 'metalowe'), 
						('betonowe', 'betonowe'),
						('murowane', 'murowane'), 
						('siatka', 'siatka'), 
						('żywopłot', 'żywopłot'), 
						('inne', 'inne')) 						
	nieruchomosc = models.OneToOneField(Nieruchomosc, related_name='domys')
	powierz_domu = models.DecimalField(max_digits=12, decimal_places=0, blank=True, default=0)
	powierz_dzial = models.DecimalField(max_digits=12, decimal_places=0, blank=True, default=0)
	status_dzial = models.CharField(max_length=30, choices=STATUS_CHOICES, default='własność')
	rodzaj_domu = models.CharField(max_length=30, choices=NIERUCH_CHOICES, blank=True)
	rok_budowy = models.CharField(max_length=4, blank=True)
	czynsz = models.DecimalField(max_digits=12, decimal_places=0, blank=True, default=0)
	kaucja = models.DecimalField(max_digits=12, decimal_places=0, blank=True, default=0)
	dostepne = models.CharField(max_length=30, blank=True)
	rodz_materialu = models.CharField(max_length=30, choices=MATERIAL_CHOICES, blank=True)
	dach = models.CharField(max_length=30, choices=DACH_CHOICES, blank=True)
	pokrycie_dach = models.CharField(max_length=30, choices=POKRYCIE_CHOICES, blank=True)
	stan_wykonczenia = models.CharField(max_length=30, choices=WYKONCZENIE_CHOICES, blank=True)
	okna = models.CharField(max_length=30, choices=OKNA_CHOICES, blank=True)
	ilosc_kond = models.PositiveIntegerField(default=0)
	ilosc_pokoi = models.PositiveIntegerField(default=0)
	ilosc_lazen = models.PositiveIntegerField(default=0)
	ilosc_kuchni = models.PositiveIntegerField(default=0)
	piwnice = models.BooleanField(default=False)
	garaz = models.BooleanField(default=False)
	poddasze = models.BooleanField(default=False)
	basen = models.BooleanField(default=False)
	klimatyzacja = models.BooleanField(default=False)
	prad = models.BooleanField(default=False)
	gaz = models.BooleanField(default=False)
	woda = models.BooleanField(default=False)
	kanalizacja = models.BooleanField(default=False)
	szambo = models.BooleanField(default=False)
	oczyszczalnia = models.BooleanField(default=False)
	telefon = models.BooleanField(default=False)
	internet = models.BooleanField(default=False)
	tel_kablowa = models.BooleanField(default=False)
	miejskie = models.BooleanField(default=False)
	gazowe = models.BooleanField(default=False)
	olejowe = models.BooleanField(default=False)
	elektryczne = models.BooleanField(default=False)
	weglowe = models.BooleanField(default=False)
	piece_kaflowe = models.BooleanField(default=False)
	kominkowe = models.BooleanField(default=False)
	kolektor_sloneczny = models.BooleanField(default=False)
	pompa_ciepla = models.BooleanField(default=False)
	biomasa = models.BooleanField(default=False)
	ogrodzenie = models.CharField(max_length=30, choices=OGRODZENIE_CHOICES, blank=True)
	dojazd = models.CharField(max_length=30, choices=DOJAZD_CHOICES, blank=True)
	teren_zamkniety = models.BooleanField(default=False)
	monitoring = models.BooleanField(default=False)
	alarm = models.BooleanField(default=False)
	drzwi_anty = models.BooleanField(default=False)
	rolety = models.BooleanField(default=False)
	domofon = models.BooleanField(default=False)
	las = models.BooleanField(default=False)
	gory = models.BooleanField(default=False)
	jezioro = models.BooleanField(default=False)
	morze = models.BooleanField(default=False)
	teren_otwarty = models.BooleanField(default=False)
	meble = models.BooleanField(default=False)
	meble_czesc = models.BooleanField(default=False)
	kuchenka = models.BooleanField(default=False)
	pralka = models.BooleanField(default=False)
	lodowka = models.BooleanField(default=False)
	zmywarka = models.BooleanField(default=False)
	piekarnik = models.BooleanField(default=False)
	mikrofala = models.BooleanField(default=False)
	telewizor = models.BooleanField(default=False)
	

	class Meta:
		ordering = ('nieruchomosc',)
	
class Mieszkania(models.Model):
	NIERUCH_CHOICES = (('wolnostojący', 'wolnostojący'),
						('bliźniak', 'bliźniak'),
						('szeregówka', 'szeregówka'),
						('kamienica', 'kamienica'),
						('blok', 'blok'),
						('apartamentowiec', 'apartamentowiec'),
						('loft', 'loft'))
	MATERIAL_CHOICES = (('cegła', 'cegła'),
						('silikat', 'silikat'), 
						('beton komórkowy', 'beton komórkowy'), 
						('pustak', 'pustak'), 
						('silikat', 'silikat'), 
						('keramzyt', 'keramzyt'), 
						('wielka płyta', 'wielka płyta'), 
						('beton', 'beton'), 
						('drewno', 'drewno'), 
						('inne', 'inne'))
	RODZAJ_CHOICES = (('jednopoziomowe', 'jednopoziomowe'), 
						('dwupoziomowe', 'dwupoziomowe'), 
						('poddasze', 'poddasze'), 
						('loft', 'loft'))
	WYKONCZENIE_CHOICES = (('do zamieszkania', 'do zamieszkania'),
						('do wykończenia', 'do wykończenia'), 
						('do remontu', 'do remontu'), 
						('stan surowy zamknięty', 'stan surowy zamknięty'), 
						('stan surowy otwarty', 'stan surowy otwarty'), 
						('inne', 'inne'))
	OKNA_CHOICES = (('drewniane', 'drewniane'),
						('plastikowe', 'plastikowe'), 
						('aluminiowe', 'aluminiowe')) 
	DOJAZD_CHOICES = (('asfalt', 'asfalt'), ('utwardzony', 'utwardzony'), ('nieutwardzony', 'nieutwardzony'))
	nieruchomosc = models.OneToOneField(Nieruchomosc, related_name='mieszkanias')
	powierz_mieszkania = models.DecimalField(max_digits=12, decimal_places=0, blank=True, default=0)
	rodzaj_zabud = models.CharField(max_length=30, choices=NIERUCH_CHOICES, blank=True)
	rodzaj_mieszkania = models.CharField(max_length=30, choices=RODZAJ_CHOICES, default='jednopoziomowe')
	pietro = models.CharField(max_length=3)
	rok_budowy = models.CharField(max_length=4, blank=True)
	czynsz = models.DecimalField(max_digits=12, decimal_places=0, blank=True, default=0)
	kaucja = models.DecimalField(max_digits=12, decimal_places=0, blank=True, default=0)
	dostepne = models.CharField(max_length=30, blank=True)
	rodz_materialu = models.CharField(max_length=30, choices=MATERIAL_CHOICES, blank=True)
	stan_wykonczenia = models.CharField(max_length=30, choices=WYKONCZENIE_CHOICES, blank=True)
	okna = models.CharField(max_length=30, choices=OKNA_CHOICES, blank=True)
	ilosc_kond = models.PositiveIntegerField(default=0)
	ilosc_pokoi = models.PositiveIntegerField(default=0)
	ilosc_lazen = models.PositiveIntegerField(default=0)
	ilosc_kuchni = models.PositiveIntegerField(default=0)
	winda = models.BooleanField(default=False)
	garaz = models.BooleanField(default=False)
	parking = models.BooleanField(default=False)
	piwnica = models.BooleanField(default=False)
	klimatyzacja = models.BooleanField(default=False)
	balkon = models.BooleanField(default=False)
	taras = models.BooleanField(default=False)
	ogrodek = models.BooleanField(default=False)
	prad = models.BooleanField(default=False)
	gaz = models.BooleanField(default=False)
	woda = models.BooleanField(default=False)
	kanalizacja = models.BooleanField(default=False)
	szambo = models.BooleanField(default=False)
	oczyszczalnia = models.BooleanField(default=False)
	telefon = models.BooleanField(default=False)
	internet = models.BooleanField(default=False)
	tel_kablowa = models.BooleanField(default=False)
	miejskie = models.BooleanField(default=False)
	gazowe = models.BooleanField(default=False)
	olejowe = models.BooleanField(default=False)
	elektryczne = models.BooleanField(default=False)
	weglowe = models.BooleanField(default=False)
	piece_kaflowe = models.BooleanField(default=False)
	kominkowe = models.BooleanField(default=False)
	kolektor_sloneczny = models.BooleanField(default=False)
	pompa_ciepla = models.BooleanField(default=False)
	biomasa = models.BooleanField(default=False)
	dojazd = models.CharField(max_length=30, choices=DOJAZD_CHOICES, default='asfalt')
	teren_zamkniety = models.BooleanField(default=False)
	monitoring = models.BooleanField(default=False)
	alarm = models.BooleanField(default=False)
	drzwi_anty = models.BooleanField(default=False)
	rolety = models.BooleanField(default=False)
	domofon = models.BooleanField(default=False)
	meble = models.BooleanField(default=False)
	meble_czesc = models.BooleanField(default=False)
	kuchenka = models.BooleanField(default=False)
	pralka = models.BooleanField(default=False)
	lodowka = models.BooleanField(default=False)
	zmywarka = models.BooleanField(default=False)
	piekarnik = models.BooleanField(default=False)
	mikrofala = models.BooleanField(default=False)
	telewizor = models.BooleanField(default=False)
	
		
	class Meta:
		ordering = ('nieruchomosc',)
		
		
class Pokoje(models.Model):
	NIERUCH_CHOICES = (('wolnostojący', 'wolnostojący'),
						('bliźniak', 'bliźniak'),
						('szeregówka', 'szeregówka'),
						('kamienica', 'kamienica'),
						('blok', 'blok'),
						('apartamentowiec', 'apartamentowiec'),
						('loft', 'loft'))
	RODZAJ_CHOICES = (('jednopoziomowe', 'jednopoziomowe'), 
						('dwupoziomowe', 'dwupoziomowe'), 
						('poddasze', 'poddasze'), 
						('loft', 'loft'))
	ILOSCOS_CHOICES = (('jednoosobowy', 'jednoosobowy'), 
						('dwuosobowy', 'dwuosobowy'), 
						('trzyosobowy', 'trzyosobowy'),
						('czteroosobowy', 'czteroosobowy'),
						('wiecej', 'więcej'))					
	nieruchomosc = models.OneToOneField(Nieruchomosc, related_name='pokojes')
	powierz_mieszkania = models.DecimalField(max_digits=12, decimal_places=0, blank=True, default=0)
	rodzaj_zabud = models.CharField(max_length=30, choices=NIERUCH_CHOICES, blank=True)
	rodzaj_mieszkania = models.CharField(max_length=30, choices=RODZAJ_CHOICES, default='jednopoziomowe')
	pietro = models.CharField(max_length=3)
	czynsz = models.DecimalField(max_digits=12, decimal_places=0, blank=True, default=0)
	kaucja = models.DecimalField(max_digits=12, decimal_places=0, blank=True, default=0)
	dostepne = models.CharField(max_length=30, blank=True)
	ilosc_pokoi = models.PositiveIntegerField(default=0)
	ilosc_osob = models.CharField(max_length=3, choices=ILOSCOS_CHOICES, default='jednoosobowy')
	prad = models.BooleanField(default=False)
	gaz = models.BooleanField(default=False)
	woda = models.BooleanField(default=False)
	kanalizacja = models.BooleanField(default=False)
	szambo = models.BooleanField(default=False)
	oczyszczalnia = models.BooleanField(default=False)
	telefon = models.BooleanField(default=False)
	internet = models.BooleanField(default=False)
	tel_kablowa = models.BooleanField(default=False)
	miejskie = models.BooleanField(default=False)
	gazowe = models.BooleanField(default=False)
	olejowe = models.BooleanField(default=False)
	elektryczne = models.BooleanField(default=False)
	weglowe = models.BooleanField(default=False)
	piece_kaflowe = models.BooleanField(default=False)
	kominkowe = models.BooleanField(default=False)
	kolektor_sloneczny = models.BooleanField(default=False)
	pompa_ciepla = models.BooleanField(default=False)
	biomasa = models.BooleanField(default=False)
	meble = models.BooleanField(default=False)
	meble_czesc = models.BooleanField(default=False)
	kuchenka = models.BooleanField(default=False)
	pralka = models.BooleanField(default=False)
	lodowka = models.BooleanField(default=False)
	zmywarka = models.BooleanField(default=False)
	piekarnik = models.BooleanField(default=False)
	mikrofala = models.BooleanField(default=False)
	telewizor = models.BooleanField(default=False)
	
	class Meta:
		ordering = ('nieruchomosc',)
		
		
	
class Garage(models.Model):
	GARAGE_CHOICES = (('wolnostojący', 'wolnostojący'),
						('w budynku', 'w budynku'),
						('przy domu', 'przy domu'))
	KONSTR_CHOICES = (('murowany', 'murowany'), 
						('blaszany', 'blaszany'), 
						('drewniany', 'drewniany'),
						('wiata', 'wiata'),
						('inny', 'inny'))
	nieruchomosc = models.OneToOneField(Nieruchomosc, related_name='garages')					
	powierz_garage = models.DecimalField(max_digits=12, decimal_places=0, blank=True, default=0)
	rodzaj_zabud = models.CharField(max_length=30, choices=GARAGE_CHOICES, blank=True)
	konstr_garage = models.CharField(max_length=30, choices=KONSTR_CHOICES, default='murowany')
	czynsz = models.DecimalField(max_digits=12, decimal_places=0, blank=True, default=0)
	kaucja = models.DecimalField(max_digits=12, decimal_places=0, blank=True, default=0)
	dostepne = models.CharField(max_length=30, blank=True)
	ogrzewanie = models.BooleanField(default=False)
	oswietlenie = models.BooleanField(default=False)
	woda = models.BooleanField(default=False)
	kanalizacja = models.BooleanField(default=False)
	szambo = models.BooleanField(default=False)
	
	
	class Meta:
		ordering = ('nieruchomosc',)

class Komercyjne(models.Model):
	NIERUCH_CHOICES = (('lokal usługowy', 'lokal usługowy'),
						('lokal handlowy', 'lokal handlowy'),
						('lokal biurowy', 'lokal biurowy'),	
						('lokal gastronomiczny', 'lokal gastronomiczny'),
						('klub', 'klub'),
						('hala magazynowa', 'hala magazynowa'), 
						('hala przemysłowa', 'hala przemysłowa'), 
						('biurowiec', 'biurowiec'), 
						('zakład przemysłowy', 'zakład przemysłowy'), 
						('hotel', 'hotel'), 
						('pensjonat', 'pensjonat'),
						('dom seniora', 'dom seniora'), 
						('DPS', 'DPS'), 
						('klinika', 'klinika'), 
						('przychodnia', 'przychodnia'),
						('gabinet stomatologiczny', 'gabinet stomatologiczny'),
						('pałac', 'pałac'))
	POZYCJA_CHOICES = (('nieruchomość samodzielna', 'nieruchomość samodzielna'),
						('część nieruchomości', 'część nieruchomości'))
	STATUS_CHOICES = (('własność', 'własność'), ('dzierżawa wieczysta', 'dzierżawa wieczysta'))
	MATERIAL_CHOICES = (('cegła', 'cegła'),
						('silikat', 'silikat'), 
						('beton komórkowy', 'beton komórkowy'), 
						('konstrukcja stalowa', 'konstrukcja stalowa'), 
						('konstrukcja żel-betonowa', 'konstrukcja żel-betonowa'),
						('silikat', 'silikat'), 
						('keramzyt', 'keramzyt'), 
						('wielka płyta', 'wielka płyta'), 
						('beton', 'beton'), 
						('drewno', 'drewno'), 
						('inne', 'inne'))
	DACH_CHOICES = (('płaski', 'płaski'), ('skośny', 'skośny'))
	POKRYCIE_CHOICES = (('dachówka ceramiczna', 'dachówka ceramiczna'),
						('blachodachówka', 'blachodachówka'), 
						('dachówka inna', 'dachówka inna'), 
						('eternit', 'eternit'), 
						('papa', 'papa'), 
						('gont', 'gont'), 
						('łupek', 'łupek'), 
						('strzecha', 'strzecha'), 
						('inne', 'inne'))
	WYKONCZENIE_CHOICES = (('do użytku', 'do użytku'),
						('do adaptacji', 'do adaptacji'), 
						('do remontu', 'do remontu'), 
						('stan surowy zamknięty', 'stan surowy zamknięty'), 
						('stan surowy otwarty', 'stan surowy otwarty'), 
						('inne', 'inne'))
	OKNA_CHOICES = (('drewniane', 'drewniane'),
						('plastikowe', 'plastikowe'), 
						('aluminiowe', 'aluminiowe'),
						('stalowe', 'stalowe'))
	POSADZKA_CHOICES = (('pylna', 'pylna'),
						('niepylna', 'niepylna'), 
						('specjalna', 'specjalna'),
						('inna', 'inna')) 
	PARKING_CHOICES = (('asfalt', 'asfalt'),
						('beton', 'beton'), 
						('kostka brukowa', 'kostka brukowa'),
						('utwardzony', 'utwardzony'),
						('nieutwardzony', 'nieutwardzony'),
						('brak', 'brak'),
						('inny', 'inny'))
	POLOZENIE_CHOICES = (('odzielny obiekt', 'odzielny obiekt'),
						('biurowiec', 'biurowiec'), 
						('centrum handlowe', 'centrum handlowe'),
						('obiekt przemysłowy', 'obiekt przemysłowy'),
						('hala magazynowa', 'hala magazynowa'),
						('blok', 'blok'),
						('kamienica', 'kamienica'),
						('inny', 'inny'))
	DOJAZD_CHOICES = (('asfalt', 'asfalt'), ('utwardzony', 'utwardzony'), ('nieutwardzony', 'nieutwardzony'))
	OGRODZENIE_CHOICES = (('drewniane', 'drewniane'),
						('metalowe', 'metalowe'), 
						('betonowe', 'betonowe'),
						('murowane', 'murowane'), 
						('siatka', 'siatka'), 
						('żywopłot', 'żywopłot'), 
						('inne', 'inne')) 	
	OGRZEWANIE_CHOICES = (('miejskie', 'miejskie'),
						('gazowe', 'gazowe'), 
						('olejowe', 'olejowe'),
						('węglowe', 'węglowe'),
						('kolektory słoneczne', 'kolektory słoneczne'),
						('inne', 'inne'),
						('brak', 'brak')) 
	nieruchomosc = models.OneToOneField(Nieruchomosc, related_name='komercyjnes')
	powierz_nieruchomosci = models.DecimalField(max_digits=12, decimal_places=0, blank=True, default=0)
	powierz_dzialki = models.DecimalField(max_digits=12, decimal_places=0, blank=True, default=0)
	status_dzial = models.CharField(max_length=30, choices=STATUS_CHOICES, default='własność')
	info_mpzp = models.TextField(blank=True)
	rodzaj_nieruchom = models.CharField(max_length=30, choices=NIERUCH_CHOICES, blank=True)
	pozycja_nieruchom = models.CharField(max_length=30, choices=POZYCJA_CHOICES, blank=True)
	rok_budowy = models.CharField(max_length=4, blank=True)
	polozenie_lokalu = models.CharField(max_length=30, choices=POLOZENIE_CHOICES, blank=True)
	rodz_materialu = models.CharField(max_length=30, choices=MATERIAL_CHOICES, blank=True)
	dach = models.CharField(max_length=30, choices=DACH_CHOICES, blank=True)
	pokrycie_dach = models.CharField(max_length=30, choices=POKRYCIE_CHOICES, blank=True)
	stan_wykonczenia = models.CharField(max_length=30, choices=WYKONCZENIE_CHOICES, blank=True)
	okna = models.CharField(max_length=30, choices=OKNA_CHOICES, blank=True)
	posadzka = models.CharField(max_length=30, choices=POSADZKA_CHOICES, blank=True)
	parking = models.CharField(max_length=30, choices=PARKING_CHOICES, blank=True)
	ilosc_kond = models.PositiveIntegerField(default=0)
	ilosc_pokoi = models.PositiveIntegerField(default=0)
	klimatyzacja = models.BooleanField(default=False)
	prad = models.BooleanField(default=False)
	gaz = models.BooleanField(default=False)
	woda = models.BooleanField(default=False)
	kanalizacja = models.BooleanField(default=False)
	szambo = models.BooleanField(default=False)
	oczyszczalnia = models.BooleanField(default=False)
	telefon = models.BooleanField(default=False)
	internet = models.BooleanField(default=False)
	tel_kablowa = models.BooleanField(default=False)
	monitoring = models.BooleanField(default=False)
	oczyszczalnia = models.BooleanField(default=False)
	ogrzewanie = models.CharField(max_length=30, choices=OGRZEWANIE_CHOICES, blank=True)
	ogrodzenie = models.CharField(max_length=30, choices=OGRODZENIE_CHOICES, blank=True)
	dojazd = models.CharField(max_length=30, choices=DOJAZD_CHOICES, blank=True)
	teren_przemyslowy = models.BooleanField(default=False)
	teren_zdrojowy = models.BooleanField(default=False)
	teren_turystyczny = models.BooleanField(default=False)
	las = models.BooleanField(default=False)
	gory = models.BooleanField(default=False)
	jezioro = models.BooleanField(default=False)
	morze = models.BooleanField(default=False)
	teren_otwarty = models.BooleanField(default=False)

	class Meta:
		ordering = ('nieruchomosc',)
			

		

class Powierzchnie(models.Model):
	NIERUCH_CHOICES = (('lokal handlowy', 'lokal handlowy'), 
						('lokal gastronomiczny', 'lokal gastronomiczny'),
						('klub', 'klub'),
						('pub', 'pub'),
						('powierzchnia handlowa', 'powierzchnia handlowa'),
						('powierzchnia magazynowa', 'powierzchnia magazynowa'), 
						('hala magazynowa', 'hala magazynowa'),
						('hala przemysłowa', 'hala przemysłowa'), 
						('powierzchnia biurowa', 'powierzchnia biurowa'), 
						('powierzchnia przemysłowa', 'powierzchnia przemysłowa'), 
						('powierzchnia hotelowa', 'powierzchnia hotelowa'), 
						('klinika', 'klinika'), 
						('przychodnia', 'przychodnia'),
						('gabinet stomatologiczny', 'gabinet stomatologiczny'))
	POZYCJA_CHOICES = (('nieruchomość samodzielna', 'nieruchomość samodzielna'),
						('część nieruchomości', 'część nieruchomości'))
	MATERIAL_CHOICES = (('cegła', 'cegła'),
						('silikat', 'silikat'), 
						('beton komórkowy', 'beton komórkowy'), 
						('konstrukcja stalowa', 'konstrukcja stalowa'), 
						('konstrukcja żel-betonowa', 'konstrukcja żel-betonowa'),
						('silikat', 'silikat'), 
						('keramzyt', 'keramzyt'), 
						('wielka płyta', 'wielka płyta'), 
						('beton', 'beton'), 
						('drewno', 'drewno'), 
						('inne', 'inne'))
	DACH_CHOICES = (('płaski', 'płaski'), ('skośny', 'skośny'))
	POKRYCIE_CHOICES = (('dachówka ceramiczna', 'dachówka ceramiczna'),
						('blachodachówka', 'blachodachówka'), 
						('dachówka inna', 'dachówka inna'), 
						('eternit', 'eternit'), 
						('papa', 'papa'), 
						('gont', 'gont'), 
						('łupek', 'łupek'), 
						('strzecha', 'strzecha'), 
						('inne', 'inne'))
	WYKONCZENIE_CHOICES = (('do użytku', 'do użytku'),
						('do adaptacji', 'do adaptacji'), 
						('do remontu', 'do remontu'), 
						('inne', 'inne'))
	OKNA_CHOICES = (('drewniane', 'drewniane'),
						('plastikowe', 'plastikowe'), 
						('aluminiowe', 'aluminiowe'),
						('stalowe', 'stalowe'))
	POSADZKA_CHOICES = (('pylna', 'pylna'),
						('niepylna', 'niepylna'), 
						('specjalna', 'specjalna'),
						('inna', 'inna')) 
	PARKING_CHOICES = (('asfalt', 'asfalt'),
						('beton', 'beton'), 
						('kostka brukowa', 'kostka brukowa'),
						('utwardzony', 'utwardzony'),
						('nieutwardzony', 'nieutwardzony'),
						('brak', 'brak'),
						('inny', 'inny'))
	POLOZENIE_CHOICES = (('odzielny obiekt', 'odzielny obiekt'),
						('biurowiec', 'biurowiec'), 
						('centrum handlowe', 'centrum handlowe'),
						('obiekt przemysłowy', 'obiekt przemysłowy'),
						('hala magazynowa', 'hala magazynowa'),
						('blok', 'blok'),
						('kamienica', 'kamienica'),
						('inny', 'inny'))
	DOJAZD_CHOICES = (('asfalt', 'asfalt'), ('utwardzony', 'utwardzony'), ('nieutwardzony', 'nieutwardzony'))
	OGRODZENIE_CHOICES = (('drewniane', 'drewniane'),
						('metalowe', 'metalowe'), 
						('betonowe', 'betonowe'),
						('murowane', 'murowane'), 
						('siatka', 'siatka'), 
						('żywopłot', 'żywopłot'), 
						('inne', 'inne')) 	
	OGRZEWANIE_CHOICES = (('miejskie', 'miejskie'),
						('gazowe', 'gazowe'), 
						('olejowe', 'olejowe'),
						('węglowe', 'węglowe'),
						('kolektory słoneczne', 'kolektory słoneczne'),
						('inne', 'inne'),
						('brak', 'brak')) 
	nieruchomosc = models.OneToOneField(Nieruchomosc, related_name='powierzchnies')
	powierz_nieruchomosci = models.DecimalField(max_digits=12, decimal_places=0, blank=True, default=0)
	powierz_dzialki = models.DecimalField(max_digits=12, decimal_places=0, blank=True, default=0)
	rodzaj_nieruchom = models.CharField(max_length=30, choices=NIERUCH_CHOICES, blank=True)
	pozycja_nieruchom = models.CharField(max_length=30, choices=POZYCJA_CHOICES, blank=True)
	rok_budowy = models.CharField(max_length=4, blank=True)
	czynsz = models.DecimalField(max_digits=12, decimal_places=0, blank=True, default=0)
	kaucja = models.DecimalField(max_digits=12, decimal_places=0, blank=True, default=0)
	dostepne = models.CharField(max_length=30, blank=True)
	polozenie_lokalu = models.CharField(max_length=30, choices=POLOZENIE_CHOICES, blank=True)
	rodz_materialu = models.CharField(max_length=30, choices=MATERIAL_CHOICES, blank=True)
	dach = models.CharField(max_length=30, choices=DACH_CHOICES, blank=True)
	pokrycie_dach = models.CharField(max_length=30, choices=POKRYCIE_CHOICES, blank=True)
	stan_wykonczenia = models.CharField(max_length=30, choices=WYKONCZENIE_CHOICES, blank=True)
	okna = models.CharField(max_length=30, choices=OKNA_CHOICES, blank=True)
	posadzka = models.CharField(max_length=30, choices=POSADZKA_CHOICES, blank=True)
	parking = models.CharField(max_length=30, choices=PARKING_CHOICES, blank=True)
	ilosc_kond = models.PositiveIntegerField(default=0)
	ilosc_pokoi = models.PositiveIntegerField(default=0)
	klimatyzacja = models.BooleanField(default=False)
	prad = models.BooleanField(default=False)
	gaz = models.BooleanField(default=False)
	woda = models.BooleanField(default=False)
	kanalizacja = models.BooleanField(default=False)
	szambo = models.BooleanField(default=False)
	oczyszczalnia = models.BooleanField(default=False)
	telefon = models.BooleanField(default=False)
	internet = models.BooleanField(default=False)
	tel_kablowa = models.BooleanField(default=False)
	monitoring = models.BooleanField(default=False)
	oczyszczalnia = models.BooleanField(default=False)
	ogrzewanie = models.CharField(max_length=30, choices=OGRZEWANIE_CHOICES, blank=True)
	ogrodzenie = models.CharField(max_length=30, choices=OGRODZENIE_CHOICES, blank=True)
	dojazd = models.CharField(max_length=30, choices=DOJAZD_CHOICES, blank=True)
	teren_przemyslowy = models.BooleanField(default=False)
	teren_zdrojowy = models.BooleanField(default=False)
	teren_turystyczny = models.BooleanField(default=False)
	las = models.BooleanField(default=False)
	gory = models.BooleanField(default=False)
	jezioro = models.BooleanField(default=False)
	morze = models.BooleanField(default=False)
	teren_otwarty = models.BooleanField(default=False)

	class Meta:
		ordering = ('nieruchomosc',)		


		
class Dewelopr(models.Model):
	RODZAJ_CHOICES = (('mieszkanie', 'mieszkanie'), 
						('szeregowka', 'szeregówka'), 
						('blizniak', 'bliźniak'), 
						('dom', 'dom'))
	nieruchomosc = models.OneToOneField(Nieruchomosc, related_name='dewelopers')
	powierz_nieruchomosci = models.DecimalField(max_digits=12, decimal_places=0, blank=True, default=0)
	ilosc_poczat = models.IntegerField(blank=True, default=0)

	class Meta:
		ordering = ('nieruchomosc',)
		

		
	
class ImageItem(models.Model):
	nieruchomosc = models.ForeignKey(Nieruchomosc, related_name='imageitems')
	title = models.CharField(max_length=65, blank=True)
	image = models.ImageField(upload_to='images/%y/%m/%d')
	opis = models.TextField(blank=True)
	created = models.DateField(auto_now_add=True, db_index=True)
	
	def __str__(self):
		return self.title