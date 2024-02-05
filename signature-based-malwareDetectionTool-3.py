#!/usr/bin/python3


# Script Name: Web Application Fingerprinting Part 1 of 3
# Author: Shay Crane
# Date of last revision: 11/15/2022
# Purpose: In Python create a banner-grabbing (or service fingerprinting) script 
#               that executes from a Linux box, using Nmap, Netcat, and Telnet.


# import libraries
import socket
import sys
import time
import subprocess


# define functions:

# user menu
def menu():
    print("Welcome to the banner-grab utility.")
    userurl=input("Enter a URL or IP address to fingerprint: ")
    userport=input("Enter port number: ")
    print("Please choose from the following tools: ")
    print("1. Netcat\n2. Telnet\n3. Nmap\n4. Exit ")
    choice=input("Enter your choice: ")

    if choice=="1":
        netcat(userurl, userport)
    elif choice=="2":
        telnet(userurl, userport)
    elif choice=="3":
        nmap(userurl, userport)
    else: 
        sys.exit 

# netcat 
def netcat(userurl,userport):
    
# attempts to establish connection
    
    # sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sock.connect((userurl,int(userport)))
    terminalscript=("nc "+userurl+" "+userport+" -v")
    subprocess.run.check_output(terminalscript)

    # sock.sendall(subprocess.run.encode(bashscript))

    # while True:
    #     data=sock.recv(1024)
    #     res+=data.decode()
    #     print(res)
    #     sock.closed()
    #     break

# telnet

# def telnetgrab(userurl,userport):
#     subproc



# nmapgrab 

# def nmapgrab():
#     script
        


# main
menu()




# For this lab you’ll need to develop and test your Python script from a Linux VM with the tools Nmap, Netcat, and Telnet installed. Generally speaking, Kali Linux is the recommendation for this challenge.

# In Python create a script that executes from a Linux box to perform the following:

# Prompts the user to type a URL or IP address.
# Prompts the user to type a port number.

# Performs banner grabbing using netcat against the target address at the target port; 
#   prints the results to the screen then moves on to the step below.

# Performs banner grabbing using telnet against the target address at the target port; 
#   prints the results to the screen then moves on to the step below.

# Performs banner grabbing using Nmap against the target address of all well-known ports; 
#   prints the results to the screen.

# Be sure to only target approved URLs like scanme.nmap.org or web servers you own.

# Stretch Goals (Optional Objectives)
# Use additional banner grabbing techniques, such as WhatWeb and CURL, to gather as much information as possible about a target web server.





