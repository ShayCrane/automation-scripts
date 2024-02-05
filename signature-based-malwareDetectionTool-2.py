#!/usr/bin/python3


# Script Name: Signature-based Malware Detection Pt. 2 of 3
# Author: Shay Crane
# Date of last revision: 11/15/2022
# Purpose: continue development of your own basic antivirus tool in Python.
#               by generating a given file's hash. 

import sys
from sys import platform
import os, hashlib, time, datetime, math 
from os.path import join

    # menu options
# 1 - check os, search for file
# 2 - get file hashes for all files in a directory
def menu():
    print("Enter 1 to check operating system and search for a file; ")
    print("Enter 2 to get file hashes for all files in a given directory; or ")
    print("Enter 9 to exit. ")
    choice=input("Enter your choice: ")

    if choice=="1":
        lookupfile()
    elif choice=="2":
        hashdir()
    else: 
        sys.exit 


# Define functions:

# Determines OS and then runs the associated function:
def lookupfile():

    print("Checking OS...")
    print(platform)
    if platform==str("Linux"):
       linuxsearch()
    elif platform==str("Windows"):
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
           sys.exit


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
                menu()

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
                menu()


# timestamp function
def timestamps():
    timestamp=time.localtime()
    return str(timestamp)


# hashing function
# returns the SHA256 hash of the file passed into it
def hashfile(filename):
#    filename=input("Enter name of the file you wish to hash: ")
    filehash=hashlib.md5()
    with open(filename,"rb") as file:
        block=0
        # loops until the end of the file
        while block !=b'':
            block=file.read(1024)
            filehash.update(block)
            print(filehash)
    # returns the hex representation of the hash digest
        return filehash.hexdigest()

# substitute the file name as the parameter
# message=hashfile(str(filename))
# print(message)

# use os.walk to crawl through directories and print to the screen all the file hashes
def hashdir():
    dircount=0
    filecount=0
    dirpath=input("Enter absolute file path to the directory to be scanned: ")
    dirpath="/home/shannon/test-folder/capture.txt"
#   dirpath="C:\Users\Crane\Desktop\getfilename.txt"
    for (path,dirs,files) in os.walk(dirpath):
        print("Directory: {:s}".format(path))
        dircount+=1

        for file in files: 
            fstat=os.stat(os.path.join(path,file))

            if (fstat.st_size>1024*1024):
                filesize=math.cell(fstat.st_size/(1024*1024))
                unit=="HR"
            elif (fstat.st_size>1024):
                filesize=math.cell(fstat.st_size/1024)
                unit="KB"
            else: 
                filesize=fstat.st_size="B"

            filecount+=1
            filename=os.path.join(path,file)
            hashname=hashfile(filename)
            timestamp=timestamps()
            print(timestamp)
            print(" File Info: "+{file}+"\tsize: "+{str(filesize) + unit}+"\tpath: "+{str(filename)})
            print(filesize+unit)
            print(dirpath+"/"+filename)
            print("Hash: ")
            print(hashname())

    print("Total hashed files: {} "+ "from {} directories"+format(filecount,dircount))
    dircount=0
    filecount=0
    menu()


# Main
menu()
hashdir()


# Requirements
# Continue developing your Python malware detection tool.

# Alter your search code to recursively scan each file and folder 
#              in the user input directory path and print it to the screen.
#
#   For each file scanned within the scope of your search directory:
#       Generate the file’s MD5 hash using Hashlib.
#       Assign the MD5 hash to a variable.
#       Print the variable to the screen along with a timestamp, file name, file size, and complete (not symbolic) file path.
#   
# TIP: You may need to bring in additional Python modules to complete today’s objective.

# The script should be tested to execute successfully in Python3.

