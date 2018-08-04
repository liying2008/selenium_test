# -*- coding: utf-8 -*-

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from load_driver import *

driver = load_firefox()
# driver = load_chrome()

try:
    driver.get("https://www.bilibili.com/")
    input_ele = driver.find_element_by_xpath('//*[@id="banner_link"]/div/div/form/input')
    print(driver.title)
    # 搜索
    input_ele.send_keys('承君')
    input_ele.send_keys(Keys.ENTER)
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[-1])
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'all-contain')))
    print(driver.title)
    driver.find_element_by_link_text('【祖娅纳惜·FRE】承君（这是我今年听到的最喜欢的古风歌你们看我都来当标题党了！）').click()
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(2)
    print(driver.title)
    # 最大化浏览器窗口
    driver.maximize_window()
    # 点击开始播放
    driver.find_element_by_xpath('//div[@class="bilibili-player-video"]').click()
    time.sleep(1)
    # 全屏播放
    driver.find_element_by_xpath('//i[@name="browser_fullscreen"]').click()
    time.sleep(5)
    # 退出全屏
    driver.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)
    time.sleep(5)
except Exception as e:
    print(e)
finally:
    driver.quit()
    pass
