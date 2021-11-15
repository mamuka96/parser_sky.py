import requests
from bs4 import BeautifulSoup

url = 'https://www.networkworld.com/'


news_network = []
def parser():

    response = requests.get(url).text
    soup = BeautifulSoup(response, 'lxml')

    posts = soup.find_all('a', class_='item-text')


    for item in posts:
        date = {'title': item.get_text(strip=True),
                 'link': url + item['href']}
        news_network.append(date)

get_network_world()
