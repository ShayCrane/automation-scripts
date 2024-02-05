#!/usr/bin/python3


# Script Name: Cookie Capture Capades
# Author: Shay Crane
# Date of last revision: 11/22/2022
# Purpose: Identify user of a given web app

# I found information at the following site that
# helped me complete this challenge:  
# https://www.geeksforgeeks.org/python-script-to-open-a-web-browser/


# The below Python script shows one possible method to return the cookie from a site that supports cookies.

import requests
import webbrowser




# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster(): # Because why not!
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

# Add here some code to make this script perform the following:
# - Send the cookie back to the site and receive a HTTP response
# - Generate a .html file to capture the contents of the HTTP response
# - Open it with Firefox
#
# Stretch Goal
# - Give Cookie Monster hands


# completing script per instructions above
# open a file and write to it the pagecontent variable     
page = requests.get(targetsite, cookies=cookie)
pagecontent = page.text
with open ('/home/shay/request.html', 'w') as f:
    f.write(pagecontent)

# register Firefox as browser for Python to use:
# webbrowser.register("firefox", None, webbrowser.BackgroundBrowser("/var/lib/snapd/desktop/applications/firefox_firefox.desktop")) #instance=None, preferred=False)
# ran script, only needs to be run once. browser is now registered. 
    

# set file path and open in firefox
url = 'file:///home/shay/request.html'
webbrowser.get("firefox").open(url)





