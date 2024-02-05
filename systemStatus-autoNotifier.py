# !/usr/bin/python3


# Script Name: System Status Auto-Notifier (email notifications)
# Author: Shay Crane
# Date of last revision: 10/05/2022
# Purpose: an uptime sensor tool that checks systems are responding by adding an automated email feature that notifies you of status changes.

# The script must:

# Ask the user for an email address and password to use for sending notifications.
# Send an email to the administrator if a host status changes (from “up” to “down” or “down” to “up”).
# Clearly indicate in the message which host status changed, the status before and after, and a timestamp of the event.

# The function below ("check_ping") can be credited to https://github.com/wwparker, who sent it to me to demonstrate 
# a consice version of the script that I submitted for class 02. 

from email.policy import SMTP
import smtplib
import ssl

user_email = input("What is your email? ")
user_key = input("Enter your password: ")
location = input("Enter the IP address you wish to monitor: ")

def check_ping():
    import os
    return os.system(ping -c 1 location)

# gives instructions on what server to talk to 
# requests information required to send the status 
# message to the email address
smtplib.SMTP_SSL(SMTP.gmail.com, 465)
smtplib.ehlo()
smtplib.login(user_email.user_key)
smtplib.sendmail('shays-bot@shaybot', user_email, msg)
smtplib.quit()

# from email.message import EmailMessage

# infinite loop
import datetime
import time 
while True:
        now = datetime.datetime.now()
        status = check_ping(location)
        if status == 0:
                print(f'{now} Network active to {location}')
        else:
                print(f'{now} Ping failed to {location}')
        time.sleep(2)


