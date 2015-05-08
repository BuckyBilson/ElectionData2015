import urllib2
from bs4 import BeautifulSoup
import re

tarurl = "http://www.bbc.co.uk/news/politics/constituencies" # the page that lists the constituency pages

constituencies = []

url = urllib2.urlopen(tarurl).read() #pull the HTML of the page
soup = BeautifulSoup(url)
for line in soup.find_all('a'):
	newline = line.get('href') # find the links
	if newline[:30] == "/news/politics/constituencies/": # match to the ones we want
		constituencies.append(newline)

for const in constituencies:
	url = urllib2.urlopen("http://www.bbc.co.uk/"+const) # append our detected ones to the beeb site
	stats = []
	for line in url.readlines():
		if '<li class="party__result--votes essential">' in line: # get the constituency name
			result = re.split("<|>", line)
			stats.append(result[2])
		elif '<div class="party__name--long">' in line: # get the party name
			result = re.split("<|>", line)
			stats.append(result[2])
		elif '<h1 class="constituency-title__title">' in line: # get the number of votes
			result = re.split("<|>", line)
			stats.append(result[2])

	print "|".join(stats)
