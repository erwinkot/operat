from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import ProfileFirmEditForm, SprFirm, NieruchomoscEditForm, NieruchomstaffEditForm, DzialkiEditForm, DomyEditForm, MieszkaniaEditForm, PokojeEditForm, GarageEditForm, KomercyjneEditForm, ImageItemEditForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profilefirm, Miejscowosc, Nieruchomosc, Nieruchomstaff, Dzialki, Domy, Mieszkania, Pokoje, Garage, Komercyjne, ImageItem
from account.models import Profile
from django.contrib.auth.models import User


def realestate_start(request):
		
	return render(request, 'realestate/client/startre.html')
	
	
def profilefirm_detail(request):
		
	return render(request, 'realestate/client/profilefirm.html')
	
	
def cennik(request):
		
	return render(request, 'realestate/client/cennik.html')
	
	
def regulamin(request):
		
	return render(request, 'realestate/client/regulamin.html')
	
	
@login_required
def panel_rejestr(request):
		
	return render(request, 'realestate/client/rejestrnieruchom.html',)	


@login_required
def probino(request, nieruchomosc_id=None):

	nieruchomosc = None
	nieruchomoscs = Nieruchomosc.objects.filter(user=request.user).select_related('dzialki')
	
	
	return render(request, 'realestate/client/probino.html', {'nieruchomoscs': nieruchomoscs})



	
@login_required
def firma_sprawdzana(request, nip=None):
	
	if request.method == 'POST':
		spr_form = SprFirm(request.POST)
		if spr_form.is_valid():
			cd = spr_form.cleaned_data
			profilefirm = Profilefirm.objects.filter(nip=cd['nip_firmy'])
			if profilefirm:
				#profile = get_object_or_404(Profile, user=request.user)
				#profile.firma = profilefirm
				#profile.save()
			
				return render(request, 'realestate/client/sprfirmaok.html', {'profilefirm': profilefirm})
			
			else: 	
				komenda = 'Firma o podanym NIP-ie nie istnieje.'
				return render(request, 'realestate/client/sprfirmaoff.html', {'komenda': komenda})
	else:
		spr_form = SprFirm()
		
	return render(request, 'realestate/client/sprfirma.html', {'spr_form': spr_form})


@login_required
def firma_dopisanie(request, nip=None):
	
	if request.method == 'POST':
		spr_form = SprFirm(request.POST)
		if spr_form.is_valid():
			cd = spr_form.cleaned_data
			profilefirm = Profilefirm.objects.filter(nip=cd['nip_firmy'])
			profile = get_object_or_404(Profile, user=request.user)
			#profile.firma = profilefirm
			profile.save()
				
			komendana = 'Dopisano użytkownika do firmy'
			
			return render(request, 'realestate/client/firmadopis.html', {'profile': profile, 'profilefirm': profilefirm})
			
		else: 	
				komenda = 'Firma o podanym NIP-ie nie istnieje.'
				return render(request, 'realestate/client/firmadopis.html', {'komenda': komenda})
	else:
		spr_form = SprFirm()
		
	return render(request, 'realestate/client/firmadopis.html', {'spr_form': spr_form})
	
@login_required
def edit_firm(request, nip): 
	
	profilefirm = get_object_or_404(Profilefirm, nip=nip)
	if request.method == 'POST':
		profilefirm_form = ProfileFirmEditForm(instance=profilefirm, data=request.POST, files=request.FILES)
		if profilefirm_form.is_valid():
			profilefirm_form.save()
			
			messages.success(request, 'Uaktualnienie profilu '\
										'zakończyło się sukcesem.')
		else:
			messages.error(request, 'Wystąpił błąd podczas uaktualniania profilu.')
	else:
		profilefirm_form = ProfileFirmEditForm(instance=profilefirm)
												
	return render(request,
					'realestate/client/editfirm.html',
						{'profilefirm_form': profilefirm_form})



@login_required
def new_firm(request): 
	
	if request.method == 'POST':
		new_profilefirm_form = ProfileFirmEditForm(data=request.POST, files=request.FILES)
        
		if  new_profilefirm_form.is_valid():
			cd = new_profilefirm_form.cleaned_data
			new_firm = new_profilefirm_form.save(commit=False)
			
			profile = get_object_or_404(Profile, user=request.user)
			new_firm.save()			
			profile.firma = new_firm
			
			profile.save()
			
			messages.success(request, 'Uaktualnienie profilu '\
										'zakończyło się sukcesem.')
		else:
			messages.error(request, 'Wystąpił błąd podczas uaktualniania profilu.')
	else:
		new_profilefirm_form = ProfileFirmEditForm()
												
	return render(request,
					'realestate/client/new_firm.html',
						{'new_profilefirm_form': new_profilefirm_form})						

						

					
						
						
@login_required	
def add_nieruchomosc_dzi(request):
	
	nieruchomosc = None
	if request.method == 'POST':
		nieruchomosc_form = NieruchomoscEditForm(data=request.POST, files=request.FILES)
		
		if  nieruchomosc_form.is_valid():
			#cd = nieruchomosc_form.cleaned_data
			new_nieruchomosc = nieruchomosc_form.save(commit=False)
			new_nieruchomosc.user = request.user
			new_nieruchomosc.profil = 'dzialka'
			new_nieruchomosc.save()
			nieruchomstaff = Nieruchomstaff.objects.create(nieruchomosc=new_nieruchomosc)
			dzialki = Dzialki.objects.create(nieruchomosc=new_nieruchomosc)
			
			messages.success(request, 'Uaktualnienie profilu '\
										'zakończyło się sukcesem.')
			return redirect('realestate:editdzialki', id=new_nieruchomosc.id)
					
									
		else:
			messages.error(request, 'Wystąpił błąd podczas uaktualniania profilu.')
		
		
						
	else:
		nieruchomosc_form = NieruchomoscEditForm()
												
	return render(request,
					'realestate/client/addnieruchomoscdzi.html',
						{'nieruchomosc_form': nieruchomosc_form})


@login_required	
def add_nieruchomosc_dom(request):
	
	if request.method == 'POST':
		nieruchomosc_form = NieruchomoscEditForm(data=request.POST, files=request.FILES)
        
		if  nieruchomosc_form.is_valid():
			cd = nieruchomosc_form.cleaned_data
			new_nieruchomosc = nieruchomosc_form.save(commit=False)
			new_nieruchomosc.user = request.user
			new_nieruchomosc.profil = 'dom'
			new_nieruchomosc.save()
			nieruchomstaff = Nieruchomstaff.objects.create(nieruchomosc=new_nieruchomosc)
			domy = Domy.objects.create(nieruchomosc=new_nieruchomosc)
			
			messages.success(request, 'Uaktualnienie profilu '\
										'zakończyło się sukcesem.')
										
			return redirect('realestate:editdomy', id=new_nieruchomosc.id)
			
						
		else:
			messages.error(request, 'Wystąpił błąd podczas uaktualniania profilu.')
				
						
	else:
		nieruchomosc_form = NieruchomoscEditForm()
												
	return render(request,
					'realestate/client/addnieruchomoscdom.html',
						{'nieruchomosc_form': nieruchomosc_form})						
						

@login_required	
def add_nieruchomosc_mie(request):
	
	if request.method == 'POST':
		nieruchomosc_form = NieruchomoscEditForm(data=request.POST, files=request.FILES)
        
		if  nieruchomosc_form.is_valid():
			cd = nieruchomosc_form.cleaned_data
			new_nieruchomosc = nieruchomosc_form.save(commit=False)
			new_nieruchomosc.user = request.user
			new_nieruchomosc.profil = 'mieszkanie'
			new_nieruchomosc.save()
			nieruchomstaff = Nieruchomstaff.objects.create(nieruchomosc=new_nieruchomosc)
			mieszkania = Mieszkania.objects.create(nieruchomosc=new_nieruchomosc)
			
			messages.success(request, 'Uaktualnienie profilu '\
										'zakończyło się sukcesem.')
										
			return redirect('realestate:editmieszkania', id=new_nieruchomosc.id)
			
						
		else:
			messages.error(request, 'Wystąpił błąd podczas uaktualniania profilu.')
				
						
	else:
		nieruchomosc_form = NieruchomoscEditForm()
												
	return render(request,
					'realestate/client/addnieruchomoscmie.html',
						{'nieruchomosc_form': nieruchomosc_form})



@login_required	
def add_nieruchomosc_pok(request):
	
	if request.method == 'POST':
		nieruchomosc_form = NieruchomoscEditForm(data=request.POST, files=request.FILES)
        
		if  nieruchomosc_form.is_valid():
			cd = nieruchomosc_form.cleaned_data
			new_nieruchomosc = nieruchomosc_form.save(commit=False)
			new_nieruchomosc.user = request.user
			new_nieruchomosc.profil = 'pokoje'
			new_nieruchomosc.save()
			nieruchomstaff = Nieruchomstaff.objects.create(nieruchomosc=new_nieruchomosc)
			pokoje = Pokoje.objects.create(nieruchomosc=new_nieruchomosc)
			
			messages.success(request, 'Uaktualnienie profilu '\
										'zakończyło się sukcesem.')
										
			return redirect('realestate:editpokoje', id=new_nieruchomosc.id)
			
						
		else:
			messages.error(request, 'Wystąpił błąd podczas uaktualniania profilu.')
				
						
	else:
		nieruchomosc_form = NieruchomoscEditForm()
												
	return render(request,
					'realestate/client/addnieruchomoscpok.html',
						{'nieruchomosc_form': nieruchomosc_form})


						

@login_required	
def add_nieruchomosc_gar(request):
	
	if request.method == 'POST':
		nieruchomosc_form = NieruchomoscEditForm(data=request.POST, files=request.FILES)
        
		if  nieruchomosc_form.is_valid():
			cd = nieruchomosc_form.cleaned_data
			new_nieruchomosc = nieruchomosc_form.save(commit=False)
			new_nieruchomosc.user = request.user
			new_nieruchomosc.profil = 'garage'
			new_nieruchomosc.save()
			nieruchomstaff = Nieruchomstaff.objects.create(nieruchomosc=new_nieruchomosc)
			garage = Garage.objects.create(nieruchomosc=new_nieruchomosc)
			
			messages.success(request, 'Uaktualnienie profilu '\
										'zakończyło się sukcesem.')
										
			return redirect('realestate:editgarage', id=new_nieruchomosc.id)
			
						
		else:
			messages.error(request, 'Wystąpił błąd podczas uaktualniania profilu.')
				
						
	else:
		nieruchomosc_form = NieruchomoscEditForm()
												
	return render(request,
					'realestate/client/addnieruchomoscgar.html',
						{'nieruchomosc_form': nieruchomosc_form})
						
						
						


@login_required	
def add_nieruchomosc_kom(request):
	
	if request.method == 'POST':
		nieruchomosc_form = NieruchomoscEditForm(data=request.POST, files=request.FILES)
        
		if  nieruchomosc_form.is_valid():
			cd = nieruchomosc_form.cleaned_data
			new_nieruchomosc = nieruchomosc_form.save(commit=False)
			new_nieruchomosc.user = request.user
			new_nieruchomosc.profil = 'komercyjne'
			new_nieruchomosc.save()
			nieruchomstaff = Nieruchomstaff.objects.create(nieruchomosc=new_nieruchomosc)
			mieszkania = Komercyjne.objects.create(nieruchomosc=new_nieruchomosc)
			
			messages.success(request, 'Uaktualnienie profilu '\
										'zakończyło się sukcesem.')
										
			return redirect('realestate:editkomercyjne', id=new_nieruchomosc.id)
			
						
		else:
			messages.error(request, 'Wystąpił błąd podczas uaktualniania profilu.')
				
						
	else:
		nieruchomosc_form = NieruchomoscEditForm()
												
	return render(request,
					'realestate/client/addnieruchomosckom.html',
						{'nieruchomosc_form': nieruchomosc_form})	
						
						

@login_required	
def add_nieruchomosc_dew(request):
	
	if request.method == 'POST':
		nieruchomosc_form = NieruchomoscEditForm(data=request.POST, files=request.FILES)
        
		if  nieruchomosc_form.is_valid():
			cd = nieruchomosc_form.cleaned_data
			new_nieruchomosc = nieruchomosc_form.save(commit=False)
			new_nieruchomosc.user = request.user
			new_nieruchomosc.profil = 'deweloper'
			new_nieruchomosc.save()
			nieruchomstaff = Nieruchomstaff.objects.create(nieruchomosc=new_nieruchomosc)
			mieszkania = Mieszkania.objects.create(nieruchomosc=new_nieruchomosc)
			
			messages.success(request, 'Uaktualnienie profilu '\
										'zakończyło się sukcesem.')
										
			return redirect('realestate:editdeweloper', id=new_nieruchomosc.id)
			
						
		else:
			messages.error(request, 'Wystąpił błąd podczas uaktualniania profilu.')
				
						
	else:
		nieruchomosc_form = NieruchomoscEditForm()
												
	return render(request,
					'realestate/client/addnieruchomoscdew.html',
						{'nieruchomosc_form': nieruchomosc_form})	


def add_image_item(request, id):
	nieruchomosc = get_object_or_404(Nieruchomosc, id=id)
	imageitems = ImageItem.objects.filter(nieruchomosc=nieruchomosc)
	if request.method == 'POST':
		images_form = ImageItemEditForm(data=request.POST, files=request.FILES)
        
		if  images_form.is_valid():
			cd = images_form.cleaned_data
			new_images = images_form.save(commit=False)
			new_images.nieruchomosc = nieruchomosc
			new_images.save()
			
			
			messages.success(request, 'Uaktualnienie profilu '\
										'zakończyło się sukcesem.')
										
			return redirect('realestate:addimageitem', id=nieruchomosc.id)
			
						
		else:
			messages.error(request, 'Wystąpił błąd podczas uaktualniania profilu.')
				
						
	else:
		images_form = ImageItemEditForm()
												
	return render(request,
					'realestate/client/imageadd.html',
						{'images_form': images_form, 'nieruchomosc': nieruchomosc, 'imageitems': imageitems})						

@login_required	
def nieruchomosc_detail(request, id):
	
	nieruchomosc = get_object_or_404(Nieruchomosc, id=id)
	imageitems = ImageItem.objects.filter(nieruchomosc=nieruchomosc)
	
												
	return render(request,
					'realestate/client/nieruchomosc_detail.html',
						{'nieruchomosc': nieruchomosc, 'imageitems': imageitems})			



@login_required	
def edit_nieruchomosc_dzi(request, id):
	
	nieruchomosc = get_object_or_404(Nieruchomosc, id=id)
	
	if request.method == 'POST':
		nieruchomosc_form = NieruchomoscEditForm(instance=nieruchomosc, data=request.POST, files=request.FILES)
        
		if  nieruchomosc_form.is_valid():
			cd = nieruchomosc_form.cleaned_data
			nieruchomosc = nieruchomosc_form.save(commit=False)
			nieruchomosc.user = request.user
			nieruchomosc.save()
						
			messages.success(request, 'Uaktualnienie profilu '\
										'zakończyło się sukcesem.')
			return redirect('realestate:editdzialki', id=nieruchomosc.id)					
									
		else:
			messages.error(request, 'Wystąpił błąd podczas uaktualniania profilu.')
		
		
						
	else:
		nieruchomosc_form = NieruchomoscEditForm(instance=nieruchomosc)
												
	return render(request,
					'realestate/client/editnieruchomoscdzi.html',
						{'nieruchomosc': nieruchomosc, 'nieruchomosc_form': nieruchomosc_form})


						
@login_required	
def edit_nieruchomosc_dom(request, id):
	
	nieruchomosc = get_object_or_404(Nieruchomosc, id=id)
	
	if request.method == 'POST':
		nieruchomosc_form = NieruchomoscEditForm(instance=nieruchomosc, data=request.POST, files=request.FILES)
        
		if  nieruchomosc_form.is_valid():
			cd = nieruchomosc_form.cleaned_data
			nieruchomosc = nieruchomosc_form.save(commit=False)
			nieruchomosc.user = request.user
			nieruchomosc.save()
						
			messages.success(request, 'Uaktualnienie profilu '\
										'zakończyło się sukcesem.')
			return redirect('realestate:editdomy', id=nieruchomosc.id)					
									
		else:
			messages.error(request, 'Wystąpił błąd podczas uaktualniania profilu.')
		
		
						
	else:
		nieruchomosc_form = NieruchomoscEditForm(instance=nieruchomosc)
												
	return render(request,
					'realestate/client/editnieruchomoscdom.html',
						{'nieruchomosc': nieruchomosc, 'nieruchomosc_form': nieruchomosc_form})


						
@login_required	
def edit_nieruchomosc_mie(request, id):
	
	nieruchomosc = get_object_or_404(Nieruchomosc, id=id)
	
	if request.method == 'POST':
		nieruchomosc_form = NieruchomoscEditForm(instance=nieruchomosc, data=request.POST, files=request.FILES)
        
		if  nieruchomosc_form.is_valid():
			cd = nieruchomosc_form.cleaned_data
			nieruchomosc = nieruchomosc_form.save(commit=False)
			nieruchomosc.user = request.user
			nieruchomosc.save()
						
			messages.success(request, 'Uaktualnienie profilu '\
										'zakończyło się sukcesem.')
			return redirect('realestate:editmieszkania', id=nieruchomosc.id)					
									
		else:
			messages.error(request, 'Wystąpił błąd podczas uaktualniania profilu.')
		
		
						
	else:
		nieruchomosc_form = NieruchomoscEditForm(instance=nieruchomosc)
												
	return render(request,
					'realestate/client/editnieruchomoscmie.html',
						{'nieruchomosc': nieruchomosc, 'nieruchomosc_form': nieruchomosc_form})
						
						
@login_required	
def edit_nieruchomosc_pok(request, id):
	
	nieruchomosc = get_object_or_404(Nieruchomosc, id=id)
	
	if request.method == 'POST':
		nieruchomosc_form = NieruchomoscEditForm(instance=nieruchomosc, data=request.POST, files=request.FILES)
        
		if  nieruchomosc_form.is_valid():
			cd = nieruchomosc_form.cleaned_data
			nieruchomosc = nieruchomosc_form.save(commit=False)
			nieruchomosc.user = request.user
			nieruchomosc.save()
						
			messages.success(request, 'Uaktualnienie profilu '\
										'zakończyło się sukcesem.')
			return redirect('realestate:editpokoje', id=nieruchomosc.id)					
									
		else:
			messages.error(request, 'Wystąpił błąd podczas uaktualniania profilu.')
		
		
						
	else:
		nieruchomosc_form = NieruchomoscEditForm(instance=nieruchomosc)
												
	return render(request,
					'realestate/client/editnieruchomoscpok.html',
						{'nieruchomosc': nieruchomosc, 'nieruchomosc_form': nieruchomosc_form})
						
						
						
@login_required	
def edit_nieruchomosc_gar(request, id):
	
	nieruchomosc = get_object_or_404(Nieruchomosc, id=id)
	
	if request.method == 'POST':
		nieruchomosc_form = NieruchomoscEditForm(instance=nieruchomosc, data=request.POST, files=request.FILES)
        
		if  nieruchomosc_form.is_valid():
			cd = nieruchomosc_form.cleaned_data
			nieruchomosc = nieruchomosc_form.save(commit=False)
			nieruchomosc.user = request.user
			nieruchomosc.save()
						
			messages.success(request, 'Uaktualnienie profilu '\
										'zakończyło się sukcesem.')
			return redirect('realestate:editgarage', id=nieruchomosc.id)					
									
		else:
			messages.error(request, 'Wystąpił błąd podczas uaktualniania profilu.')
		
		
						
	else:
		nieruchomosc_form = NieruchomoscEditForm(instance=nieruchomosc)
												
	return render(request,
					'realestate/client/editnieruchomoscpok.html',
						{'nieruchomosc': nieruchomosc, 'nieruchomosc_form': nieruchomosc_form})


						


@login_required	
def edit_nieruchomosc_kom(request, id):
	
	nieruchomosc = get_object_or_404(Nieruchomosc, id=id)
	
	if request.method == 'POST':
		nieruchomosc_form = NieruchomoscEditForm(instance=nieruchomosc, data=request.POST, files=request.FILES)
        
		if  nieruchomosc_form.is_valid():
			cd = nieruchomosc_form.cleaned_data
			nieruchomosc = nieruchomosc_form.save(commit=False)
			nieruchomosc.user = request.user
			nieruchomosc.save()
						
			messages.success(request, 'Uaktualnienie profilu '\
										'zakończyło się sukcesem.')
			return redirect('realestate:editkomercyjne', id=nieruchomosc.id)					
									
		else:
			messages.error(request, 'Wystąpił błąd podczas uaktualniania profilu.')
		
		
						
	else:
		nieruchomosc_form = NieruchomoscEditForm(instance=nieruchomosc)
												
	return render(request,
					'realestate/client/editnieruchomosckom.html',
						{'nieruchomosc': nieruchomosc, 'nieruchomosc_form': nieruchomosc_form})
						
						
						
						
#@login_required	
#def edit_nieruchomosc_dew(request, id):
	
	#nieruchomosc = get_object_or_404(Nieruchomosc, id=id)
	
	#if request.method == 'POST':
		#nieruchomosc_form = NieruchomoscEditForm(instance=nieruchomosc, data=request.POST, files=request.FILES)
        
		#if  nieruchomosc_form.is_valid():
			#cd = nieruchomosc_form.cleaned_data
			#nieruchomosc = nieruchomosc_form.save(commit=False)
			#nieruchomosc.user = request.user
			#nieruchomosc.save()
						
			#messages.success(request, 'Uaktualnienie profilu '\
										#'zakończyło się sukcesem.')
			#return redirect('realestate:editdeweloper', id=nieruchomosc.id)					
									
		#else:
			#messages.error(request, 'Wystąpił błąd podczas uaktualniania profilu.')
		
		
						
	#else:
		#nieruchomosc_form = NieruchomoscEditForm(instance=nieruchomosc)
												
	#return render(request,
					#'realestate/client/editnieruchomoscdew.html',
						#{'nieruchomosc': nieruchomosc, 'nieruchomosc_form': nieruchomosc_form})
						
					
@login_required					
def edit_dzialki(request, id):
	
	nieruchomosc = get_object_or_404(Nieruchomosc, id=id)
	dzialki = get_object_or_404(Dzialki, nieruchomosc=nieruchomosc)
	if request.method == 'POST':
		dzialki_form = DzialkiEditForm(instance=dzialki, data=request.POST, files=request.FILES)
        
		if  dzialki_form.is_valid():
			cd = dzialki_form.cleaned_data
			dzialka = dzialki_form.save(commit=False)
			dzialka.save()
			
						
			messages.success(request, 'Uaktualnienie profilu '\
										'zakończyło się sukcesem.')
			
			
		else:
			messages.error(request, 'Wystąpił błąd podczas uaktualniania profilu.')
	else:
		dzialki_form = DzialkiEditForm(instance=dzialki)
												
	return render(request,
					'realestate/client/editdzialki.html',
					{'nieruchomosc': nieruchomosc, 'dzialki': dzialki, 'dzialki_form': dzialki_form})
					


@login_required					
def edit_domy(request, id):
	
	nieruchomosc = get_object_or_404(Nieruchomosc, id=id)
	domy = get_object_or_404(Domy, nieruchomosc=nieruchomosc)
	if request.method == 'POST':
		domy_form = DomyEditForm(instance=domy, data=request.POST, files=request.FILES)
        
		if  domy_form.is_valid():
			cd = domy_form.cleaned_data
			dom = domy_form.save(commit=False)
			dom.save()
			
			messages.success(request, 'Uaktualnienie profilu '\
										'zakończyło się sukcesem.')
		else:
			messages.error(request, 'Wystąpił błąd podczas uaktualniania profilu.')
	else:
		domy_form = DomyEditForm(instance=domy)
												
	return render(request,
					'realestate/client/editdomy.html',
					{'nieruchomosc': nieruchomosc, 'domy': domy, 'domy_form': domy_form})
					
					

					
@login_required
def edit_mieszkania(request, id):
	nieruchomosc = get_object_or_404(Nieruchomosc, id=id)
	mieszkania = get_object_or_404(Mieszkania, nieruchomosc=nieruchomosc)
	if request.method == 'POST':
		
		mieszkania_form = MieszkaniaEditForm(instance=mieszkania, data=request.POST, files=request.FILES)
        
		if  mieszkania_form.is_valid():
			cd = mieszkania_form.cleaned_data
			mieszkanie = mieszkania_form.save(commit=False)
			mieszkanie.save()
			
			messages.success(request, 'Uaktualnienie profilu '\
										'zakończyło się sukcesem.')
		else:
			messages.error(request, 'Wystąpił błąd podczas uaktualniania profilu.')
	else:
		mieszkania_form = MieszkaniaEditForm(instance=mieszkania)
												
	return render(request,
					'realestate/client/editmieszkania.html',
					{'nieruchomosc': nieruchomosc, 'mieszkania_form': mieszkania_form})
					
					
@login_required
def edit_pokoje(request, id):
	nieruchomosc = get_object_or_404(Nieruchomosc, id=id)
	pokoje = get_object_or_404(Pokoje, nieruchomosc=nieruchomosc)
	if request.method == 'POST':
		
		pokoje_form = PokojeEditForm(instance=pokoje, data=request.POST, files=request.FILES)
        
		if  pokoje_form.is_valid():
			cd = pokoje_form.cleaned_data
			pokoj = pokoje_form.save(commit=False)
			pokoj.save()
			
			messages.success(request, 'Uaktualnienie profilu '\
										'zakończyło się sukcesem.')
		else:
			messages.error(request, 'Wystąpił błąd podczas uaktualniania profilu.')
	else:
		pokoje_form = PokojeEditForm(instance=pokoje)
												
	return render(request,
					'realestate/client/editpokoje.html',
					{'nieruchomosc': nieruchomosc, 'pokoje_form': pokoje_form})
					
					
					
					
@login_required
def edit_garage(request, id):
	nieruchomosc = get_object_or_404(Nieruchomosc, id=id)
	garage = get_object_or_404(Garage, nieruchomosc=nieruchomosc)
	if request.method == 'POST':
		
		garage_form = GarageEditForm(instance=garage, data=request.POST, files=request.FILES)
        
		if  garage_form.is_valid():
			cd = garage_form.cleaned_data
			garage = garage_form.save(commit=False)
			garage.save()
			
			messages.success(request, 'Uaktualnienie profilu '\
										'zakończyło się sukcesem.')
		else:
			messages.error(request, 'Wystąpił błąd podczas uaktualniania profilu.')
	else:
		garage_form = GarageEditForm(instance=garage)
												
	return render(request,
					'realestate/client/editgarage.html',
					{'nieruchomosc': nieruchomosc, 'garage_form': garage_form})

					
					
					
@login_required
def edit_komercyjne(request, id):
	nieruchomosc = get_object_or_404(Nieruchomosc, id=id)
	komercyjne = get_object_or_404(Komercyjne, nieruchomosc=nieruchomosc)
	if request.method == 'POST':
		
		komercyjne_form = KomercyjneEditForm(instance=komercyjne, data=request.POST, files=request.FILES)
        
		if  komercyjne_form.is_valid():
			cd = komercyjne_form.cleaned_data
			komercyjne = komercyjne_form.save(commit=False)
			komercyjne.save()
			
			messages.success(request, 'Uaktualnienie profilu '\
										'zakończyło się sukcesem.')
		else:
			messages.error(request, 'Wystąpił błąd podczas uaktualniania profilu.')
	else:
		komercyjne_form = KomercyjneEditForm(instance=komercyjne)
												
	return render(request,
					'realestate/client/editkomercyjne.html',
					{'nieruchomosc': nieruchomosc, 'komercyjne_form': komercyjne_form})
					
					
@login_required
def przeglad(request, nieruchomosc_id=None):

	nieruchomosc = None
	nieruchomoscs = Nieruchomosc.objects.filter(user=request.user)
	
	
												
	return render(request,
					'realestate/client/przeglad.html',
					{'nieruchomoscs': nieruchomoscs})
