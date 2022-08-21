import requests
import json

import sys
sys.path.insert(0,'bs4.zip')
from bs4 import BeautifulSoup

#Imitate the Mozilla browser.
user_agent = {'User-agent': 'Mozilla/5.0'}


def compare_prices(product_laughs,product_glomark):
    #TODO: Aquire the web pages which contain product Price

    
    
    #TODO: LaughsSuper supermarket website provides the price in a span text.
    page = requests.get(url=product_laughs)
    html = page.content
    soup = BeautifulSoup(html, 'html.parser') 

    tag = soup.find( class_ = 'product-name') # get product element
    text = tag.get_text() # Removing html tags
    product_name_laughs = text.strip() # Cleaning Data
    #print(product_name_laughs)

    price = soup.find('span', class_='regular-price') # get price element
    price = price.get_text() # Removing html tags
    price_laughs = price.strip() # Cleaning Data
    price_laughs= price_laughs.replace("Rs.", "")
    price_laughs=float(price_laughs)
    #print(price_laughs)
    

    #TODO: Glomark supermarket website provides the data in jason format in an inline script.
    #You can use the json module to extract only the price

    page = requests.get(url=product_glomark, headers=user_agent) 
    html = page.content
    soup = BeautifulSoup(html, 'html.parser') 

    tag = soup.find( class_ = 'product-title') # get product element
    text = tag.get_text() # Removing html tags
    product_name_glomark = text.strip() # Cleaning Data
    #print(product_name_glomark)

    data = [
     json.loads(x.string) for x in soup.find_all("script", type="application/ld+json")
    ]
    for d in data:
      price_glomark=(d['offers'][0]['price'])
    price_glomark=float(price_glomark)
    #print(price_glomark)

    
    #TODO: Parse the values as floats, and print them.
    
    print('Laughs  ',product_name_laughs,'Rs.: ' , price_laughs)
    print('Glomark ',product_name_glomark,'Rs.: ' , price_glomark)
    
    if(price_laughs>price_glomark):
        print('Glomark is cheaper Rs.:',price_laughs - price_glomark)
    elif(price_laughs<price_glomark):
        print('Laughs is cheaper Rs.:',price_glomark - price_laughs)    
    else:
        print('Price is the same')
