# -*- coding: utf-8 -*-

import time

from load_driver import *

# driver = load_firefox()
driver = load_chrome()

try:
    driver.get('file:///' + os.path.abspath('html/scrollbar_test.html'))
    # 最大化浏览器窗口
    # driver.maximize_window()
    time.sleep(2)
    target = driver.find_element_by_id("last_tr")
    driver.execute_script("arguments[0].scrollIntoView();", target)
    time.sleep(5)
except Exception as e:
    print(e)
finally:
    driver.quit()
    pass
