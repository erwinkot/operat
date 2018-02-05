$(document).ready(function() {
	var imgs = [];
	$('#slider img').each(function() {
		var imgSrc = $(this).attr('src');
		var newPhoto = new Image();
		newPhoto.src = imgSrc;
		$(this).click(function() {
			//evt.preventDefault();
			$('#photo').attr('src', newPhoto.src);
		});
					
	});
	
	$('#slider img').each(function() {
		var srcImg = $(this).attr('src');
		imgs.push(srcImg);
		//$('#hul').append(srcImg + ',' + ' ');
		
	});
	
	var monka = imgs[0];
	$('#photo').attr('src', monka);
	
	
	$('#spdiv').click(function() {
			var oldPhoto = $('#photo').attr('src');
			if (oldPhoto.indexOf('http://') !=-1) {
				var porka = oldPhoto.slice(21);
			} else {
				var porka = oldPhoto
			}
			for  (var i=0; i<imgs.length; i++) {
				var srcBieg = imgs[i];
				if (srcBieg == porka) {
					srcUst = imgs[i+1];
					$('#photo').attr('src', srcUst);
				}
			} 
		
	});
	
	$('#sldiv').click(function() {
		
		var oldsPhoto = $('#photo').attr('src');
		if (oldsPhoto.indexOf('http://') !=-1) {
			var porkas = oldsPhoto.slice(21);
		} else {
			var porkas = oldsPhoto
		}
		for  (var i=0; i<imgs.length; i++) {
			var srcBiegs = imgs[i];
			if (srcBiegs == porkas) {
				srcUsts = imgs[i-1];
				$('#photo').attr('src', srcUsts);
			}
		} 
		
	});
	
});
		




window.onload = ustawWybor;

function ustawWybor() {
	var listMedia = ["prąd", "gaz", "woda", "kanalizacja", "szambo", "oczyszczalnia ścieków", "telefon"];
	var listOtocz = ["las", "góry", "jezioro", "morze", "teren otwarty"];
	//var listZabezp = ["teren zamknięty", "monitoring", "alarm", "drzwi anty-włamaniowe", "rolety", "domofon/wideofon"];
	//var listDodatki = ["piwnice", "garaż", "poddasze", "basen", "klimatyzacja"];
	//var listOgrzew = ["miejskie", "gazowe", "olejowe", "elektryczne", "węglowe", "piece kaflowe", "kominkowe", "kolektor słoneczny", "pompa ciepła", "biomasa"];
	//var listMieDodatki = ["piwnica", "garaż", "parking", "winda", "klimatyzacja", "balkon", "taras", "ogródek"];
	
	for (var i = 0; i < listMedia.length; i++) {
		var media = listMedia[i];
		var id = "dommedia" + i;
		var li = document.getElementById(id);
		var dups = li.textContent;
		if (dups == "True") {
			li.innerHTML = media;
		} else {
			li.remove();
		}
	}
	
	for (var i = 0; i < listOtocz.length; i++) {
		var otocz = listOtocz[i];
		var id = "domotocz" + i;
		var li = document.getElementById(id);
		var dups = li.textContent;
		if (dups == "True") {
			li.innerHTML = otocz;
		} else {
			li.remove();
		}
	}
	
}


