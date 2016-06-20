# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 20:45:18 2016

@author: lillywinfree
"""

#! usr/bin/env python3 
#phoneAndEmail.py 
#finds phone numbers and email addresses from the clipboard

import pyperclip, re
#create phone number regex
phoneRegex=re.compile(r'''(
    (\d{3}|\(d{3}\))?                #area code
    (\s|-|\.)?                       #separator
    (\d{3})                          #first 3 digits
    (\s|-|\.)                        #separator
    (\d{4})                          #last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?   #extension
    )''', re.VERBOSE)                #gets rid of spaces
#create email regex
emailRegex=re.compile(r'''(
    [a-zA-Z0-9._%+-]                 #username
    @          
    [a-zA-Z0-9._]+                   #domain name
    (\.[a-zA-Z]{2,4})                #dot-something
    )''', re.VERBOSE)
#Find matches in clipboard text.
text=str(pyperclip.paste())
matches=[]        #there is one tuple for each match
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]]) #join the values from each group together w a - to form one value to pass to the clipboard
    if groups[8] != '':             #group8 is the extension
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])
#group 0 matches the entire regex
#copy matches to clipboard
if len(matches)>0:    
    pyperclip.copy('\n'.join(matches))   #join matches to one string value
    print('Copied to the clipboard:')
    print('\n'.join(matches))
else:
    print('No phone number or email address found.')
    