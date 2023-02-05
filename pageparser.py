import requests
import json
from bs4 import BeautifulSoup
import urllib3
import time


url = 'https://www.olx.kz/d/kk/obyavlenie/rakovina-v-almaty-IDntDoq.html'
# url="https://kolesa.kz/cars/"

newhttp = urllib3.PoolManager()
newresponse = newhttp.request('GET', url)
print("Status: " + str(newresponse.status))
print("!____LESGOOOOOOOOOOOOOOOOOOOOOOOOOOOO____!")

newsoup = BeautifulSoup(newresponse.data, features="html.parser")

pName = newsoup.find("h1", {"class": "css-1soizd2 er34gjf0"}).get_text()
pPrice = int("".join(newsoup.find("h3", {"class": "css-ddweki er34gjf0"}).get_text().split()[:-1]))
pTags = newsoup.find("ul", {"class":"css-sfcl1s"})
wTag = pTags.find_all("p")
pTags = []
d = {}
# print(pTags)
# print(pTag)
for i in wTag:
    # print(i.get_text())
    pTags.append(i.get_text())
product = {
    'Product_Name':pName,
    'Price':pPrice,
    'Tags':pTags
}
print(product)
time.sleep(1)
