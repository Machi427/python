import requests
from bs4 import BeautifulSoup

res = requests.get("http://gihyo.jp/")
soup = BeautifulSoup(res.text)


print(soup)
