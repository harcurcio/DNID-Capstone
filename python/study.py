#Python program to scrape website  
#and save quotes from website 
import requests 
from bs4 import BeautifulSoup 
import csv 
   
URL = "https://www.coronavirus.pitt.edu/student-learning-living/study-spaces"
r = requests.get(URL) 
   
soup = BeautifulSoup(r.content, 'html5lib')
status=[]  # a list to store statuses 
   
table = soup.find('section', attrs = {'id':'block-system-main'}) 
#print(table.prettify())
   
for row in table.findAll('dl', attrs= {'class': "ckeditor-accordion"}):
	study= {}
	study['Room'] = row.dt.text
	status.append(study);
print(status)

filename = 'studyspace.csv'
with open(filename, 'w', newline='') as f: 
    w = csv.DictWriter(f,['Room']) 
    w.writeheader() 
    for study in status: 
        w.writerow(study) 

	#print(row.h4.text)
	#stat = {}
	#stat['posture'] = row.h4.text
	#for row2 in table.findAll('ul'):
#		for row3 in table.findAll('li'):
#			stat['campus'] = row.li.text
#	status.append(stat)
