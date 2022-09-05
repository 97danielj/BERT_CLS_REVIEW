from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import re
import json


#options = webdriver.ChromeOptions()
#options.add_argument('headless')

from crawling import *
from find_element import *
from scrollbody import *

WAIT = 3
SCROLL_PAUSE_SEC = 1


def main(key_word, page_num):
    review_dic = dict()
    page_num = page_num - 1
    #refresh_count = 0

    url = 'https://map.naver.com/v5/search'
    driver = webdriver.Chrome('./chromedriver')
    driver.get(url)
    driver.implicitly_wait(2)

    # 검색어 입력
    find_search_input(key_word, driver=driver)
    driver.implicitly_wait(2)

    # 프레임 변경
    switch_frame('searchIframe', driver)
    sleep(0.5)

    # 페이지 버튼 찾기
    find_page_btn(driver, page_num)
    driver.implicitly_wait(WAIT)
    page_down(40, driver)
    sleep(SCROLL_PAUSE_SEC)
    driver.implicitly_wait(SCROLL_PAUSE_SEC)
    page_down(5, driver)
    sleep(SCROLL_PAUSE_SEC)
    page_up(40,driver)
    sleep(SCROLL_PAUSE_SEC)
    page_up(5,driver)
    sleep(SCROLL_PAUSE_SEC)
    store_elements = driver.find_elements(By.CSS_SELECTOR, 'div.ouxiq > a:nth-child(1)')
    print('total store_list : ', len(store_elements))  # 매장리스트 접근
    # 체크포인트
    ck_pt_idx = 0

    while True:
        while True:
            try:  # 이상한 오류가 뜰경우 현재위치 까지 저장 하고, 크롤링 인덱스 반환
                store_name = crawling(driver, ck_pt_idx, store_elements, review_dic)
                print('현재 크롤링 중인 매장 인덱스와 매장명 : ', ck_pt_idx,store_name)
                ck_pt_idx += 1
                sleep(0.5)
                switch_frame('searchIframe', driver)


                # 한 refresh를 벗어나는 조건문
                if len(review_dic[store_name]['review']) >= 500:
                    break

            except:
                # json 파일로 저장
                with open(f'./Crawling2/naver_{key_word}_review_dic_page{page_num + 1}.json', 'w', encoding='utf-8') as f:
                    json.dump(review_dic, f, indent=4, ensure_ascii=False)
                return ck_pt_idx

        # 페이지의 크롤링을 나오는 조건문
        if ck_pt_idx == len(store_elements) - 1:
            break

        print('새로고침을 진행합니다.')
        driver.refresh()
        driver.implicitly_wait(WAIT)
        switch_frame('searchIframe', driver)
        find_page_btn(driver, page_num)

        sleep(SCROLL_PAUSE_SEC)
        page_down(40, driver)
        sleep(SCROLL_PAUSE_SEC)
        driver.implicitly_wait(1)
        page_down(5, driver)
        sleep(SCROLL_PAUSE_SEC)
        store_elements = driver.find_elements(By.CSS_SELECTOR, 'div.ouxiq > a:nth-child(1)')
        print('total store_list', len(store_elements))

    print('크롤링을 저장하고, 종료합니다.')
    # json 파일로 저장
    with open(f'./Crawling2/naver_{key_word}_review_dic_page{page_num + 1}.json', 'w', encoding='utf-8') as f:
        json.dump(review_dic, f, indent=4, ensure_ascii=False)

key_word_list = ['서울 횟집', '인천 횟집', '부산 횟집', '대구 횟집', '광주 횟집', '대전 횟집', '울산 횟집']
main(key_word_list[0],2)


