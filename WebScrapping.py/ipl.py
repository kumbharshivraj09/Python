import requests
from bs4 import BeautifulSoup
import pandas as pd

url='https://www.iplt20.com/auction/2022'
web=requests.get(url)
# print(web)
soup=BeautifulSoup(web.text,'html.parser')
# print(soup.prettify)

table=soup.find("table",class_="ih-td-tab w-100 auction-tbl")
# print(table)
title=soup.find_all()