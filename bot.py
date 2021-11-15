import telebot
import requests
from bs4 import BeautifulSoup
import time

token = '2065382655:AAGBGh1tAz68DJXfYu3j8z2zbKT90YRGdY8'
id_channel = '@sky_footboll'
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def commands(message):
    back_post_id = 0
    while True:
        post_text = parser(back_post_id)
        bot.send_message(id_channel, message.text)

bot.polling()

url = 'https://www.networkworld.com/'
news_network = []
def parser(back_post_id):

    response = requests.get(url).text
    soup = BeautifulSoup(response, 'lxml')

    posts = soup.find_all('a', class_='item-text', id=True)
    posts_id = id(posts)
    if posts_id != back_post_id:
        for item in posts:
            date = {'title': item.get_text(strip=True),
                     'link': url + item['href']}
            news_network.append(date)
        return news_network
    else:
        return None, posts_id

parser()