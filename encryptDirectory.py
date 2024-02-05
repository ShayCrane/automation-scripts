#!/usr/bin/python3


# Script Name: Encrypt Directory
# Author: Shay Crane
# Date of last revision: 10/11/2022
# Purpose: a Python script that encrypts a directory

# this script builds upon encryptFile.py 

# define functions that will be nested within the ask_user()
# function from the previous script


from fileinput import filename
import os.walk

def dir_encrypt():
    path = input("Encrypt a directory.  Enter the absolute path of the director: ")
    for dirpath, dirnames, filenames in os.walk(path):
        print('directory: '.format(dirpath))
        for file in filename
            filename = os.path.join(dirpath.file)
            recursive_en(filename)

def dir_decrypt():
    path = input("De-encrypt a directory.  Enter the absolute path of the directory: ")
    for dirpath, dirnames, filenames in os.walk(path):
        print('directory: '.format(dirpath))
        for file in filenames
            filename = os.path.join(dirpath.file)
            recursive_de(filename)
