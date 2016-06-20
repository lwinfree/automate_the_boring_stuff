# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 15:19:46 2016

@author: lillywinfree
"""

#! usr/bin/env python3
# mapIt.py - opens google map and pastes address from clipboard

import webbrowser, sys, pyperclip
if len(sys.argv)>1:
    #get address from command line
    address= ' '.join(sys.argv[1:])
else:
    #get address from clipboard
    address= pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)