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
htmldata = getdata("https://www.g-star.com/nl_nl/shop/dames/tops")

#load more button
soup = BeautifulSoup(htmldata, 'html.parser')

#find all links + titles and add them in the list
for item in soup.find_all('img', alt=True, srcset=True):
    webshop = "g-star"
    productName = item['alt']
    link = item['srcset']
    list_images.append((webshop, productName, link))

    # with open (name +'.jpg', 'wb') as f: 
    #     im = requests.get(link)
    #     f.write(im.content)

df = pd.DataFrame(list_images, columns = ['Webshop','Product name', 'Link'])

df.to_csv('images_g-star.csv')

print(df)