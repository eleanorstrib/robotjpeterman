
from bs4 import BeautifulSoup as bsoup
import requests
import re

r = requests.get("https://www.jpeterman.com/item/wpt-1645/101200310412/silk-palazzo-pants")
doc = r.text

soup = bsoup(doc)

# product name = html/head/title
# keywords = html/head/meta content = , name = "keywords"
# description = html/head/meta content = , name = "description"
name = soup.find("title").string.strip()
keywords = list((soup.find("meta", {"name": "KEYWORDS"})['content'].strip()).split(","))
description = re.sub('<[^<]+?>', '', (soup.find("meta", {"name": "DESCRIPTION"})['content']))

print(name)
print("*" * 40)
print(keywords)
print("*" * 40)
print(description)
print(type(description))
