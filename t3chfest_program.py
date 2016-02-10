#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2
from bs4 import BeautifulSoup
import string
import requests
import cookielib
import csv
import json


talks_t3chfest=[]

def main():
    url = "https://t3chfest.uc3m.es/programa/"

    data = requests.get(url)

    bs = BeautifulSoup(data.text,"lxml")
    
    print "Links"
    print "-------------------" 
    links = bs.find_all('a')
    for link in links:
            print link
            

    track1 = bs.find_all('a', {'class': 'track1'})
    track2 = bs.find_all('a', {'class': 'track2'})
    track3 = bs.find_all('a', {'class': 'track3'})
    track4 = bs.find_all('a', {'class': 'track4'})
    
    for aux in track1:
	speaker = aux.find('p')
	title = aux.find('h5')
	track = "track1"
	talk_t3chfest = {}
	if speaker is not None and title is not None:
	    talk_t3chfest['speaker'] = speaker.text.encode('utf-8')
	    talk_t3chfest['title'] = title.text.encode('utf-8')
	    talk_t3chfest['track'] = track
	    if talk_t3chfest not in talks_t3chfest:
		talks_t3chfest.append(talk_t3chfest)

    for aux in track2:
	speaker = aux.find('p')
	title = aux.find('h5')
	track = "track2"
	talk_t3chfest = {}
	if speaker is not None and title is not None:
	    talk_t3chfest['speaker'] = speaker.text.encode('utf-8')
	    talk_t3chfest['title'] = title.text.encode('utf-8')
	    talk_t3chfest['track'] = track
	    if talk_t3chfest not in talks_t3chfest:
		talks_t3chfest.append(talk_t3chfest)
		
    for aux in track3:
	speaker = aux.find('p')
	title = aux.find('h5')
	track = "track3"
	talk_t3chfest = {}
	if speaker is not None and title is not None:
	    talk_t3chfest['speaker'] = speaker.text.encode('utf-8')
	    talk_t3chfest['title'] = title.text.encode('utf-8')
	    talk_t3chfest['track'] = track
	    if talk_t3chfest not in talks_t3chfest:
		talks_t3chfest.append(talk_t3chfest)
		
    for aux in track4:
	speaker = aux.find('p')
	title = aux.find('h5')
	track = "track4"
	talk_t3chfest = {}
	if speaker is not None and title is not None:
	    talk_t3chfest['speaker'] = speaker.text.encode('utf-8')
	    talk_t3chfest['title'] = title.text.encode('utf-8')
	    talk_t3chfest['track'] = track
	    if talk_t3chfest not in talks_t3chfest:
		talks_t3chfest.append(talk_t3chfest)    
		

if __name__=="__main__":
    main()

    outfile = open('t3chfest.json','wb')
    outfile.write('[')
    index = 0
    
    for talk_t3chfest in talks_t3chfest:
	index = index +1
	print talk_t3chfest['track']
        print talk_t3chfest['title'].decode('utf-8').encode('cp850','replace').decode('cp850')
        print talk_t3chfest['speaker'].decode('utf-8').encode('cp850','replace').decode('cp850')
        line = json.dumps(talk_t3chfest,sort_keys=True, indent=4) + "\n"
	if len(talks_t3chfest)>index:
	    outfile.write(line+",")
	else:
	    outfile.write(line)
		
	print "------------------"
	
    outfile.write(']')
    
    with open('t3chfest.csv' ,'wb') as csvfile: 
            t3chfest_writer = csv.writer(csvfile)
            for result in talks_t3chfest:
                t3chfest_writer.writerow([str(result['track']),str(result['title']),str(result['speaker'])])
	
	
	
