from bs4 import BeautifulSoup as Bs
import requests
from fake_useragent import UserAgent
import pandas as pd
import csv
import json

ua = UserAgent()
headers = {"User-Agent": ua.chrome}
url = "https://cars.av.by/hyundai/solaris"
html = requests.get(url).text
soup = Bs(html, 'html.parser')
req = requests.get(url, headers=headers)

# print(soup.prettify())
#
# print('HTML', soup.h2)
# print('HTML', soup.h2.text)
# print('HTML', soup.h2.name)

div = soup.find_all("div", class_="listing-item")

data = []

for car in div:
    link = "https://cars.av.by" + car.find("a", class_="listing-item__link").get("href")
    params = car.find("div", class_="listing-item__params").text
    price_byn = car.find("div", class_="listing-item__prices").find("div", class_="listing-item__price").text
    price_usd = car.find("div", class_="listing-item__prices").find("div", class_="listing-item__priceusd").text

    data.append([link, params, price_byn, price_usd])

header = ["Ссылка", "Характеристики", "цена byn", "цена usd"]
df = pd.DataFrame(data, columns=header)
df.to_csv("data.csv", sep=";", encoding="UTF-8")


for i in data:
    print(i)

with open("ex.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False)