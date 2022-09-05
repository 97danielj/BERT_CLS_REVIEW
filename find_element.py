
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

WAIT = 3
SCROLL_PAUSE_SEC = 1


# css 찾을때 까지 10초대기
def time_wait(num, code,driver):
    try:
        wait = WebDriverWait(driver, num).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, code)))
    except:
        print(code, '태그를 찾지 못하였습니다.')
        driver.quit()
    return wait



def find_search_input(key_word,driver):
    # 검색창 찾기
    driver.switch_to.default_content()
    time_wait(2, 'div.input_box > input.input_search',driver)
    search = driver.find_element(By.CSS_SELECTOR,'div.input_box > input.input_search')
    search.send_keys(key_word)  # 검색어 입력
    driver.implicitly_wait(3)
    search.send_keys(Keys.ENTER)  # 엔터버튼 누르기
    sleep(5)
    #res = driver.page_source  # 페이지 소스 가져오기
    #soup = BeautifulSoup(res, 'html.parser')  # html 파싱하여  가져온다
    #sleep(1)


def find_review_btn(driver):
    sleep(2)
    try:
        menu_list = driver.find_elements(By.CSS_SELECTOR,'a.tpj9w')
        driver.implicitly_wait(3)
        #개수가 7개인 경우 리뷰 버튼 고정되어있지 않다.
        if len(menu_list) == 7:
            if menu_list[-1].text == '리뷰':
                return menu_list[-1]
            elif menu_list[-2].text == '리뷰':
                return menu_list[-2]
            else:
                return menu_list[-3]
        else:
            return menu_list[-2]
    except:
        print('리뷰버튼이 존재하지 않습니다.')




def find_page_btn(driver, page_num):
    pages = driver.find_elements(By.CSS_SELECTOR, 'a.mBN2s')
    if page_num <= 5:
        pages[page_num].click()
        sleep(1)
    else:
        driver.find_elements(By.CSS_SELECTOR, 'div.zRM9F > a:nth-child(6)').click()
        driver.implicitly_wait(WAIT)
        driver.find_element(By.CSS_SELECTOR, 'div.zRM9F > a:nth-child(6)').click()
        driver.implicitly_wait(WAIT)