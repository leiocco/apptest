# author:yuan
# contact: test@test.com
# datetime:2020/6/24 14:01
# software: PyCharm

"""
文件说明：连接真机终端
"""
from appium import webdriver
"""
文件说明：设备信息
"""
desired_caps = {}
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "6.0"
desired_caps["deviceName"] = "android_50_series-1448102"
"""
文件说明：测试包信息
"""
desired_caps["appPackage"] = "com.gengcon.android.wms"
desired_caps["appActivity"] = "com.gengcon.android.wms.ui.SplashActivity"
desired_caps["automationName"] = "UiAutomator1"
"""
文件说明：远程连接
"""
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
"""
文件说明：连接等待
"""
driver.implicitly_wait(10)