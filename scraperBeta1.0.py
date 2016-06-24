from bs4 import BeautifulSoup
import urllib2
import string
import random
import urllib
import os
import re
import time

word = raw_input("Gimme a word: ")
while (1<2):
	tempUrl = "https://pastebin.com"
	req = urllib2.Request(tempUrl, headers={ 'User-Agent': 'Mozilla/5.0' })
	html = urllib2.urlopen(req).read()
	#soup = BeautifulSoup(html)
	soup = BeautifulSoup(html, "html.parser")
	pastesUrl = soup.findAll('ul', attrs={'class':['right_menu']})

	for ul in pastesUrl:
	    href_tags = soup.findAll('ul', attrs={'class':['right_menu']})
	for ul in href_tags:
		links = ul.find('a')['href']
		#Debug
	url = "https://pastebin.com/raw" + str(links)
	#url = "https://pastebin.com/raw/QJABPw68"

	text = urllib.urlopen(url).read()

	#### Other way to scan raw file
	#textRaw = textRaw.urlopen(url)
	#text = textRaw.read().decode("utf-8")

	answer = "[-] Invalid: " + url
	for line in text:
    	#print line
		#print text
		if (word in text):
			answer = "[+] Valid: " + url
			# Name file amount
			#name = str(len([name for name in os.listdir('.') if os.path.isfile(name)]) - 1)
			link = links.replace("/", "")
			urllib.urlretrieve(url, str(link) + ".txt")
			break

	print answer
	time.sleep(3)
	#print url
