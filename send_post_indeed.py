import requests
from requests import get 

#user input 
query = input("query:\n")
location = input("location:\n")

#params for requests method
params = {'q':query , 'l':location}

#search url
baseurl = urlparse(url).netloc
requests.get("https://tr.indeed.com/jobs", params = params).url