import requests
import json
from bs4 import BeautifulSoup
import urllib3
import time

dataset = []
counter = 0

http = urllib3.PoolManager()
for p in range(1, 24):
    if p == 1:
        url = 'https://www.olx.kz/d/kk/dom-i-sad/mebel/mebel-dlya-vannoy-komnaty'
    else:
        url = 'https://www.olx.kz/d/kk/dom-i-sad/mebel/mebel-dlya-vannoy-komnaty/?page=' + str(p)

    response = http.request('GET', url)
    print("Status: " + str(response.status))
    print("!____LESGOOOOOOOOOOOOOOOOOOOOOOOOOOOO____!")
    print("!______________A_NEW_PAGE________________!")
    print("PAGE NUMBER: " + str(p))

    soup = BeautifulSoup(response.data, "html.parser")
    names = soup.find_all("a", {"class": "css-rc5s2u"})

    for name in names:
        purl = 'https://www.olx.kz/d/kk/obyavlenie' + name.get('href')
        print('PRODUCT+1_________________________')
        newresponse = http.request('GET', purl)

        newsoup = BeautifulSoup(newresponse.data, "html.parser")
        try:
            pName = newsoup.find("h1", {"class": "css-1soizd2 er34gjf0"}).get_text()
        except ValueError:
            pName = "None"
        try:
            pPrice = int("".join(newsoup.find("h3", {"class": "css-ddweki er34gjf0"}).get_text().split()[:-1]))
        except ValueError:
            pPrice = 0
        pTags = newsoup.find("ul", {"class": "css-sfcl1s"})
        wTag = pTags.find_all("p")
        try: 
            pTags = [i.get_text() for i in wTag]
        except:
            pTags = []
        product = {
            "Product_Name": pName,
            "Price": pPrice,
            "Tags": pTags
        }
        print(product)
        dataset.append(product)
        counter += 1
    time.sleep(1)

print(dataset)  
print("BOLDY__________________________")
print("Product count: " + str(counter))
print("ADIHAT_________________________")  
with open("olx_dataset.json", "w") as outfile:
    json.dump(dataset, outfile, ensure_ascii=False)
