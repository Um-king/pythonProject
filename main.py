# 네이버 리뷰 가져오기
# https://blog.naver.com/PostView.nhn?blogId=yk02061&logNo=222228280467


# 1. 웹 크롤링 기본 Format 설명

import requests

# ##### 크롤링을 하기 위해 필요한 API 호출
# bs4에 존재하는 BeautifulSoup 모듈을 가져온다. (BeautifulSoup은 Parsing을 위한 모듈)
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd
from tqdm.notebook import tqdm
import time
import re
import sys

from selenium.webdriver.common.keys import Keys # 키보드 키를 제어하는 라이브러리
keys = Keys()


url = 'https://smartstore.naver.com/6032_formen/products/4385167811?NaPm=ct%3Dlfz8v2ps%7Cci%3Dca08e62731269f22805406d9d312f8d8467d07d0%7Ctr%3Dslcc%7Csn%3D659293%7Chk%3Df49e12e8747b149e4d733f22242f328497457fd4'

# 크롬웹드라이버 저장
driver = webdriver.Chrome(executable_path='/Users/user/.ipython/chromedriver.exe')
driver.get(url)

page = requests.get(url)

count = 0
stop = int(input("전체 리뷰 수를 입력해주세요 ")) / 11

# 상품 리뷰 페이지(1,2,...n)를 개발자 도구로 확인하면 해당 규칙으로 작성되어 있다.
next_btn = ['a:nth-child(2)', 'a:nth-child(3)', 'a:nth-child(4)', 'a:nth-child(5)', 'a:nth-child(6)', 'a.fAUKm1ewwo._2Ar8-aEUTq']
review_list = []

while count < stop:
    for pagenum in next_btn:
        driver.find_element_by_css_selector('#REVIEW > div > div._180GG7_7yx > div.cv6id6JEkg > div > div >' +str(pagenum) + '').click()
        time.sleep(2)
        for i in range(0, 20):
            html = driver.page_source
            soup = bs(html, "html.parser")
            review = soup.find_all('div', class_ = '_19SE1Dnqkf')
            review = review[i].text
            review = re.sub('[^0-9a-zA-Zㄱ-ㅎ가-힣]', "", review)
            review_list.append(review)

    count = count + 1

review_list