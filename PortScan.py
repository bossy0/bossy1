#!/use/bin/env python

import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet P1NK PORT TARAMA")
print("""   
P1NK P4NTH3R PORT TARAMA Aracina Hos Geldiniz.

1) H1ZL1 T4R4M4
2) S3RV1S V3 V3RS1Y0N B1LG1S1
3) 1SL3T1M S1ST3M1 B1LG1S1

""")

islemno = raw_input("1SL3M NUM4R4S1 G1R1N:")

if(islemno=="1"):
	hedefip = raw_input("H3D3F 1P G1R1N:")
	os.system("nmap " + hedefip)
elif(islemno=="2"):
	hedefip = raw_input("H3D3F 1P G1R1N:")
	os.system("nmap -sS -sV " + hedefip)
elif(islemno=="3"):
	hedefip = raw_input("H3D3F 1P G1R1N:")
	os.system("nmap -0 " + hedefip)
else:
	print("H4C1 0RD4 B1S3Y YOK :( hatali secim. ")
