from django.conf.urls import url
from . import views

urlpatterns = [
	
    url(r'^$', views.bithouse_start, name='startbit'),
	url(r'^home/$', views.bithouse_home, name='home'),
	url(r'^ogloszenia/$', views.ogloszenia, name='ogloszenia'),
	#url(r'^ogloszenia/bit/realestate/nieruchomosc/(?P<id>\d+)/$', views.detail, name='detail'),
	url(r'^dzialki/bit/realestate/nieruchomosc/(?P<id>\d+)/$', views.detail_dzi, name='detail_dzi'),
	url(r'^domy/bit/realestate/nieruchomosc/(?P<id>\d+)/$', views.detail_dom, name='detail_dom'),
	url(r'^domy/wy/bit/realestate/nieruchomosc/(?P<id>\d+)/$', views.detail_dom_wy, name='detail_dom_wy'),
	url(r'^mieszkania/bit/realestate/nieruchomosc/(?P<id>\d+)/$', views.detail_mie, name='detail_mie'),
	url(r'^mieszkania/wy/bit/realestate/nieruchomosc/(?P<id>\d+)/$', views.detail_mie_wy, name='detail_mie_wy'),
	url(r'^komercyjne/bit/realestate/nieruchomosc/(?P<id>\d+)/$', views.detail_kom, name='detail_kom'),
	url(r'^komercyjne/wy/bit/realestate/nieruchomosc/(?P<id>\d+)/$', views.detail_kom_wy, name='detail_kom_wy'),
	url(r'^deweloper/bit/realestate/nieruchomosc/(?P<id>\d+)/$', views.detail_dew, name='detail_dew'),
	#url(r'^pow/bit/realestate/nieruchomosc/(?P<id>\d+)/$', views.detail_pow, name='detail_pow'),
	url(r'^dzialki/$', views.ogloszenia_dzialki, name='dzialki'),
	url(r'^dzialki/wy/$', views.ogloszenia_dzialki_wy, name='dzialki_wy'),
	url(r'^domy/$', views.ogloszenia_domy, name='domy'),
	url(r'^domy/wy/$', views.ogloszenia_domy_wy, name='domy_wy'),
	url(r'^mieszkania/$', views.ogloszenia_mieszkania, name='mieszkania'),
	url(r'^pokoje/$', views.ogloszenia_pokoje, name='pokoje'),
	url(r'^garage/$', views.ogloszenia_garage, name='garage'),
	url(r'^mieszkania/wy/$', views.ogloszenia_mieszkania_wy, name='mieszkania_wy'),
	url(r'^komercyjne/$', views.ogloszenia_komercyjne, name='komercyjne'),
	url(r'^komercyjne/wy/$', views.ogloszenia_komercyjne_wy, name='komercyjne_wy'),
	url(r'^deweloper/$', views.ogloszenia_deweloper, name='deweloper'),
	url(r'^deweloper/dom/$', views.ogloszenia_deweloper_dom, name='deweloper_dom'),
	
]