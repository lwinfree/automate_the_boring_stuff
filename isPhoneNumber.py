# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 15:52:46 2016

@author: lillywinfree
"""
#! usr/bin/env python3
#isPhoneNumber.py

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True
    
message='call me at 415-555-1011 tomorrow. 415-555-9999 is my officec.'
for i in range(len(message)):
    chunk=message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')
    
# can write this with regular expressions (regex)
#import regex - import re
#create Regex object - re.complie() use w raw string
#pass your string into Regex object's search() method, returns a Match object
#call the Match object's group() method to return a string of matched text    

#phoneNumberRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#mo=phoneNumberRegex.search('My number is 415-555-4242.')  
#print('phone number found: ' + mo.group())
  