WAIT = 3
SCROLL_PAUSE_SEC = 1

from find_element import *
from scrollbody import *


def crawling_menu_review(driver):
    # -----리뷰 버튼 클릭-------
    find_review_btn(driver).click()
    sleep(1)
    page_down(1, driver)
    driver.implicitly_wait(WAIT)
    # ----------------메뉴, 크롤링 블록----------------
    menu_list = list()
    review_list = list()
    # 메뉴, 크롤링 블록을 포함하는 try-except문
    try:
        # --------------메뉴 크롤링 블록--------------------------
        # 메뉴 요소 찾기
        menu_elements = driver.find_elements(By.CSS_SELECTOR, 'div.place_fixed_subtab > div > div:nth-child(1) > div > div > div > span > a > span:first-child')
        sleep(SCROLL_PAUSE_SEC)
        try:
            # 왼쪽 버튼 찾기
            left_btn = driver.find_element(By.CSS_SELECTOR, 'a.PznE8.aNw43')
            driver.implicitly_wait(WAIT)
            left_btn.click()
            driver.implicitly_wait(WAIT)
        except:
            pass

        try:
            # 오른족 버튼 찾기
            right_btn = driver.find_element(By.CSS_SELECTOR, 'div.place_fixed_subtab > div > div:nth-child(1) > div > div > a.ZCqf_.aNw43')
            driver.implicitly_wait(WAIT)
        except:
            pass
        # -----------여기까지--------------
        i = 0
        # menu_elentents가 존재하지 않는다면 except로 갈 것이다.
        try:
            while True:
                if menu_elements[i].text != '':  # 요소가 존재하고 메뉴 텍스트도 보일때
                    menu_list.append(menu_elements[i].text)
                    if i == len(menu_elements) - 1:  # 메뉴 리스트 길이면 나온다.
                        break
                    i += 1
                else:
                    right_btn.click()
                    sleep(SCROLL_PAUSE_SEC)
                    driver.implicitly_wait(WAIT)
        except:
            pass

        # last_scroll = driver.execute_script("return document.body.scrollHeight")
        # view_more_count = 0

        # --------------리뷰 크롤링 블록--------------------------
        try:
            while True:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(1)
                driver.implicitly_wait(WAIT)

                # if view_more_count ==19:
                # break
                try:
                    # 더보기 버튼 클릭
                    driver.implicitly_wait(WAIT)
                    driver.find_element(By.CSS_SELECTOR, 'a.fvwqf').click()
                    # view_more_count += 1

                except:
                    # 더보기 버튼이 없다면 while문을 빠져나온다.
                    break
                    # 끝까지 스크롤 다운

                # new_scroll = driver.execute_script("return document.body.scrollHeight")
                # driver.implicitly_wait(WAIT)
                # if last_scroll == new_scroll:
                #    break
                # else:
                #    last_scroll= new_scroll

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # 가게 리스트 마다 방문자 리뷰 가져오기
            review_elements = driver.find_elements(By.CSS_SELECTOR, "span.zPfVt")
            sleep(1)
            for i in review_elements:
                review_list.append(i.text)
        except:
            print('리뷰 크롤링중 오류가 났습니다.')
            pass

    except:
        print('메뉴 & 리뷰 크롤링중 오류가 났습니다.')
        pass

    return menu_list, review_list


def crawling(driver, i, store_elements, review_dic):
    sleep(1)
    store_elements[i].click()  # li의 스토어를 클릭
    driver.implicitly_wait(WAIT)  # 2초 휴식
    return_name = None
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

        memu_list, review_list = crawling_menu_review(driver)

    except:
        print('크롤링 함수 오류가 났습니다.')
        pass

    # 메뉴 크롤링
    review_dic[store_name]['menu'] = memu_list

    # 방문자 리뷰 크롤링
    review_dic[store_name]['review'] = review_list
    driver.implicitly_wait(WAIT)

    return store_name
