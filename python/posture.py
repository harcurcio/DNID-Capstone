#Python program to scrape website  
#and save quotes from website 
import requests 
from bs4 import BeautifulSoup 
import csv 
   
URL = "https://www.coronavirus.pitt.edu/"
r = requests.get(URL) 
   
soup = BeautifulSoup(r.content, 'html5lib')
status=[]  # a list to store statuses 
   
table = soup.find('div', attrs = {'class':'views-field views-field-views-conditional'}) 
#print(table.prettify())
   
for row in table.findAll('div', attrs= {'class': ""}):
	print(row)
	#print(row.h4.text)
	#stat = {}
	#stat['posture'] = row.h4.text
	#for row2 in table.findAll('ul'):
#		for row3 in table.findAll('li'):
#			stat['campus'] = row.li.text
#	status.append(stat)
#print(status)

	
#filename = 'risk_posture.csv'
#with open(filename, 'w', newline='') as f: 
#    w = csv.DictWriter(f,['posture','campus']) 
#    w.writeheader() 
#    for stat in status: 
#        w.writerow(stat)
