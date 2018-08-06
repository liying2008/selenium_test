# -*- coding: utf-8 -*-

import time

from load_driver import *

driver = load_firefox()
# driver = load_chrome()

try:
    driver.get('https://developer.android.google.cn/reference/android/support/packages')
    # 最大化浏览器窗口
    driver.maximize_window()
    right_target = driver.find_element_by_partial_link_text('微信')
    driver.execute_script("arguments[0].scrollIntoView();", right_target)
    time.sleep(2)
    left_target = driver.find_element_by_xpath('//*[@id="gc-wrapper"]/div[2]/nav[1]/ul/li[last()]')
    driver.execute_script("arguments[0].scrollIntoView();", left_target)
    time.sleep(5)
except Exception as e:
    print(e)
finally:
    driver.quit()
    pass
