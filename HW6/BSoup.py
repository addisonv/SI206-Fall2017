from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

url = urlopen('http://py4e-data.dr-chuck.net/known_by_Aedin.html')
text = url.read()

for i in range(7):
	soup = BeautifulSoup(text, "html.parser")
	a = soup.find_all('a')
	link = a[17]
	url = urlopen(link['href'])
	text = url.read()
	soup2 = BeautifulSoup(text, "html.parser")
	for x in soup2.find_all('title'):
		name = x.text
	
print(name)


