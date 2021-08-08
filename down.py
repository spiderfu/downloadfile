# -*- coding: utf-8 -*-
'''
@File     : download.py
@Author   : fuzizhu
@Software : PyCharm
@Project  : 代码
@Date     : 2020/12/15 11:08
@Desc     : 
'''
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def down(url, user, pwd, path):
    options = Options()
    options.add_argument('user-agent=ywy')
    options.add_argument("--disable-extensions")
    # 下载路径设置
    prefs = {"download.default_directory": path}
    options.add_experimental_option("prefs", prefs)
    # options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    browser = webdriver.Chrome(
        executable_path="chromedriver.exe", options=options)
    browser.get(url)
    time.sleep(2)
    # 等待两秒，等待页面加载
    browser.find_element_by_css_selector("#loginform-1 > div:nth-child(2) > dl:nth-child(1) > dd > input").send_keys(
        user)
    browser.find_element_by_css_selector("#loginform-1 > div:nth-child(2) > dl:nth-child(2) > dd > input").send_keys(
        pwd)
    browser.find_element_by_css_selector('#loginform-1 > div.btns > input[type="button"]').click()
    time.sleep(2)
    # 等待两秒，等待登录和页面加载

    try:
        browser.find_element_by_css_selector('#btnDownload').click()
        # 点击下载
        time.sleep(2)
        # 等待下载
    except:
        # 如果异地确认登陆
        browser.find_element_by_css_selector('#reLogin > div > div.content > a:nth-child(2)').click()
        time.sleep(2)
        browser.find_element_by_css_selector('#btnDownload').click()
        # 点击下载
        time.sleep(2)
        # 等待下载
    browser.quit()
    # 退出


if __name__ == "__main__":
    # 在这里切换url
    url = 'http://hfggcf518760b87544e9chkpwb609cbbx06vc5.fhbb.libproxy.ruc.edu.cn/foxit-htmlreader-web/Reader.do?fileid=921a38f93e524b0ca543d9d3a3d6465b&lang=zh-cn&pi=255'
    user = '2013000706'
    pwd = 'YOUth999'
    # 保存的地址(绝对路径)
    path = 'E:\spiderfu\工作\朝鲜\代码\download'
    down(url, user, pwd, path)
