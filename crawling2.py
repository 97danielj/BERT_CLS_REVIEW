WAIT = 4
SCROLL_PAUSE_SEC = 1

from find_element import *
from scrollbody import *


def crawling_review_rank(driver):
    #menu_list = list()
    review_list = list()
    review_rank_list = list()
    # -----리뷰 버튼 클릭-------
    try:
        find_review_btn(driver).click()
        sleep(1)
        page_down(1, driver)
        driver.implicitly_wait(WAIT)
        # --------------리뷰, 평점 크롤링 블록--------------------------
        try:
            while True:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(1)
                driver.implicitly_wait(WAIT)
                # 더보기 버튼 클릭
                btn = time_wait(5, 'a.fvwqf', driver)
                if btn != False:
                    btn.click()
                else:
                    break



            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # 리뷰 리스트
            #review_elements = time_wait(10, 'li.YeINN', driver)
            review_elements = driver.find_elements(By.CSS_SELECTOR, "li.YeINN")
            driver.implicitly_wait(SCROLL_PAUSE_SEC)
            sleep(1)
            # 리뷰 텍스트 크롤링
            for i in review_elements:
                try:
                    review_rank = i.find_element(By.CSS_SELECTOR,'span.P1zUJ.HNG_1 > em').text
                    review_rank_list.append(review_rank)
                except:
                    pass
                    continue
                try:
                    review_text = i.find_element(By.CSS_SELECTOR, 'div.ZZ4OK > a > span.zPfVt').text
                    review_list.append(review_text)
                except:
                    review_list.append(None)
                    #review_text = i.find_element(By.CSS_SELECTOR, 'div.ZZ4OK > a > span.zPfVt').text

        except:
            print('리뷰 크롤링중 오류가 났습니다.')
            pass
    except:
        print('리뷰 버튼이 없습니다.')

    return review_list, review_rank_list


def crawling(driver, i, store_elements, review_dic):
    sleep(1)
    store_elements[i].click()  # li의 스토어를 클릭
    driver.implicitly_wait(WAIT)  # 2초 휴식

    try:
        # 다른 iframe으로 변경
        switch_frame('entryIframe', driver)
        sleep(1)
        time_wait(3, 'span.Fc1rA', driver)
        try:
            # -----매장명 가져오기-----
            store_name = driver.find_element(By.CSS_SELECTOR, 'span.Fc1rA').text
            driver.implicitly_wait(2)
            review_dic[store_name] = dict()

        except:
            print('매장명 가져오기 오류')
            pass

        # -----평점 가져오기-----
        try:
            sleep(0.5)
            rank = driver.find_element(By.CSS_SELECTOR, 'div.zD5Nm.f7aZ0 > div.dAsGb > span.PXMot.LXIwF > em')
            driver.implicitly_wait(WAIT)
            review_dic[store_name]['rank'] = rank.text
        except:
            print('평점이 없습니다.')
            pass

        # --------위치 가져오기---------
        try:
            sleep(0.5)
            location = driver.find_element(By.CSS_SELECTOR, 'span.IH7VW').text
            driver.implicitly_wait(WAIT)
            review_dic[store_name]['location'] = location
        except:
            print('위치가져오기 오류')
            pass

        review_list, review_rank_list = crawling_review_rank(driver)

    except:
        print('크롤링 함수 오류가 났습니다.')
        pass

    # 메뉴 크롤링
    #review_dic[store_name]['menu'] = memu_list

    # 방문자 리뷰
    review_dic[store_name]['review'] = review_list
    driver.implicitly_wait(WAIT)

    # 방문자 평점
    review_dic[store_name]['review_rank'] = review_rank_list
    driver.implicitly_wait(WAIT)

    return store_name
