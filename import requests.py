import requests
from bs4 import BeautifulSoup
import telegram

my_token = '2062236097:AAEbmTzXP0b0gl4BKlHGMuqH2gKqqXyOMlc'
bot = telegram.Bot(token = my_token)
chat_id = bot.getUpdates()[-1].message.chat.id #가장 최근에 온 메세지의 chat id를 가져옵니다

url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20211029'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
list = soup.select('.info-hall')
if '듄' in html and 'IMAX' in str(list):
    bot.sendMessage(chat_id = chat_id, text = "예매 가능")