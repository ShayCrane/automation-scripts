#!/usr/bin/python3


# Script Name: Scapy Pt. 2
# Author: Shay Crane
# Date of last revision: 10/18/2022
# Purpose: Add feature to the Network Security Tool created in Scapy Pt. 1 (scapy1-networkSecurityTool.py) 
#          that gives user all IP addresseses within a given CIDR block 


#import libraries
import sys  
from sys import flags
from tkinter import Menu
from scapy.all import ICMP, IP, sr1, sr, TCP
import random
from ipaddress import IPv4Network


#define function to display menu
def display_menu():
    print("Choose your network security tool: ")
    print("1. TCP Port Range Scanner", "2. ICMP Ping Sweeper", "3. Exit")
    sectool=input("Enter the # of your chosen Network Scan Tool: ")
    if sectool=="1":
        tcp_scan()
    elif sectool=="2":
        ping_sweep()
    elif sectool=="3":
        sys.exit("Exiting the program... Exited.")
    else:
        print("Invalid input. Please try again. ") 
        display_menu()

#define function to return to menu or exit
def return_menu():
    mymenu=input("Return to main menu? yes or no:  ")
    if mymenu=="yes":
        display_menu()
    elif mymenu=="no":
        sys.exit
    else: 
        print("Invalid input. Please try again. ") 
        display_menu() 

#define tcp scan function
def tcp_scan():
    host=input("Enter an IP address or scanme.nmap.org: ")
    port_range=[22,23,80,443,3389]
    for dst_port in port_range:
        src_port=random.randint(1025,65534)
    response=sr1(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=1,verbose=0,) # ping and scan
    print(response)
    if response==None: 
        print(str(host)+":"+str(dst_port)) 
        print("was silently dropped.")
        return_menu()
    elif(response.haslayer(TCP)): 
        if(response.getlayer(TCP).flags == 0x12): 
            print(str(host)+":"+str(dst_port))
            print("is open.")
            return_menu()
        if(response.getlayer(TCP).flags == 0x14):
            print(str(host)+":"+str(dst_port))
            print("is closed.")
            return_menu()
    else: 
        print(host+":"+dst_port)
        print("was silently dropped")
        return_menu()
    
    
#define ping sweep function: ICMP Ping Sweep Tool
def ping_sweep():
    network=input("In CIDR notation, enter the IP address you wish to scan: ")
    ip_list=IPv4Network(network)
    print(ip_list)

    for host in ip_list:
        print(host)
        live_count=0
        choice="y"

    while choice=="y":
        choice=input("Display number of IP addresses in the CIDR block? yes or no: ")
        if choice=="yes":
            live_count+=1
            print("Total number of IP addresses in your chosen CIDR block:  "+str(live_count))
            return_menu()
        else: 
            return_menu()


#main 
display_menu()





