from django.contrib import admin
from .models import Profile, Profilefirm

class ProfileAdmin(admin.ModelAdmin):
	list_display = ['user', 'adres', 'kod_pocztowy', 'miejscowosc', 'telefon', 'data_urodzenia', 'status', 'firma']

admin.site.register(Profile, ProfileAdmin)