
window.onload = ustawWybor;

function ustawWybor() {
	var listMedia = ["prąd", "gaz", "woda", "kanalizacja", "szambo", "oczyszczalnia ścieków", "telefon", "internet", "telewizja kablowa"];
	var listOtocz = ["las", "góry", "jezioro", "morze", "teren otwarty"];
	var listZabezp = ["teren zamknięty", "monitoring", "alarm", "drzwi anty-włamaniowe", "rolety", "domofon/wideofon"];
	var listDodatki = ["piwnice", "garaż", "poddasze", "basen", "klimatyzacja"];
	var listOgrzew = ["miejskie", "gazowe", "olejowe", "elektryczne", "węglowe", "piece kaflowe", "kominkowe", "kolektor słoneczny", "pompa ciepła", "biomasa"];
	var listMieDodatki = ["piwnica", "garaż", "parking", "winda", "klimatyzacja", "balkon", "taras", "ogródek"];
	
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
	
	for (var i = 0; i < listZabezp.length; i++) {
		var zabezp = listZabezp[i];
		var id = "domzabezp" + i;
		var li = document.getElementById(id);
		var dups = li.textContent;
		if (dups == "True") {
			li.innerHTML = zabezp;
		} else {
			li.remove();
		}
	}
	
	for (var i = 0; i < listDodatki.length; i++) {
		var dodatki = listDodatki[i];
		var id = "domdodatki" + i;
		var li = document.getElementById(id);
		var dups = li.textContent;
		if (dups == "True") {
			li.innerHTML = dodatki;
		} else {
			li.remove();
		}
	}
	
	for (var i = 0; i < listOgrzew.length; i++) {
		var ogrzew = listOgrzew[i];
		var id = "domogrzew" + i;
		var li = document.getElementById(id);
		var dups = li.textContent;
		if (dups == "True") {
			li.innerHTML = ogrzew;
		} else {
			li.remove();
		}
	}
	
	for (var i = 0; i < listMieDodatki.length; i++) {
		var dodatkimie = listMieDodatki[i];
		var id = "miedodatki" + i;
		var li = document.getElementById(id);
		var dupsik = li.textContent;
		if (dupsik == "True") {
			li.innerHTML = dodatkimie;
		} else {
			li.remove();
		}
	}	
}

	


