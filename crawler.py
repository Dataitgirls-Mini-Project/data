from selenium.webdriver.common.keys import Keys
import time
from selenium                       import webdriver
from bs4                            import BeautifulSoup
import csv, time, pandas as pd
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

# 스크래핑하고자 하는 url 대입
URL = 'https://ohou.se/productions/482084/selling?affect_type=ProductCategoryIndex&affect_id=](https://ohou.se/productions/482084/selling?affect_type=ProductCategoryIndex&affect_id=)'

driver = webdriver.Chrome()
driver.get(url=URL)

#리뷰 클릭
driver.find_element_by_class_name("production-selling-navigation__item__count").click()
time.sleep(3)

#html 로 파싱
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# 담아줄 리스트 만들기
product_name_list = []
user_name_list = []
total_star_list = [] 
date_list = []
review_list = []
help_list = []
durability_star_list = []
price_star_list = []
design_star_list = []
delievery_star_list = []

# 리뷰 페이지 스크래핑
while True:
    items = driver.find_elements_by_xpath("//div[@class='production-review-item__container']")
    for item in items :
        user_name = item.find_element(By.CSS_SELECTOR,".production-review-item__writer__info__name").text
        total_star = item.find_element(By.CSS_SELECTOR,".production-review-item__writer__info__total-star").get_attribute('aria-label')
        total_star = total_star.split(' ')[1][:-1]
        date = item.find_element(By.CSS_SELECTOR,".production-review-item__writer__info__date").text
        date = date.split(' ')[0]
        review = item.find_element(By.CSS_SELECTOR,".production-review-item__description").text
        
        # 도움이돼요 스크래핑
        try :
            help = item.find_element(By.CSS_SELECTOR,".production-review-item__help__text__number")
            help = help.text
        except NoSuchElementException:
            help = "0"
        
        #디테일 별점 스크래핑
        detail_star = item.find_elements(By.CSS_SELECTOR,".production-review-item__writer__info__detail-star__item")
        if detail_star:
            detail_star_list = []

            for star in detail_star:
                star = star.get_attribute('aria-label')
                star = star.split(' ')[1][:-1]
                detail_star_list.append(star)

            durability_star = detail_star_list[0]
            price_star = detail_star_list[1]
            design_star = detail_star_list[2]
            delievery_star = detail_star_list[3]

        else:
            durability_star = 'null'
            price_star = 'null'
            design_star = 'null'
            delievery_star = 'null'
        
        # 각 값들을 리스트에 append
        user_name_list.append(user_name)
        total_star_list.append(total_star)
        date_list.append(date)
        review_list.append(review)
        help_list.append(help)
        durability_star_list.append(durability_star)
        price_star_list.append(price_star)
        design_star_list.append(design_star)
        delievery_star_list.append(design_star)
        
    # 페이지 이동 버튼 클릭 
    try:
        nxt=driver.find_element_by_xpath('//button[@class="_2XI47 _3I7ex"]')
        nxt.click() 
        time.sleep(1)
    except:
        break  
        
    # 딕셔너리 만들기!
    element_list = {
    'user_name': user_name_list,
    'total_star': total_star_list,
    'durability_star' : durability_star_list,
    'price_star' : price_star_list,
    'design_star' : design_star_list,
    'delievery_star' : delievery_star_list,
    'date' : date_list,
    'review': review_list,
    'help': help_list
    }
    
df = pd.DataFrame(data=element_list, columns=['user_name',
                                              'total_star',
                                              'durability_star',
                                              'price_star',
                                              'design_star',
                                              'delievery_star',
                                              'date', 
                                              'review',
                                              'help'])
df.to_csv('review_top_5.csv')
driver.quit()