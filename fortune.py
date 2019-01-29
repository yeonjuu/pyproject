import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

year = '19981221'

driver = webdriver.Chrome('C:\\Users\\COM\\chromedriver_win32\\chromedriver')
driver.get("https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%98%A4%EB%8A%98%EC%9D%98+%EC%9A%B4%EC%84%B8")
#input_year = driver.find_element_by_name_id('srch_txt').send_keys('19981221')

input_year = driver.find_element_by_xpath('//*[@id="srch_txt"]')
input_year.send_keys("19981221")

click_btn = driver.find_element_by_xpath('//*[@id="fortune_birthCondition"]/div[1]/fieldset/input').click()
time.sleep(3)

fortune1 = driver.find_element_by_xpath('//*[@id="fortune_birthResult"]/dl[1]/dd/p')
print("★총운★\n"+fortune1.text)

time.sleep(3)
driver.find_element_by_class_name('birth_love').click()
fortune2 = driver.find_element_by_xpath('//*[@id="fortune_birthResult"]/dl[1]/dd/p')
print("♥애정운♥\n"+fortune2.text)

time.sleep(3)
driver.find_element_by_class_name('birth_money').click()
fortune3 = driver.find_element_by_xpath('//*[@id="fortune_birthResult"]/dl[1]/dd/p')
print("§금전운§\n"+fortune3.text)

time.sleep(3)
driver.find_element_by_class_name('birth_company').click()
fortune4 = driver.find_element_by_xpath('//*[@id="fortune_birthResult"]/dl[1]/dd/p')
print("♨직장운♨\n"+fortune4.text)

time.sleep(3)
driver.find_element_by_class_name('birth_study').click()
fortune5 = driver.find_element_by_xpath('//*[@id="fortune_birthResult"]/dl[1]/dd/p')
print("♬학업운♬\n"+fortune5.text)


