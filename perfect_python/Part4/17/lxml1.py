import requests
from lxml import etree

res = requests.get("http://rss.rssad.jp/rss/gihyo/feed/atom")
open("gihyo.xml", "wb").write(res.content)
tree = etree.parse("gihyo.xml")
root = tree.getroot()

print(root)
