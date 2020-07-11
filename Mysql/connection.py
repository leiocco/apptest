# author:yuan
# contact: test@test.com
# datetime:2020/7/11 15:55
# software: PyCharm

"""
文件说明：
    
"""

import pymysql  # 导入 pymysql

# 打开数据库连接
db = pymysql.connect(host="10.10.13.120",user="wms",password="wms",db="wms",port=3306)

# 使用cursor()方法获取操作游标
cur = db.cursor()