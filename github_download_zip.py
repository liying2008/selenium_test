# -*- coding: utf-8 -*-

import time

from load_driver import *

# driver = load_firefox()
driver = load_chrome()

try:
    driver.get("https://github.com/liying2008/SmartisanDialog")
    # 最大化浏览器窗口
    driver.maximize_window()
    time.sleep(2)
    print(driver.title)
    # 点击 Clone or download
    driver.find_element_by_xpath('//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[5]/details/summary').click()
    # 点击 Download ZIP
    driver.find_element_by_link_text("Download ZIP").click()
    time.sleep(5)
except Exception as e:
    print(e)
finally:
    driver.quit()
    pass
