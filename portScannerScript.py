#!/usr/bin/python3

# Script Name: Create a Port Scanner
# Author: Shay Crane
# Date of last revision: 12/05/2022
# Purpose: Complete the Port Scanner Script and its to-dos
#   The socket python module grants us access to low level 
#       networking interface operations directly from the Python 3 script.



import socket

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = 10 #Set a timeout value here.
sockmod.settimeout(timeout)

hostip = input("Enter host IP address: ") # Collect a host IP from the user.
portno = input("Enter port number: ") #  Collect a port number from the user, then convert it to an integer data type.
int(portno)
#hostip = "10.0.0.164"
#portno = "3389"
def portScanner(portno):
    if sockmod.connect((hostip, portno)): 
        # Replace "FUNCTION" with the appropriate socket.function call as found in the [socket docs]
        print("Port closed")
    else:
        print("Port open")

portScanner(portno)