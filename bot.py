import requests
from bs4 import BeautifulSoup
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN
import json
import time

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
chat_id = '@sky_footboll'
url = 'https://www.networkworld.com/'
news_network = []
OUT_FILENAME = 'out.json'


def parser():
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'lxml')

    posts = soup.find_all('a', class_='item-text')

    for item in posts:
        date = {'title': item.get_text(strip=True),
                'link': url + item['href']}

        with open(OUT_FILENAME, 'w') as f:
            json.dump(news_network, f, indent=1)

            for key in date.keys():
                date[key] = date[key].replace('\n', '')
                date[key] = date[key].replace('\t', '')
        news_network.append(date)

parser()

def ttime():
    parser()
    while True:
        time.sleep(5)
ttime()





@dp.message_handler(commands=['get_news'])
async def send_file(message: types.Message):
    with open('out.json') as file:
        news_network = json.load(file)
        await message.answer(news_network)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

