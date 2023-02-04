import requests
import json
from bs4 import BeautifulSoup
import urllib3


url = 'https://www.olx.kz/d/kk/obyavlenie/rakovina-v-almaty-IDntDoq.html'
# url="https://kolesa.kz/cars/"

newhttp = urllib3.PoolManager()
newresponse = newhttp.request('GET', url)
print("Status: " + str(newresponse.status))
print("!____LESGOOOOOOOOOOOOOOOOOOOOOOOOOOOO____!")

newsoup = BeautifulSoup(newresponse.data, features="html.parser")

pName = newsoup.find("h1", {"class": "css-1soizd2 er34gjf0"}).get_text()
pPrice = newsoup.find("h3", {"class": "css-ddweki er34gjf0"}).get_text()
pTags = newsoup.find("ul", {"class":"css-sfcl1s"})

pTag = pTags.find_all("p")

print(pName)
print(pPrice)
# print(pTags)
# print(pTag)
for i in pTag:
    print(i.get_text())