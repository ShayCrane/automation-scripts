#!/usr/bin/python3


# Script Name: Event Logging Tool Pt. 3 of 3
# Author: Shay Crane
# Date of last revision: 11/09/2022
# Purpose:  add log handler feature to script built in parts 1 & 2. 




# import libraries
import logging
import datetime
import time 
import os

from logging.handlers import RotatingFileHandler





# import libraries
import logging
import datetime
import time 
import os

from logging.handlers import RotatingFileHandler



# create logger
logger=logging.getLogger("my_logger")

# create log handlers
s_handler=logging.StreamHandler()
f_handler=logging.FileHandler("file.log")
s_handler.setLevel(logging.INFO)
f_handler.setLevel(logging.INFO)

# Create formatters and add it to handlers
s_format=logging.Formatter("%(name)s - %(levelname)s - %(message)s")
f_format=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
s_handler.setFormatter(s_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(s_handler)
logger.addHandler(f_handler)

logger.warning("This is a warning")
logger.error("This is an error")


# defining function
def check_ping():
    print(os.system("ping -c 1 10.0.0.164 "))
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
check_ping(rotatelog())
#try: 
while True:
    ping_status=0 
    #logging.info(ping_status)
    print("Current date and time: ")
    now=datetime.datetime.now()
    print(str((now)))
    print("Start : %s" % time.ctime()) 
    time.sleep(2)
    print("End : %s" % time.ctime())

# except:




