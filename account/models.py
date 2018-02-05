from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.text import slugify
from realestate.models import Profilefirm, Miejscowosc

class Profile(models.Model):
	STATUS_CHOICES = (('fizyczna', 'Osoba fizyczna'), ('firmap', 'Przedstawiciel firmy'), ('biurop', 'Przedstawiciel biura'))
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	adres = models.CharField(max_length=60)
	kod_pocztowy = models.CharField(max_length=6)
	miejscowosc = models.ForeignKey(Miejscowosc, related_name='account_profiles', default=1)
	telefon = models.CharField(max_length=30, blank=True, null=True)
	data_urodzenia = models.DateField(blank=True, null=True)
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='fizyczna')
	firma = models.ForeignKey(Profilefirm, related_name='account_profiles', default=2)
	
	def __str__(self):
		return 'Profil użytkownika {}.'.format(self.user.username)