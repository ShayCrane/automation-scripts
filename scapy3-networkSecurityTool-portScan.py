#!/usr/bin/python3


# Script Name: Scapy Pt. 3
# Author: Shay Crane
# Date of last revision: 10/19/2022
# Purpose: ping a given IP address; if host exists, 
#            scan its ports, and determine if any of its ports are open



#import libraries
import random
from typing import List 
from sys import flags
from scapy.all import ICMP, IP, sr1, sr, TCP
from ipaddress import IPv4Network

host=input("Enter IP address-- or scanme.nmap.org: ")
port_range=[22,23,80,443,3389]


#define function to ping a given IP address and print status to screen
def ping_fun(host):
    response=sr1(IP(dst=str(host))/ICMP(),timeout=1,verbose=0)
    if response==None: 
        print(f"{host} is down or not responding. ") 
    elif (
        int(response.getlayer(ICMP).type)==3 and
        int(response.getlayer(ICMP).code) in [1,2,3,9,10,13]
    ):
        print(f"{host} is blocking ICMP traffic. ")
    else: 
        print(f"{host} is responding. ")
        port_scan(host,port_range)


#define function to scan for open ports and print to screen port status
def port_scan(host,port_range):
    for dst_port in port_range:
        src_port=random.randint(1025,65534)
        response=sr1(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=1,verbose=0,) 
    if response is None: 
        print(f"{host}:{dst_port} was silently dropped (or filtered). ") 
    elif (response.haslayer(TCP)): 
        if (response.getlayer(TCP).flags==0x12): 
            send_rst=sr(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags='R'),timeout=1,verbose=0)
            print(f"{host}:{dst_port} is open. ")
        elif (response.getlayer(TCP).flags==0x14):
            print(f"{host}:{dst_port} is closed.")
    elif (response.haslayer(ICMP)):
        if (
            int(response.getlayer(ICMP).type)==3 and
            int(response.getlayer(ICMP).code) in [1,2,3,9,10,13]
        ):
            print(f"{host}:{dst_port} was silently dropped (or filtered).")

#main
ping_fun(host)

#end

