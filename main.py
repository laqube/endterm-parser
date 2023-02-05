import requests
import json
from bs4 import BeautifulSoup
import urllib3
import time


dataset =[]
counter = 0

for p in range(1, 24):
    url=''
    if(p==1):
        url = 'https://www.olx.kz/d/kk/dom-i-sad/mebel/mebel-dlya-vannoy-komnaty'
    else:
        url = 'https://www.olx.kz/d/kk/dom-i-sad/mebel/mebel-dlya-vannoy-komnaty/?page=' + str(p)
    # url="https://kolesa.kz/cars/"

    dataset =[]
    counter = 0
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    print("Status: " + str(response.status))
    print("!____LESGOOOOOOOOOOOOOOOOOOOOOOOOOOOO____!")
    print("!______________A_NEW_PAGE________________!")
    print("PAGE NUMBER:" + str(p))

    soup = BeautifulSoup(response.data, features="html.parser")
    names = soup.find_all("a", {"class":"css-rc5s2u"})
    pCount = len(names)
    pLinks = [] 
    for i in range(0, pCount):
        pLinks.append(names[i].get('href'))
        purl = 'https://www.olx.kz/d/kk/obyavlenie' + names[i].get('href')
        print('PRODUCT+1_________________________')
        newhttp = urllib3.PoolManager()
        newresponse = newhttp.request('GET', purl)

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
        dataset.append(product)
        counter += 1
    time.sleep(1)
print(dataset)  
print("BOLDY__________________________")
print("Product count: " + str(counter))
print("ADIHAT_________________________")  
with open('olx_dataset.json', 'w') as outfile:
    json.dump(dataset, outfile, ensure_ascii=False)

