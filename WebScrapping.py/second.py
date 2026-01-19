
import requests
from bs4 import BeautifulSoup
import pandas as pd

web=requests.get('https://webscraper.io/test-sites/e-commerce/ajax/computers/tablets')
soup=BeautifulSoup(web.text,'html.parser')
# print(web)
# print(web.content)
print(soup.prettify)
# p=soup.find_all('p')
# for i in p:
#  print(p)

box=soup.find_all('div',class_="col-md-4 col-xl-4 col-lg-4")
print(box)