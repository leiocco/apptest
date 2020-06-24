# author:yuan
# contact: test@test.com
# datetime:2020/6/24 13:59
# software: PyCharm

from start import *
"""
文件说明：WMS登录
"""
el1 =driver.find_element_by_id("com.gengcon.android.wms:id/et_phone")
el1.send_keys("17362313866")
el2 =driver.find_element_by_id("com.gengcon.android.wms:id/et_pwd")
el2.send_keys("aa123456")
driver.hide_keyboard()
el3 =driver.find_element_by_id("com.gengcon.android.wms:id/btn_login")
el3.click()

