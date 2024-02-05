#!/usr/bin/python3


# Script Name: Automated Brute Force Wordlist Tool Pt. 1
# Author: Shay Crane
# Date of last revision: 10/24/2022
# Purpose:  begin the development of a custom tool that performs
#           brute force attacks to better understand the types of
#           automation employed by malicious hackers. 



#import libraries
import time
import getpass
import sys

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



#iterator
def iterator():
    path=input("Enter your dictionary's filepath:\n")
    file=open(path)
    line=file.readline()

    while line:
        line=line.rstrip()
        word=line
        print(word)
        time.sleep(1)
        line=file.readline()
    file.close()
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
            print("{pwrd} was not found in your wordlist")
            menu()

#main
#call menu function
menu()

