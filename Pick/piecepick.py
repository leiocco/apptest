# author:yuan
# contact: test@test.com
# datetime:2020/6/24 14:02
# software: PyCharm

"""
文件说明：单个拣货
"""
from Pick.login import *
"""
文件说明：进入拣货
"""
el1 =driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[3]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.TextView")
el1.click()
"""
文件说明：筛选出待拣货&货票分开的订单
"""
el2 =driver.find_element_by_id("com.gengcon.android.wms:id/tv_right")
el2.click()
el3 =driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.GridView[1]/android.widget.RelativeLayout[2]/android.widget.TextView")
el3.click()
el4 =driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.GridView[2]/android.widget.RelativeLayout[1]/android.widget.TextView")
el4.click()
el5 =driver.find_element_by_id("com.gengcon.android.wms:id/tv_define")
el5.click()
"""
文件说明：绑定拣货蓝
"""
el6 =driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.LinearLayout")
el6.click()
el7 =driver.find_element_by_id("com.gengcon.android.wms:id/et_code")
el7.send_keys("JHL0001")#绑定拣货蓝
el8 = driver.find_element_by_id("com.gengcon.android.wms:id/et_code")
el8.click()
driver.press_keycode(66);
"""
文件说明：开始拣货
"""
