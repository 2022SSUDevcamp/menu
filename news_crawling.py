from unittest import result
from bs4 import BeautifulSoup
import telegram
import requests
import datetime

token = "5324060418:AAE5dfUkJn7s9SVMf5IagypfsqCXFQwbbgg" #token
receiver_id = 5622685016 # Chat_id
bot = telegram.Bot(token = token)

def sendMessage(chat_id, message):
    bot.sendMessage(chat_id = chat_id, text=message)


def crawling() :
    # soup 객체에서 추출해야 하는 정보를 찾고 반환하세요.
    custom_header = {
        'referer' : 'https://www.naver.com/',
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    url = "http://www.naver.com"
    req = requests.get(url, headers = custom_header)
    soup = BeautifulSoup(req.text, "html.parser")

    div = soup.find("div", class_="list_issue")

    news_title = []
    for a in div.find_all("a"):
        news_title.append(a.get_text())

    news_urls = []
    
    for new in div.find_all("a"):
        news_url= new.attrs['href']
        news_urls.append(news_url)

    result = []

    for i,j in zip(news_title, news_urls):
        result.append("" + i + j + "\n")

    return " ".join(result)


def date_extract():
    current = datetime.datetime.today()
    today_time = current + datetime.timedelta(hours=9)
    today_time = today_time.strftime("%Y/%m/%d") + " 많이 읽은 경제뉴스 TOP 10"
    return today_time    

def main() :
    today_news = crawling()
    date = date_extract()

    date_news = date, today_news

    for n in date_news:
        bot.sendMessage(chat_id=receiver_id, text=n)

    # crawling 함수의 결과를 출력합니다.
    # print(crawling())


if __name__ == "__main__" :
    main()