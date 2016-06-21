# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 14:12:52 2016

@author: lillywinfree
"""

#! usr/bin/env python3
#lucky.py searches google, opens several results

import requests, sys, webbrowser, bs4

print('Googling...')  #display text while downloading the Google page
res=requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

#Retrieve top search results links
soup=bs4.BeautifulSoup(res.text)

#Open a browser tab for each result
linkElems=soup.select('.r a')
numOpen=min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
    


