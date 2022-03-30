from requests import get 
from bs4 import BeautifulSoup
import pandas as pd 


url = 'https://tr.indeed.com/jobs?q=python%20developer&l&vjk=1ca2f79b63043079'
# heading6 company_location tapItem-gutter companyInfo

content = get(url).content
bs_obj = BeautifulSoup(content, "lxml")


#main container 
container = bs_obj.find_all('div', class_='job_seen_beacon')

jobs = []

for x in container:
	try:
		#parameters
		jobTitle = x.find('h2', class_='jobTitle jobTitle-color-purple').text
		companyName = x.find('span', class_='companyName').text
		location = x.find('div', class_='companyLocation').text
		description = x.find('div', class_='job-snippet').text


		print("="*50)
		print("JOB TITLE:\t", jobTitle)
		print("COMPANY:\t", companyName)	
		print("LOCATION:\t", location)
		print("DESCRIPTION:\t",description)
		

		jobdata = [jobTitle,companyName,location,description]
		jobs.append(jobdata)

		# try:
		# 	joblink = x.find('a',href=True)
		# 	print("JOBLINK:\t",joblink['href'])
		# except:
		# 	pass

	except:

		#parameters 
		newJobTitle = x.find('h2', class_= "jobTitle jobTitle-color-purple jobTitle-newJob").text
		companyName = x.find('span', class_='companyName').text
		location = x.find('div', class_='companyLocation').text
		description = x.find('div', class_='job-snippet').text
		

		print("="*50)
		print("NEW JOB TITLE:\t", newJobTitle)
		print("COMPANY:\t", companyName)	
		print("LOCATION:\t", location)
		print("DESCRIPTION:\t",description)

		jobdata = [newJobTitle,companyName,location,description]
		jobs.append(jobdata)



		# try:
		# 	joblink = x.find('a',href=True)
		# 	print("JOBLINK:\t",joblink['href'])
		# except:
		# 	pass
		

		pass 


jobs = pd.DataFrame(jobs)
print(jobs)

jobs.to_csv('indeed_page_1.csv')