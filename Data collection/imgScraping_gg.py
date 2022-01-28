import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

#save images in a list
list_images=[]

#request
def getdata(url):
    r = requests.get(url)
    return r.text

#define URL
htmldata = getdata("https://www.gutsgusto.com/nl/kleding/tops-blouses")

#load more button
soup = BeautifulSoup(htmldata, 'html.parser')

#find all links + titles and add them in the list
for item in soup.find_all('img', alt=True, src=True):
    webshop = "Guts-Gusto"
    productName = item['alt']
    link = item['src']
    list_images.append((webshop, productName, link))

df = pd.DataFrame(list_images, columns = ['Webshop','Product name', 'Link'])

df.to_csv('images_gutsgusto.csv')

print(df)