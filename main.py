import requests
import json
from bs4 import BeautifulSoup
import urllib3
import time

dataset = []  #An empty dataset
counter = 0   #A document counter

http = urllib3.PoolManager()
for p in range(1, 24):
    if p == 1:
        url = 'https://www.olx.kz/d/kk/dom-i-sad/mebel/mebel-dlya-vannoy-komnaty'                 #First page of the category
    else:
        url = 'https://www.olx.kz/d/kk/dom-i-sad/mebel/mebel-dlya-vannoy-komnaty/?page=' + str(p) #Rest of the pages 

    response = http.request('GET', url)
    print("Status: " + str(response.status))
    print("!____LESGOOOOOOOOOOOOOOOOOOOOOOOOOOOO____!")     #indication of successful connection
    print("!______________A_NEW_PAGE________________!")             
    print("PAGE NUMBER: " + str(p))                         #page counter

    soup = BeautifulSoup(response.data, "html.parser")
    names = soup.find_all("a", {"class": "css-rc5s2u"})     #all the links for certain products located on that page

    for name in names:
        purl = 'https://www.olx.kz/d/kk/obyavlenie' + name.get('href')
        print('PRODUCT+1_________________________')         #indication of successfull connection to a product page
        newresponse = http.request('GET', purl)             

        newsoup = BeautifulSoup(newresponse.data, "html.parser")
                                                            #I used try-except block to ignore errors in case if one of the variables is null or of wrong datatype
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
        }                                                   #The structure of single document
        print(product)
        dataset.append(product)
        counter += 1
    time.sleep(1)                                           #Timer to avoid bot detection, actually in my case I believe it was useless

print(dataset)  
print("BOLDY__________________________")                    #Indicator of successful completion of scrabbing 
print("Product count: " + str(counter))                     #Document counter
print("ADIHAT_________________________")                    
with open("olx_dataset.json", "w") as outfile:              #Creating a json file
    json.dump(dataset, outfile, ensure_ascii=False)         #ensure_ascii=False is used in order to decode the dataset right away
