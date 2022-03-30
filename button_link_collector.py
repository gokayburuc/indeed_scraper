#!/usr/bin/env python

from requests import get 
from bs4 import BeautifulSoup
import pandas as pd 


url ='https://tr.indeed.com/jobs?q=python%20developer&l=istanbul&ts=1648656157857&rs=1&vjk=1ca2f79b63043079'

content = get(url).content
bs_obj = BeautifulSoup(content, "lxml")

print(type(bs_obj))

buttons = bs_obj.find('ul', class_='pagination-list')

print(type(buttons))

links = buttons.find_all('a', href=True)

for link in links:
	print(link['href'])
