# -*- coding: utf-8 -*-
import csv
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from load_driver import *

driver = load_firefox()
# driver = load_chrome()

csv_file = 'comments.csv'
try:
    driver.get("https://www.bilibili.com/video/av22957730")
    # 滚动到 comment 元素
    target = driver.find_element_by_class_name("comment")
    driver.execute_script("arguments[0].scrollIntoView();", target)
    print(driver.title)
    # 写入 CSV 标题
    with open(csv_file, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f, dialect='excel')
        writer.writerow(['楼层', '来源', '评论时间', '用户名', '评论内容'])

    # 获取所有评论
    while True:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'list-item')))
        comments = target.find_elements_by_xpath('.//div[@class="comment-list"]/div[contains(@class,"list-item")]')
        print('comments count', len(comments))
        for comment in comments:
            # 楼层
            floor = comment.find_element_by_xpath('./div[2]/div[@class="info"]/span[@class="floor"]').text
            # 评论来源（来自安卓客户端 or ...）
            plad = ''
            try:
                plad = comment.find_element_by_xpath('./div[2]/div[@class="info"]/span[@class="plad"]').text
            except:
                pass
            # 评论时间
            comment_time = comment.find_element_by_xpath('./div[2]/div[@class="info"]/span[@class="time"]').text
            # 用户名
            username = comment.find_element_by_xpath('./div[2]/div[@class="user"]/a[1]').text
            # 评论内容
            text = comment.find_element_by_xpath('./div[2]/p[@class="text"]').text
            print('floor', floor)
            print('plad', plad)
            print('comment_time', comment_time)
            print('username', username)
            print('text', text)
            row = [floor, plad, comment_time, username, text]
            with open(csv_file, 'a', newline='', encoding='utf-8-sig') as f:
                writer = csv.writer(f, dialect='excel')
                writer.writerow(row)
        try:
            # 点击 下一页
            driver.find_element_by_link_text('下一页').click()
            time.sleep(3)
        except:
            print('没有下一页了')
            break

    time.sleep(5)
except Exception as e:
    print(e)
finally:
    driver.quit()
    pass
