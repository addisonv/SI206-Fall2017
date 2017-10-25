import unittest
import requests
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = requests.get("https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=All",  headers={'User-Agent': 'SI_CLASS'})
text = url.text
umsi_titles = {}
count = 0
for loop in range(13):
	soup = BeautifulSoup(text, "html.parser")
	x = soup.find_all("div", class_="ds-1col node node-person node-teaser view-mode-teaser clearfix")
	for a in x:
		y = a.find_all("div", class_="field field-name-title field-type-ds field-label-hidden") 
		h2 = y[0].find_all("h2")
		name = h2[0].text
		z = a.find_all("div", class_="field field-name-field-person-titles field-type-text field-label-hidden")
		div = z[0].find_all("div", class_="field-item even")
		title = div[0].text 
		umsi_titles[name]=title
	count+=1
	url = "https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=All&page="
	next_page = url + str(count)
	req = requests.get(next_page,  headers={'User-Agent': 'SI_CLASS'})
	text = req.text
print(umsi_titles)



