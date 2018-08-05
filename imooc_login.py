# -*- coding: utf-8 -*-

import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from load_driver import *

from util.Properties import Properties

# driver = load_firefox()
driver = load_chrome()

try:
    driver.get("https://www.imooc.com/")
    # 最大化浏览器窗口
    driver.maximize_window()
    time.sleep(2)
    print(driver.title)
    try:
        # 鼠标移动到头像上
        header_element = driver.find_element_by_xpath('//*[@id="header-avator"]/img')
        ActionChains(driver).move_to_element(header_element).perform()
        element = driver.find_element_by_link_text('安全退出')
        # 点击 安全退出
        element.click()
    except:
        print('尚未登录')

    # 等待登录链接出现
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'js-signin-btn')))
    # 点击 登录 链接
    driver.find_element_by_id("js-signin-btn").click()
    # 等待登录框出现
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.NAME, 'email')))
    # 加载本地属性文件
    local_properties = Properties('local.properties').get_properties()
    driver.find_element_by_name("email").click()
    driver.find_element_by_name("email").clear()
    driver.find_element_by_name("email").send_keys(local_properties['imooc_email'])
    driver.find_element_by_name("password").click()
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(local_properties['imooc_password'])
    # 点击 登录 按钮
    driver.find_element_by_xpath('//input[@value="登录"]').click()
    time.sleep(5)
except Exception as e:
    print(e)
finally:
    driver.quit()
    pass
