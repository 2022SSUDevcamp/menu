#데이터베이스 라이브러리
from xmlrpc.client import DateTime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import DB
import datetime
from sqlalchemy.sql import func


#크롤링 라이브러리
from bs4 import BeautifulSoup
from datetime import date
import urllib.request

#텔레그램 라이브러리
import telegram
bot = telegram.Bot(token="5324060418:AAE5dfUkJn7s9SVMf5IagypfsqCXFQwbbgg")

#데이터 수집
url = "https://ssudorm.ssu.ac.kr:444/SShostel/mall_main.php?viewform=B0001_foodboard_list&board_no=1"
res = urllib.request.urlopen(url).read()
soup = BeautifulSoup(res, "html.parser")

table = soup.find("table", attrs={"class": "boxstyle02"})
dorm_trs = table.find_all("tr")

dorm_today = date.today().weekday() + 1
for index, dorm in enumerate(dorm_trs[dorm_today].find_all("td")):
    if index == 0:
            print("\n\n[아침]\n" + dorm.text.strip()) 
            brunch=dorm.text.strip()                    #텔레그램 메시지로 보내기 위해 아침, 점심, 저녁으로 구분
            repo=DB.Repo()                              
            repo.add_crawling_data(brunch)              #데이터베이스 저장
    elif index == 1:
            print("\n\n[점심]]\n" + dorm.text.strip())
            lunch=dorm.text.strip()
            repo=DB.Repo()
            repo.add_crawling_data(lunch)
    elif index == 2:
            print("\n\n[저녁]\n" + dorm.text.strip()) 
            dinner=dorm.text.strip()
            repo=DB.Repo()
            repo.add_crawling_data(dinner)
            #텔레그램 메시지로 보낸다. 
            bot.send_message(5622685016, "[아침]\n" + brunch + "\n\n[점심]\n" + lunch + "\n\n[저녁]\n" + dinner)