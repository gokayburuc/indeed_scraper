#!/usr/bin/env python

from urllib.parse import parse_qs,parse_qsl
from pprint import pprint 

url = 'https://tr.indeed.com/viewjob?jk=3e17e649ba55ddef&tk=1fvdkl5qujl28800&from=serp&vjs=3'
url_two ='https://tr.indeed.com/viewjob?jk=657612a95903987a&tk=1fvdn64thsp7u801&from=serp&vjs=3'


pprint(parse_qsl(url))