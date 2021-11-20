import requests
from bs4 import BeautifulSoup
import json
import time

url = 'https://www.networkworld.com/'

OUT_FILENAME = 'out.json'
news_network = []
def parser():

    response = requests.get(url).text
    soup = BeautifulSoup(response, 'lxml')

    posts = soup.find_all('a', class_='item-text')
    img = soup.find_all('a', class_='well-img')

    for item in posts:
        date = {'title': item.get_text(strip=True),
                'link': url + item['href'],
                }
        news_network.append(date)
        return print(news_network)
# parser()

with open(OUT_FILENAME, 'w') as f:
    json.dump(news_network, f, indent=1)


