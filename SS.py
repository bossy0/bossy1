#!/usr/bin/python
#-*- coding: utf-8 -*-

import mechanize,sys,re,HTMLParser,urllib
from bs4 import BeautifulSoup
h = HTMLParser.HTMLParser()
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)')]
def giris():
	try:
		if sys.argv[1] == "-d" and sys.argv[3] == "-s" and sys.argv[5] == "-f":
			dork = sys.argv[2]
			sayfa_sayisi = sys.argv[4]
			dosya_ismi = sys.argv[6]
			arama(dork,sayfa_sayisi,dosya_ismi)
		else:
			print "    >> python googler.py -d /admin.php -s 10 -f cikti.txt \n\n    -d = dork \n    -s = Sayfa sayısı\n    -f = kaydedilcek dosya ismi"
	except:
		print "    >> python googler.py -d /admin.php -s 10 -f cikti.txt \n\n    -d = dork \n    -s = Sayfa sayısı\n    -f = kaydedilcek dosya ismi"
def arama(dork,sayfa_sayisi,dosya_ismi):
	dosya = open(dosya_ismi,"a")
	dorks=urllib.quote(dork)
	for i in range(0,int(sayfa_sayisi)):
		ss = i+1
		url = "https://www.google.com.tr/search?q=%s&noj=1&start=%s0" %(dorks,i)
		print "[+] %s. Sayfa yazildi.." %ss
		a = br.open(url)
		kodlar = a.read()
		kazan = BeautifulSoup(kodlar)
		ayiklama = kazan.find_all('h3')
		for i in ayiklama:
			ayiklama1 = i.find_all('a')
			#print ayiklama1
			for a in ayiklama1:
				hedef = a.get('href')
				l = hedef.lstrip('/url?q=')
				f = re.findall('(.*?)&sa',l)
				for hedef in f:
					asd = h.unescape(urllib.unquote(hedef))
					dosya.write(asd+"\n")
					#print hedef

	dosya.close()
	print "\n[-] İşlem bitmiştir.. "
giris()
