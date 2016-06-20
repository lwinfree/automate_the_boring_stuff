# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 12:10:22 2016

@author: lillywinfree
"""

#! /usr/bin/env python3.
# password.py - insecure password locker program

PASSWORDS = {'email': 'akjshdkjashdk', 
'blog': 'AShkajhsdkjkjhs',
'luggage': '12345'}

import sys, pyperclip
if len(sys.argv)<2:
    print('Usage: python password.py [account]-copy account password')
    sys.exit()
    
account = sys.argv[1]   #first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else: print('There is no account named ' + account)

