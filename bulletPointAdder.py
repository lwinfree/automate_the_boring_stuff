# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 14:11:39 2016

@author: lillywinfree
"""

#! usr/bin/env python3
# bulletPointAdder.py
#add * at beginning of each line of a list, then paste to clipboard

import pyperclip
text=pyperclip.paste()

#separate lines and add stars
lines=text.split('\n')
for i in range(len(lines)):  #loop thru all indexes in the "lines" list
    lines[i]= '* ' + lines[i] # add star to each string in "lines" list
text = '\n'.join(lines)  #join list of string values to single string value to pass to pyperclip.copy

pyperclip.copy(text)
