import requests
import json
from bs4 import BeautifulSoup
import urllib3


url = 'https://www.olx.kz/d/kk/dom-i-sad/mebel/mebel-dlya-vannoy-komnaty'
# url="https://kolesa.kz/cars/"

http = urllib3.PoolManager()
response = http.request('GET', url)
print("Status: " + str(response.status))
print("!____LESGOOOOOOOOOOOOOOOOOOOOOOOOOOOO____!")

soup = BeautifulSoup(response.data, features="html.parser")
names = soup.find_all("a", {"class":"css-rc5s2u"})
pCount = len(names)
pLinks = []
for i in range(0, pCount):
    pLinks.append(names[i].get('href'))
    purl = 'https://www.olx.kz/d/kk/obyavlenie' + names[i].get('href')
    print(purl)

# pLinks = list(set(pLinks))
# print(len(pLinks))

    


