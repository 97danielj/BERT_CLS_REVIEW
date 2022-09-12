#options = webdriver.ChromeOptions()
#options.add_argument('headless')

from crawling import *
from find_element import *
from scrollbody import *

WAIT = 3
SCROLL_PAUSE_SEC = 1


def naver_crawling(key_word, page_num, ck_pt_idx = 0):
    print(f'---------------{key_word}크롤링을 시작합니다.------------------')

    # 매장 정보를 저장할 딕셔너리 구조체
    review_dic = dict()
    if ck_pt_idx != 0:
        with open(f'./naver/naver_{key_word}_review_dic_page{page_num}.json', 'r', encoding='utf-8') as f:
            review_dic = json.load(f)

    page_num = page_num - 1

    #크롬 드라이버 열기
    #options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    url = 'https://map.naver.com/v5/search'
    driver = webdriver.Chrome('./chromedriver')
    driver.get(url)
    driver.implicitly_wait(2)
    driver.maximize_window()
    driver.implicitly_wait(WAIT)
    sleep(WAIT)

    #검색창 찾기
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

    if ck_pt_idx == 0:
        page_up(40, driver)
        sleep(SCROLL_PAUSE_SEC)
        page_up(5,driver)
        sleep(SCROLL_PAUSE_SEC)
    store_elements = driver.find_elements(By.CSS_SELECTOR, 'div.ouxiq > a:nth-child(1)')
    print('total store_list : ', len(store_elements))  # 매장리스트 접근

    while True: # refresh 반복뮨
        while True: # 매장 접근을 위한 반복문
            try:
                store_name = crawling(driver, ck_pt_idx, store_elements, review_dic)
                print('현재 크롤링 중인 매장 인덱스와 매장명 : ', ck_pt_idx, store_name)
                #마지막 매장인 경우
                if ck_pt_idx == len(store_elements) -1:
                    break

                sleep(0.5)
                switch_frame('searchIframe', driver)
                # 리뷰가 많을 경우 refresh()를 위해 벗어나는 조건문
                if len(review_dic[store_name]['review']) >= 500:
                    break
                else:
                    ck_pt_idx += 1

            # 예상치 못한 오류가 뜨는 경우
            except:
                # json파일 저장
                with open(f'./naver/naver_{key_word}_review_dic_page{page_num + 1}.json', 'w', encoding='utf-8') as f:
                    json.dump(review_dic, f, indent=4, ensure_ascii=False)
                #현재 driver는 닫기
                driver.close()
                #오류난 위치 반환
                return ck_pt_idx


        # 새로고침 반복을 나오는 조건문
        if ck_pt_idx == len(store_elements) - 1:
            break
        else:
            ck_pt_idx += 1

        print('새로고침을 진행합니다.')
        driver.refresh()
        driver.implicitly_wait(WAIT)
        sleep(0.5)
        driver.refresh()
        driver.implicitly_wait(WAIT)
        sleep(0.5)
        switch_frame('searchIframe', driver)
        find_page_btn(driver, page_num)

        sleep(SCROLL_PAUSE_SEC)
        page_down(40, driver)
        sleep(SCROLL_PAUSE_SEC)
        driver.implicitly_wait(SCROLL_PAUSE_SEC)
        page_down(5, driver)
        sleep(SCROLL_PAUSE_SEC)
        store_elements = driver.find_elements(By.CSS_SELECTOR, 'div.ouxiq > a:nth-child(1)')
        print('total store_list', len(store_elements))

    print('크롤링을 저장하고, 종료합니다.')
    # json 파일로 저장
    with open(f'./naver/naver_{key_word}_review_dic_page{page_num + 1}.json', 'w', encoding='utf-8') as f:
        json.dump(review_dic, f, indent=4, ensure_ascii=False)

    driver.close()
    sleep(WAIT)
    return

key_word_list = ['서울 횟집','인천 횟집', '부산 횟집', '대구 횟집', '광주 횟집', '대전 횟집', '울산 횟집']
#key_word_list = ['부산 횟집', '대구 횟집', '광주 횟집', '대전 횟집', '울산 횟집']
'''for page_num in range(4,7):
    for key_word in key_word_list:
        naver_crawling(key_word, page_num)
'''
naver_crawling(key_word_list[-1], 3)












