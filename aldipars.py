import json
from bs4 import BeautifulSoup
import urllib3
import time

url = 'https://enic-kazakhstan.edu.kz/ru/reference_information/universities'

http = urllib3.PoolManager()
response = http.request('GET', url)
print("Status: " + str(response.status))

soup = BeautifulSoup(response.data, "html.parser")
table = soup.find("table", {"class": "display multiMerge dataTable no-footer"})
print(table)