# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 11:48:34 2016

@author: lillywinfree
"""

#! usr/bin/env python3
#stopwatch.py - A simple stopwatch program

import time

#Display program's instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "click" the' +
'stopwatch. Press Ctrl-C to quit.')
input()   #press Enter to begin
print('Started.')
startTime=time.time()   #get the first lap's start time
lastTime = startTIme
lapNum=1

#TODO: Start tracking the lap times

try:
    while True:
        input()
        lapTime=round(time.time() - lastTime, 2)
        totalTime = round(time.time()-startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time() #reset the last lap time
except KeyboardInterrupt:
    #handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')
    