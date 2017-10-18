from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

f = open("comments_32355.html", "r")
text = f.read()
f.close()

soup = BeautifulSoup(text, "html.parser")

numbers = []

for x in soup.find_all('span'):
	numbers.append(int(x.text))

print(sum(numbers))
# print(sum(numbers))