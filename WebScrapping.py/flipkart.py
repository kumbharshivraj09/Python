

print("")

import requests
import pandas as pd
from bs4 import BeautifulSoup

url = ('https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DMOTOROLA&param=19873&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIk1vdG9yb2xhIHNtYXJ0cGhvbmVzIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&bu=MOBILE&wid=10.productCard.PMU_V2_10')
headers ={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}


r = requests.get(url, headers=headers)
soup=BeautifulSoup(r.text,"html.parser")

soup.find_all('div',class_='DOjaWF gdgoEp')
class1=soup.find_all('div',class_='DOjaWF gdgoEp')

class1[0]
phones_html = class1[0]

phones_html.find_all('div',class_='cPHDOP col-12-12')

phones=phones_html.find_all('div',class_='cPHDOP col-12-12')

phones[0]

phones[0].find('img')['src'] #img
phones[0].find('div',class_='KzDlHZ').text #name
phones[0].find('div',class_='Nx9bqj _4b5DiR').text #price
phones[0].find('div',class_='XQDdHH').text #rating
phones[0].find('div',class_='_6NESgJ').text #descri

for item in phones:
    try:
       print(item.find('img')['src'])       #img
    except Exception as err:
        print("Error ")

for item in phones:
    try:
        print(item.find('div',class_='KzDlHZ').text)   #name
    except Exception as err:
        print("Error ")

for item in phones:
    try:
        print(item.find('div',class_='Nx9bqj _4b5DiR').text)   #price
    except Exception as err:
        print("Error ")

for item in phones:
    try:
        print(item.find('div',class_='XQDdHH').text)   #rating
    except Exception as err:
        print("Error ")

for item in phones:
    try:
        print(item.find('div',class_='_6NESgJ').text)   #discrip
    except Exception as err:
        print("Error ")