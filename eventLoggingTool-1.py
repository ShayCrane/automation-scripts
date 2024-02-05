#!/usr/bin/python3


# Script Name: Event Logging Tool Pt. 1 of 3
# Author: Shay Crane
# Date of last revision: 11/07/2022
# Purpose:  incorporate logging capabilities into 
#               one of my previously built scripts. 

# examples of the types of errors detectable by logging library:
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')


# import libraries
import logging
import datetime
import time 
import os


# configuration of logging file, minimum level to induce output, and format
logging.basicConfig(filename="ping-error.log", level=logging.INFO, format="%(levelname)s:%(asctime)s:%(message)s")


# defining function
def check_ping():
    # changed IP address from original script 
    # to one that does not exist on my network
    # to induce an error to print to the log file
    print(os.system('ping -c 1 10.0.0.11 '))
    return 

ping_status=check_ping()
# infinite while loop
try: 
    while True:
        ping_status=0 
        logging.info(ping_status)
        print("Current date and time: ")
        now=datetime.datetime.now()
        print(str((now)))
        print("Start : %s" % time.ctime()) 
        time.sleep(2)
        print("End : %s" % time.ctime())
        
except: 
        logging.error('Error sending ICMP, bad IP address.') # error message regarding bad IP address



# misc output notes for bash script output to file:
# stdin - 0
# standard input stream 
#    accepts text as its input. 
# 
# stdout - 1
# Text output from the command to the shell 
#    is delivered via the stdout (standard out) stream. 
# 
# stderr - 2
# Error messages from the command 
#    are sent through the stderr (standard error) stream.

# Streams in Linux are treated as though they were files.

# importing libraries

