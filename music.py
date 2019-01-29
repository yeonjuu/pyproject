from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from datetime import datetime 
import requests

# options = webdriver.ChromeOptions()
# options.add_argument("--disable-notifications")

# driver = webdriver.Chrome('C:\\Users\\COM\\chromedriver_win32\\chromedriver', options = options)
# sleep(3)

# driver.get('https://www.melon.com/chart/index.htm')

# html = driver.page_source # 페이지의 elements모두 가져오기
# soup = BeautifulSoup(html, 'html.parser') 
# titles = soup.select('#lst50 > td:nth-child(6) > div > div >span >a')

# print(titles)

# ranks = driver.find_element_by_xpath('//*[@id="frm"]/div')
# print("table:"  + ranks.text)


# ranks = driver.find_element_by_class_name('bullet_icons rank_static')

# print("table:"  + ranks.text)

url = "https://music.naver.com/listen/top100.nhn?domain=TOTAL_V2"
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, "html.parser")

ranks = soup.select(
    'td.change'
)

change = []
for rank in ranks :
    change.append(rank.text)

# for i in range(len(change)) :
#     print(change[i], end='')

print(change)