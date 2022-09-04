import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from bs4 import BeautifulSoup
import re
import json
WAIT = 3
SCROLL_PAUSE_SEC = 1
#options = webdriver.ChromeOptions()
#options.add_argument('headless')


# frame 변경 메소드
def switch_frame(frame,driver):
    driver.switch_to.default_content()  # frame 초기화
    driver.implicitly_wait(1)
    driver.switch_to.frame(frame)  # frame 변경
    driver.implicitly_wait(1)


# 페이지 다운
def page_down(num,driver):
    body = driver.find_element(By.CSS_SELECTOR,'body')
    body.click()
    for i in range(num):
        body.send_keys(Keys.PAGE_DOWN)


def page_up(num, driver):
    body = driver.find_element(By.CSS_SELECTOR,'body')
    body.click()
    for i in range(num):
        body.send_keys(Keys.PAGE_UP)