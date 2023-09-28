import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []
Prices = []
Description = []
Reviews = []

for i in range(2, 12):
    url='https://www.flipkart.com'

    r = requests.get(url)

    soup = BeautifulSoup(r.text, "lxml")
    # print(soup)
    box = soup.find('div', class_ = '_1YokD2 _3Mn1Gg')

    names = box.find_all('div', class_ = '_4rR01T')
    # print(names)
    for i in names:
        name = i.text
        Product_name.append(name)

    # print(Product_name)

    prices = box.find_all("div", class_ = "_30jeq3 _1_WHN1")

    for i in prices:
        name=i.text
        Prices.append(name)

    # print(Prices)

    # desc
    desc = box.find_all("ul", class_ = "_1xgFaf")

    for i in desc:
        name=i.text
        Description.append(name)

    # print(Description)


    reviews = box.find_all("div", class_ = "_3LWlk")

    for i in reviews:
        name=i.text
        Reviews.append(name)

    # print(Reviews)

df = pd.DataFrame({"Product Name": Product_name, "Prices": Prices, "Descriptions": Description, "Reviews": Reviews})
# print(df)

df.to_csv("flipkart.csv")













    
    # while True:
    # np= soup.find("a", class_ = "_1LKT03").get("href")
    # cnp = "https://www.flipkart.com"+np
    # print(cnp)

    # url = cnp
    # r = requests.get(url)
    # soup = BeautifulSoup(r.text, "lxml")