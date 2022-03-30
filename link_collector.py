#!/usr/bin/env python

from bs4 import BeautifulSoup
from requests import get 
from urllib.parse import urljoin



baseurl = 'https://tr.indeed.com/jobs?q=python%20developer%20&l&vjk=657612a95903987a'

mainurl = 'https://tr.indeed.com/viewjob?'

#scrape parameters
cnt = get(baseurl).content
bs  = BeautifulSoup(cnt,"lxml")

links = bs.find_all('a',href =True)

for t in links:
	print(urljoin(mainurl,t['href']))