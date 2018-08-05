# -*- coding: utf-8 -*-

import time

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
    # 加载本地属性文件
    local_properties = Properties('local.properties').get_properties()
    # 添加 Cookie
    driver.add_cookie({'name': 'apsid', 'value': local_properties['apsid']})
    # 刷新，变为已登录状态
    driver.refresh()
    time.sleep(5)
except Exception as e:
    print(e)
finally:
    driver.quit()
    pass
