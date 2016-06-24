from bs4 import BeautifulSoup
import urllib2
import string
import random
import urllib
import os
import re
import time

print ("Welcome to Pastebin Scraper")
print("Please type the number for the search mode")
print ("1: Scan a specific word.")
print ("2: Scan for various words, dividing them by space bar.")
# print ("3: Scan for ips or proxies.")

input = raw_input("Type in the mode:")
if (input == 1):
	word = raw_input("Gimme a word: ")
	while (1<2):
		tempUrl = "https://pastebin.com"
		req = urllib2.Request(tempUrl, headers={ 'User-Agent': 'Mozilla/5.0' })
		html = urllib2.urlopen(req).read()
		soup = BeautifulSoup(html, "html.parser")
		pastesUrl = soup.findAll('ul', attrs={'class':['right_menu']})

		for ul in pastesUrl:
		    href_tags = soup.findAll('ul', attrs={'class':['right_menu']})
		for ul in href_tags:
			links = ul.find('a')['href']

		url = "https://pastebin.com/raw" + str(links)

		text = urllib.urlopen(url).read()

		answer = "[-] Invalid: " + url
		for line in text:
	    	#print line
			#print text
			if (word in text):
				answer = "[+] Valid: " + url
				link = links.replace("/", "")
				urllib.urlretrieve(url, str(link) + ".txt")
				break
		print answer
		time.sleep(3)
else if (input == 2):
	word = raw_input("Gimme a set of words: ")

	while (1<2):
		tempUrl = "https://pastebin.com"
		req = urllib2.Request(tempUrl, headers={ 'User-Agent': 'Mozilla/5.0' })
		html = urllib2.urlopen(req).read()
		soup = BeautifulSoup(html, "html.parser")
		pastesUrl = soup.findAll('ul', attrs={'class':['right_menu']})

		for ul in pastesUrl:
		    href_tags = soup.findAll('ul', attrs={'class':['right_menu']})
		for ul in href_tags:
			links = ul.find('a')['href']

		url = "https://pastebin.com/raw" + str(links)

		text = urllib.urlopen(url).read()

		answer = "[-] Invalid: " + url
		for line in text:
	    	#print line
			#print text
			if (word in text):
				answer = "[+] Valid: " + url
				link = links.replace("/", "")
				urllib.urlretrieve(url, str(link) + ".txt")
				break
		print answer
		time.sleep(3)
