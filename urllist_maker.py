import requests
from requests import get
from urllib.parse import quote 

#user input 
query = input("query:\n").replace(' ', '+')
location = input("location:\n")

#params for requests method
params = {'q':quote(query) , 'l':quote(location)}

#search url
search_url = requests.get("https://tr.indeed.com/jobs?", params = params).url


urllist = []

for x in range(10, 100, 10):
	new_url = f"{search_url}&start={str(x)}"
	print(new_url)