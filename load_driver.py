# -*- coding: utf-8 -*-
import os

from selenium import webdriver


def load_firefox():
    profile_dir = os.path.abspath('firefox_data')
    profile = webdriver.FirefoxProfile(profile_dir)
    # see about:config
    # 设置Firefox的默认下载文件夹。0：桌面；1：“我的下载”；2：自定义
    profile.set_preference('browser.download.folderList', 2)
    # 下载文件保存位置
    profile.set_preference('browser.download.dir', os.path.abspath('download'))
    # True：使用默认下载路径；False：总是询问下载位置
    profile.set_preference('browser.download.useDownloadDir', True)
    # 当下载开始时是否显示下载管理器。True：显示，False：不显示
    profile.set_preference('browser.download.manager.showWhenStarting', False)
    # 无需确认即可下载的文件类型
    profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip, text/csv')
    profile.set_preference('browser.newtabpage.enabled', True)
    profile.set_preference('browser.link.open_newwindow', 3)
    # Firefox Driver
    firefox_driver = r'f:\webdriver\firefox\geckodriver.exe'
    return webdriver.Firefox(firefox_profile=profile, executable_path=firefox_driver)


def load_chrome():
    # 自定义的设置
    user_data_dir = os.path.abspath('chrome_data')
    options = webdriver.ChromeOptions()
    # 指定用户文件夹 User Data 的路径
    options.add_argument('--user-data-dir=' + user_data_dir)
    # 取消沙盒模式
    # options.add_argument('--no-sandbox')
    prefs = dict()
    # 设置禁止弹出下载窗口
    prefs['profile.default_content_settings.popups'] = 0
    # 设置默认下载路径
    prefs['download.default_directory'] = os.path.abspath('download')
    options.add_experimental_option("prefs", prefs)
    # Chrome Driver
    chrome_driver = r'f:\webdriver\chrome\chromedriver.exe'
    return webdriver.Chrome(executable_path=chrome_driver, chrome_options=options)


def load_edge():
    edge_driver = r'f:\webdriver\edge\MicrosoftWebDriver.exe'
    return webdriver.Edge(executable_path=edge_driver)


def load_ie():
    ie_driver = r'f:\webdriver\ie\IEDriverServer.exe'
    return webdriver.Ie(executable_path=ie_driver)
