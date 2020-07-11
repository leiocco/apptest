# author:yuan
# contact: test@test.com
# datetime:2020/6/24 17:17
# software: PyCharm

"""
文件说明： 启动web WMS页面
"""
from selenium import webdriver

driver = webdriver.Chrome('D:\ChromDriver\chromedriver.exe')
driver.get('http://pc.wms.jc-test.cn')