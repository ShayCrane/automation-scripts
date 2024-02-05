#!/usr/bin/python3


# Script Name: Signature-based Malware Detection Pt. 1 of 3
# Author: Shay Crane
# Date of last revision: 11/14/2022
# Purpose: print to screen results of file directory search
#               by writing a script that will work on both Ubuntu and Windows OS.



from sys import platform
import os
from os.path import join



# Define functions:

# Determines OS and then runs the associated function:
def lookupfile():
   print("Checking OS...")
   print(platform)
   if platform=="Linux":
       linuxsearch()
   elif platform=="Windows":
       print("The OS is: ")
       print(platform)
       windowssearch()
   else:
       choice=input("Cannot detect OS.\nEnter 1 for any Linux distribution:\nEnter 2 for any Windows version:\nOr to exit, enter 3: ")
       if choice=="1":
           linuxsearch()
       elif choice=="2":
           windowssearch()
       else:
           print("Exiting...")
           quit


# Linux search
def linuxsearch():
   filename=input("File Search...\nEnter name of file:  ")
   filepath=input("Enter the file path in which to search for ")
   fileschecked=0
   for root, dirs, files in os.walk(filepath):
       for file in files:
           fileschecked+=1
           if file==filename:
               print(str(fileschecked)+" files were searched, and your file was located at: "+root+"/"+filename)
               print("Raven is the BEST.")


# Windows search
def windowssearch():
   filename=input("File Search...\nEnter name of file:  ")
   filepath=input("Enter the file path in which to search for ")
   fileschecked=0
   for root, dirs, files in os.walk(filepath):
       for file in files:
           fileschecked+=1
           if file==filename:
               print(str(fileschecked)+" files were searched, and your file was located at: "+root+"/"+filename)
               print("Raven is the BEST.")

# Main
lookupfile()