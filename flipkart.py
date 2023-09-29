import requests
from bs4 import BeautifulSoup
import pandas as pd

phone_name = []
phone_prices = []

page_number = input("Enter the number of pages: ")
for i in range(1, int(page_number)+1):
    url="https://www.flipkart.com/search?q=iphone+15&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page="+str(i)
    req = requests.get(url)
    content= BeautifulSoup(req.content, 'html.parser')
#     print(content)
    name= content.find_all('div', {"class": '_4rR01T'})
    price = content.find_all('div', {"class": "_30jeq3 _1_WHN1"})
    print(len(name))
    
    for i in name:
        phone_name.append(i.text)
    for i in price:
        phone_prices.append(i.text)

for i in phone_name:
    print(i)

for i in phone_prices:
    print(i)

# phone_name = []
# phone_prices = []

# product = input("Enter the product name: ")
# name = product.replace(" ","+")

# url="https://www.flipkart.com/search?q="+str(name)
# req = requests.get(url)
# content= BeautifulSoup(req.content, 'html.parser')
# #     print(content)
# name= content.find('div', {"class": '_4rR01T'})
# price = content.find('div', {"class": "_30jeq3 _1_WHN1"})
# print(len(name))
    
# for i in name:
#     phone_name.append(i.text)
# for i in price:
#     phone_prices.append(i.text)

data={'phone name': phone_name, "phone prices": phone_prices}
df=pd.DataFrame(data)
print(df)