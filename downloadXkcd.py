# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 15:44:23 2016

@author: lillywinfree
"""

#! usr/bin/env Python3
# downloadXkcd.py - downloads every XKCD comic

import requests, os, bs4

url='http://xkcd.com'   #starting url
os.makedirs('xkcd', exist_ok=True)   #store comics in ./xkcd
while not url.endswith('#'):
    # Download the page
    print('Downloading page %s...' % url)
    res=requests.get(url)
    res.raise_for_status()
    
    soup=bs4.BeautifulSoup(res.text)
    
    # Find the URL of the comic image
    comicElem=soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        try:
            comicUrl='http:' + comicElem[0].get('src')
            #download the image
            print('Downloading the image %s...' % (comicUrl))
            res=requests.get(comicUrl)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            #skip this comic
            prevLink=soup.select('a[rel="prev"]')[0]
            url='http://xkcd.com' + prevLink.get('href')
            continue
        
    #TODO: Save the image to ./xkcd
    imageFile=open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
        
    #TODO: Get the Prev button's url
    prevLink=soup.select('a[rel="prev"]')[0]
    url='http://xkcd.com' + prevLink.get('href')    

print('Done.')
