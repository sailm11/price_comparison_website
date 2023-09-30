import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time
import sys

import requests
from bs4 import BeautifulSoup

options = webdriver.FirefoxOptions()

#uncomment the below code if you don't want a browser window to open
# options.add_argument('--headless') 

flag = 0
cchc = ''

#will contain the peices of all websites and show the best price accordingly
final_price_list = []

proItem = input("Enter product name:\n")
itemName = proItem.replace(" ","+")

def amazon(itemName):

    itemName = itemName
    amazon_url = f'https://www.amazon.in/s?k={itemName}&ref=nb_sb_noss'
    headers = {
        'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'
    }


    req = requests.get(amazon_url,headers=headers)
    soup = BeautifulSoup(req.content,'html.parser')


    pro_list = soup.find_all('div',{'data-component-type':'s-search-result'})
    try:
        prod = pro_list[0]

        imageTag = prod.find('div',class_='a-section aok-relative s-image-fixed-height')
        prodImage = imageTag.find('img')
        prodImageLink = prodImage['src']
        print("Image Link:",prodImageLink)

        atag = prod.h2.a
        prodName = atag.text

        price = prod.find('span',class_="a-price")
        amazonPrice = price.find('span',class_="a-offscreen").text
            

        temp_pro_price = amazonPrice.replace("₹","")
        final_pro_price = float(temp_pro_price.replace(",",""))
        final_price_list.append(final_pro_price)

        print("\nName:",prodName)
        print("Product Link: ",amazon_url)
        print("Price:",amazonPrice)
        time.sleep(2)
    except:
        print("Product not found!")
        print("\n\n\nNow Let's scrape Croma.........\n")

def flipkart(itemName):
    itemName = itemName
    url= f"https://www.flipkart.com/search?q={itemName}"
    req = requests.get(url)
    content= BeautifulSoup(req.content, 'html.parser')
    #     print(content)
    name= content.find('div', {"class": '_4rR01T'})
    price = content.find('div', {"class": "_30jeq3 _1_WHN1"})
    image = content.find('div', {"class": 'css-1dbjc4n r-1awozwy r-1wfhzrg r-1h0z5md'})
    