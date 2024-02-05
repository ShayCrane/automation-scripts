#!/usr/bin/python3


# Script Name: Attack Tools Part 2 of 3
# Author: Shay Crane
# Date of last revision: 12/03/2022
# Purpose: Custom Nmap scanner using Python 
#   complete all to-dos



import nmap

scanner = nmap.PortScanner()

print("Nmap Automation Tool")
print("--------------------")

#### ip_addr = input("IP address to scan: ") ####
ip_addr = '127.0.0.1' 
print("The IP you entered is: ", ip_addr)
type(ip_addr)

resp = input("""\nSelect scan to execute:
                1) SYN ACK Scan
                2) UDP Scan
                3) Regular\n""") ### TODO: Select what your third scan type will be
print("You have selected option: ", resp)



### TODO: Prompt the user to type in a port range for this tool to scan

#### range = input("Enter port range for SYN ACK Scan: ") ####
range = '1-1024' 
if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())

elif resp == '2':
    ### TODO: Add missing code block here
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sU')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())

elif resp == '3':
    ### TODO: Add missing code block here
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr)
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())

elif resp >= '4':
    print("Please enter a valid option")