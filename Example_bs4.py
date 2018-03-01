from bs4 import BeautifulSoup
from urllib.request import urlopen


html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')
print(html)

soup = BeautifulSoup(html, features='lxml')
print("\n", soup.h1)
print("\n", soup.p)

all_href = soup.find_all('a')
all_href = [l['href'] for l in all_href]
print("\n", all_href)

all_href = soup.find_all('a')
for l in all_href:
    print("\n", l['href'])
