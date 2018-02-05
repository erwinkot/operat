from django.conf.urls import url
from . import views

urlpatterns = [
	
    url(r'^$', views.realestate_start, name='startre'),
	url(r'^cennik/$', views.cennik, name='cennik'),
	url(r'^regulamin/$', views.regulamin, name='regulamin'),
	#url(r'^edfi/$', views.edit_firm, name='editfirm'),
	url(r'^pitka/$', views.probino, name='probino'),
	url(r'^fspr/$', views.firma_sprawdzana, name='sprfirma'),
	url(r'^fsprok/$', views.firma_sprawdzana, name='sprfirmaok'),
	url(r'^fspdopis/$', views.firma_dopisanie, name='firmadopis'),
	url(r'^(?P<nip>[0-9]+)/$', views.edit_firm, name='editfirm'),
	url(r'^newfi/$', views.new_firm, name='new_firm'),
	url(r'^parej/$', views.panel_rejestr, name='rejestrnieruchom'),
	url(r'^reniedz/$', views.add_nieruchomosc_dzi, name='addnieruchomoscdzi'),
	url(r'^reniedom/$', views.add_nieruchomosc_dom, name='addnieruchomoscdom'),
	url(r'^przeglad/$', views.przeglad, name='przeglad'),
	url(r'^reniemie/$', views.add_nieruchomosc_mie, name='addnieruchomoscmie'),
	url(r'^reniepok/$', views.add_nieruchomosc_pok, name='addnieruchomoscpok'),
	url(r'^reniegar/$', views.add_nieruchomosc_gar, name='addnieruchomoscgar'),
	url(r'^reniekom/$', views.add_nieruchomosc_kom, name='addnieruchomosckom'),
	#url(r'^reniedew/$', views.add_nieruchomosc_dew, name='addnieruchomoscdew'),
	url(r'^redzia/(?P<id>\d+)/$', views.edit_dzialki, name='editdzialki'),
	url(r'^editniedzia/(?P<id>\d+)/$', views.edit_nieruchomosc_dzi, name='editnieruchdzi'),
	url(r'^editniedom/(?P<id>\d+)/$', views.edit_nieruchomosc_dom, name='editnieruchdom'),
	url(r'^editniemie/(?P<id>\d+)/$', views.edit_nieruchomosc_mie, name='editnieruchmie'),
	url(r'^editniepok/(?P<id>\d+)/$', views.edit_nieruchomosc_pok, name='editnieruchpok'),
	url(r'^editniegar/(?P<id>\d+)/$', views.edit_nieruchomosc_gar, name='editnieruchgar'),
	url(r'^editniekom/(?P<id>\d+)/$', views.edit_nieruchomosc_kom, name='editnieruchkom'),
	url(r'^redom/(?P<id>\d+)/$', views.edit_domy, name='editdomy'),
	url(r'^imageadd/(?P<id>\d+)/$', views.add_image_item, name='addimageitem'),
	url(r'^remies/(?P<id>\d+)/$', views.edit_mieszkania, name='editmieszkania'),
	url(r'^repoko/(?P<id>\d+)/$', views.edit_mieszkania, name='editpokoje'),
	url(r'^regara/(?P<id>\d+)/$', views.edit_garage, name='editgarage'),
	url(r'^rekom/(?P<id>\d+)/$', views.edit_komercyjne, name='editkomercyjne'),
	#url(r'^redew/(?P<id>\d+)/$', views.edit_mieszkania, name='editdeweloper'),
	url(r'^nieruchomosc/(?P<id>\d+)/$', views.nieruchomosc_detail, name='nieruchomosc_detail'),
]