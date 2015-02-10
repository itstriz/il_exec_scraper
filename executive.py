#!env/bin/python
from bs4 import BeautifulSoup
from urllib2 import urlopen
import re

def asp_to_md(url):
    BASE_URL = 'http://www.illinois.gov'
    html = urlopen(BASE_URL + url).read()
    soup = BeautifulSoup(html)

    f = open('test_file.txt', 'w')
    f.write(html)
    f.close()

BASE_URL = 'http://www.illinois.gov/Government/ExecOrders/Pages/default.aspx'

html = urlopen(BASE_URL).read()
soup = BeautifulSoup(html)

all_links = soup.findAll('a')
hrefs = []
p = re.compile('^\/Government\/ExecOrders\/Pages\/[0-9]{4}\_[0-9]{2}.aspx$')
for link in all_links:
    if link.has_attr('href') and p.match(link['href']):
        hrefs.append(link['href'])

f = open('executive_orders.txt', 'r+')
data = f.read()
data = data.split('\n')
for href in hrefs:
    if href not in data:
        pass
f.close()

asp_to_md(href[0])
