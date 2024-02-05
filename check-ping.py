#!/usr/bin/python3


# Script Name: Check Ping
# Author: Shay Crane
# Date of last revision: 10/04/2022
# Purpose: a Python script that creates an uptime sensor tool and uses ICMP packets to evaluate if hosts on the LAN are up or down.

# The script must:

# Transmit a single ICMP (ping) packet to a specific IP every two seconds.
# Evaluate the response as either success or failure.
# Assign success or failure to a status variable.
# For every ICMP transmission attempted, print the status variable along with a comprehensive timestamp and destination IP tested.
# Example output: 2020-10-05 17:57:57.510261 Network Active to 8.8.8.8

# I found some helpful advice at the following link:  
# https://stackoverflow.com/questions/26468640/python-function-to-test-ping

# from pythonping import ping 

# importing libraries
import datetime
import time 
import os



# defining function
def check_ping():
    print(os.system('ping -c 1 10.0.0.227 '))
    return 

ping_status = check_ping()
# infinite while loop
while True:
    ping_status = 0 
    print("Current date and time: ")
    now = datetime.datetime.now()
    print(str((now)))
    print("Start : %s" % time.ctime()) 
    time.sleep(2)
    print("End : %s" % time.ctime())
       

# notes from a developer friend not associated with code fellows for reference in posterity:
# to get the status from the check_ping function, you need to do status = check_ping(). Also the check_ping function needs to return 
# the results of the os.system function call (which is what the return os.system does). you could also do ping_results = os.system 
# and then return ping_results. That one of the things that you are missing. You also need to output a string that indicates if the ping passed/failed. 
# The os.system call returns the value of 0 on success and a non-zero error code if it failed. ping returns >0 if it can't ping.