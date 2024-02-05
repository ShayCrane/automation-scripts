#!/usr/bin/python3


# Script Name: Event Logging Tool Pt. 2 of 3
# Author: Shay Crane
# Date of last revision: 11/08/2022
# Purpose:  add log rotation feature based on size 
#               to the Python script created in pt. 1 (class26.py). 



# import libraries
import logging
import datetime
import time 
import os

from logging.handlers import RotatingFileHandler



# configuration of logging file, minimum level to induce output, and format
# logging.basicConfig(filename="ping-error.log", level=logging.INFO, format="%(levelname)s:%(asctime)s:%(message)s")


# defining function
def check_ping():
    print(os.system('ping -c 1 10.0.0.164 '))
    return 
# infinite while loop

def rotatelog():
    logger=logging.getLogger("Rotating Log - Size")
    logger.setLevel(logging.INFO)
    
# adds a rotating handler for the log file
    handler=RotatingFileHandler("test-logs-bytes.log", maxBytes=100, backupCount=5)
    formatter=logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")

# set handler and formatter for log file
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    print("Logging started.")

    for i in range(200):
        logger.info("Log line %s" % i)
        logmsg="Log Level: Warning "
        logmsg+=str(i)
        logger.warning(logmsg)
        logger.info("Log Level: Information ")
        logger.critical("Log Level: CRITICAL")
        logger.error("Log Level: Error ")
        time.sleep(1.5)

ping_status=check_ping()
check_ping()
try: 
    while True:
        ping_status=0 
        #logging.info(ping_status)
        print("Current date and time: ")
        now=datetime.datetime.now()
        print(str((now)))
        print("Start : %s" % time.ctime()) 
        time.sleep(2)
        print("End : %s" % time.ctime())
except: 
# name logger, set log level for printing to log files
    rotatelog(ping_status)
