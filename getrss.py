
#By ##

import feedparser, os, sys, time, datetime, subprocess

data = time.strftime('%d%m%Y')
arq = open(data+'.txt', 'rw')

#Get feeds just title
url = feedparser.parse('http://www.wordpressexploit.com/feed/')
with open(data+'.txt', 'rw') as outfile:
	for e in url['entries']:
    #print e.get('title', '')
		title = e.get('title', '')
		summary =  e.get('summary', '') 
		link = e.get('link', '')
		outfile.write(title)


	


    
    



