#!/usr/bin/python3


# Script Name: Encrypt a File
# Author: Shay Crane
# Date of last revision: 10/10/2022; 10/11/2022; 02/03/2023
# Purpose: a Python script that encrypts a single file



import os
import sys
import getpass
from cryptography.fernet import Fernet

# Get the file to encrypt
file_name = input("Enter the file to encrypt: ")

# Generate a key
key = Fernet.generate_key()

# Open the file
with open(file_name, 'rb') as f:
    data = f.read()

# Encrypt the file
fernet = Fernet(key)
encrypted_data = fernet.encrypt(data)

# Save the encrypted file
encrypted_file_name = file_name + ".encrypted"
with open(encrypted_file_name, 'wb') as f:
    f.write(encrypted_data)

# Save the encryption key
key_file_name = file_name + ".key"
with open(key_file_name, 'wb') as f:
    f.write(key)

# Print success message
print("File successfully encrypted and key saved to file.")




# ------------------


# Older version of script


# I used the following site for guidance in writing this script:
# https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python

# # This script is not complete.

# # import libraries

# from cryptography.fernet import Fernet # symmetric authenticated cryptography library
# import os.path 
# from os.path import exists
# import sys


# # define funciton: loads the key from the current directory named 'key.key'
# def load_key():
#     return open("key.key", "rb").read()
# #declare variables
# key = load_key()
# f = Fernet(key)

# # generates a key, saves it into a file
# def write_key():
#     key = Fernet.generate_key()
#     with open(key.key, wb) as key_file: 
#         key_file.write(key)

# # 1 define function: encrypts file contents
# def encrypt_file():
#     filepath = input("Enter path of file to be encrypted: ")
#     with open(filepath, "rb") as file:  #reads all file data
#         filedata = file.read()
#     encrypted_data = f.encrypt(filedata) 
#     with open(filepath, "wb") as encrypted_file: #writes encrypted file
#         encrypted_file.write(encrypted_data)

# # 2 define function: given a filename and key (bytes), 
# # it decrypts the file and prints it to screen(?)
# def decrypt_file(): 
#         # key = load_key()
#         # print("Key is " + str(key.decode('utf-8')))
#     filepath = input("Enter path of file to be decrypted: ")
#     with open(filepath, "rb") as file: 
#         encrypted_data = file.read()
#         decrypted_data = f.decrypt(encrypted_data)
#     with open(filepath, "wb") as decrypted_file: 
#         decrypted_file.write(decrypted_data)
    
# # 3 define function: encrypts a msg
# def encrypt_message():
#     message = input("Enter message you want me to encrypt: ").encode()
#     print("Plaintext is: " + str(message.decode('utf-8')))
#     encrypted_msg = f.encrypt(message)
#     print(encrypted_msg)
#     print("cleaning up messy encryption...")
#     print("Ciphertext is: " + str(encrypted_msg.decode('utf-8')))
          
# # 4 define function: decrypts the msg by decrypting the Fernet token
# def decrypt_message():  
#     message = input("Enter encrypted message for me to decrypt: ").encode()
#     print("Ciphertext is: " + str(message.decode('utf-8')))
#     decrypted = f.decrypt(message)
#     print("This message will self-destruct in 10 seconds.  10... 9...")
#     print("Plaintext is: " + str(message.decode('utf-8')))

# # 5 define function: a menu for user to input choice of encryption or decryption
# def ask_user(): 
#     user_choice = input("Encrypt file: enter 1\n Decrypt file: enter 2\n Encrypt message: enter 3\n Decrypt message: enter 4\n Exit: enter 'n'")

#     if (user_choice == "1"):
#         encrypt_file()
#         print("Your file has been encrypted. *Sh-sh-shaaaaahh!!!* ")
#     elif (user_choice == "2"):
#         decrypt_file()
#         print("Your file has been decrypted, SIRE.")
#     elif (user_choice == "3"):
#         encrypt_message()
#         print("*takes your message*")
#         print("")
#         print("*tears it into shreds*")
#         print("")
#         print("Your message is now encrypted.  ;) ")
#     elif (user_choice == "4"):
#         decrypt_message()
#         print("*feverishly pieces your message back together with scotch tape*")
#         print("")
#         print("*hands you a tiny taped-up mess*")
#         print("")
#         print("Your message has been decrypted.")
#     elif (user_choice == "n"):
        
#         sys.exit()
#     else:
#         print("That is not an option in the menu. Try again.")


# # loads the key from the current directory named 'key.key'
# # While loop reads key variable
# while True:
# # key check
#     key_exists = os.path.exists('key.key')
#     print('Key Status: ')
#     print(key_exists)
#     if key_exists == False: 
#         write_key()
#     else: 
#         load_key()

# #Main
# ask_user()
# # While user_choice

