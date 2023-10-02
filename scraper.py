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

options = webdriver.ChromeOptions()

wait_time = 10

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
    # itemName = itemName
    # url= f"https://www.flipkart.com/search?q={itemName}"
    # req = requests.get(url)
    # content= BeautifulSoup(req.content, 'html.parser')
    # #     print(content)
    # name= content.find('div', {"class": '_4rR01T'})
    # price = content.find('div', {"class": "_30jeq3 _1_WHN1"})
    print("Let's start scraping flipkart......")
    itemName = itemName
    baseurl='https://www.flipkart.com'
    flipurl = f'https://www.flipkart.com/search?q={itemName}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
    headers = {
    'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'
    }

        #scrape the main pro_list page of item
    req = requests.get(flipurl,headers=headers)
    soup = BeautifulSoup(req.content,'html.parser')

    try:

            #main list
        pro_list = soup.find_all('div',class_='_2kHMtA')

            #will contain links of all product in the list
        proLink = []

        for i in pro_list:
            for link in i.find_all('a',href=True):
                proLink.append(baseurl + link['href'])


            #scrape data from particular item
        itemLink = proLink[0]

        req = requests.get(itemLink,headers=headers)
        soup = BeautifulSoup(req.content,'html.parser')
        image = soup.find_all('img',class_="_396cs4 _2amPTt _3qGmMb")
        rating = soup.find('div', class_="_3LWZlK")

        for name in soup.find_all('span',class_="B_NuCI"):
            pro_name = name.text.strip()
        for price in soup.find_all('div',class_="_30jeq3 _16Jk6d"):
            pro_price = price.text.strip()
        for img in image:
            pro_image = img.get('src')

            #append the price scraped in float form
        temp_pro_price = pro_price.replace("₹","")
        final_pro_price = float(temp_pro_price.replace(",",""))
        final_price_list.append(final_pro_price)
            
        print("\n")    
        print(itemLink)
        print(pro_name)
        print(pro_price)
        print(pro_image)
        print("\n\n\nNow Let's scrape Amazon.....\n")
        ################

    except:
            #main list
        pro_list = soup.find_all('div',class_='_1xHGtK _373qXS')

            #will contain links of all product in the list
        proLink = []

        for i in pro_list:
            for link in i.find_all('a',href=True):
                proLink.append(flipurl + link['href'])


            #scrape data from particular item
        itemLink = proLink[0]

        req = requests.get(itemLink,headers=headers)
        soup = BeautifulSoup(req.content,'html.parser')
        image = soup.find_all('div',class_="CXW8mj _3nMexc")
            
        for name in soup.find_all('span',class_="G6XhRU"):
            pro_name = name.text.strip()
        for price in soup.find_all('div',class_="_30jeq3 _16Jk6d"):
            pro_price = price.text.strip()
        #     for img in image:
        #         pro_image = img.get('src')

        print("\n")    
        print(itemLink)
        print(pro_name)
        print(pro_price)
        #     print(pro_image)
        print("\n\n\nNow Let's scrape Amazon.....\n")

def croma(itemName):
    itemName = itemName.replace("+","%20")
    croma_base_url = 'https://www.croma.com'
    croma_url = f'https://www.croma.com/searchB?q={itemName}%3Arelevance&text={itemName}'
    driver = webdriver.Chrome(options=options)
    headers = {
        'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'
    }

    driver.get(croma_url)

    # driver.implicitly_wait(wait_time)

    soup=BeautifulSoup(driver.page_source,'html.parser')

        #list of all the products on the newUrl
    pro_list = []
    pro = soup.findAll('div',class_='content-wrap')
    for j in pro:
        for i in j.findAll('ul',class_='product-list'):
            # print(i)
            for k in i.findAll('li',class_='product-item'):
                pro_list.append(k)

    try:
        prod = pro_list[0]

        imageTag = prod.find('div',class_='product-img')
        prodImage = imageTag.find('img')
        prodImageLink = prodImage['src']
        print("Image Link:",prodImageLink)

        atag = prod.h3.a

        prodLink = croma_base_url + atag['href']
        print("\nProduct Link:",prodLink)

        name = prod.h3.text
        print("Name:",name)

        cromaPrice = prod.find('span',class_='amount')
            
            #append the price scraped in float form
        temp_pro_price = cromaPrice.replace("₹","")
        final_pro_price = float(temp_pro_price.replace(",",""))
        final_price_list.append(final_pro_price)
            
        print("\nPrice:",cromaPrice)
        print("\n\n\nNow Let's scrape Ajio.........\n")
    except:
        print("Product not found!")