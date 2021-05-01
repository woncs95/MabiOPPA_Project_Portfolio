import requests
from bs4 import BeautifulSoup

url = "https://katrin-troisi-hausverwaltung.de/angebote"
html = requests.get(url).text

soup = BeautifulSoup(html, "html5lib")
tags = soup.select("#_bs-7")

for tag in tags:
    print(tag.text)