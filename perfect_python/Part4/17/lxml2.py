import requests
from lxml import etree

res = requests.get("http://rss.rssad.jp/rss/gihyo/feed/atom")
root = etree.fromstring(res.text.encode("utf-8"))

print(root)
