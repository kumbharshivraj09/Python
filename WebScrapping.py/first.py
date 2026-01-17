# Web Scrapping is an automatic method to obtain large amount of data from website
#Web Scrapiing extraxct underiying html code,with it, data stored in datbase .
 

#structure data - excel format,table etc.
#unstructure data - video,image,link etc.

# component of web scapping : 
#website load-->parsing-->html tree traversel-->extracting data-->transform data

import requests
from bs4 import BeautifulSoup

web=requests.get('https://www.tutorialsfreak.com/')
# print(web.content)
soup=BeautifulSoup(web.content,'html.parser')
# print(soup)
soup.prettify()
# print(soup.title)
# print(soup.h1)

#tag

tag=soup.html
# print(tag)

# tag=soup.p
# print(tag)

tag=soup.a
# print(tag)

#navigable string : 

print(soup.p.string)
print(soup.h1.string)

#Beautfulsoup : 

# print(soup.name)
# print(soup.title)
# print(soup.head)
# print(soup.body)

print(soup.find_all('h2'))
print(soup.find_all('p'))
print(soup.body.prettify())


# FINDING ELEMENT IN WEB PAGE : 


