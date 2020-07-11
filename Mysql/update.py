# author:yuan
# contact: test@test.com
# datetime:2020/7/11 16:19
# software: PyCharm

"""
文件说明：
    
"""
from Mysql.connection import *

sql_update = "update user set username = '%s' where id = %d"

try:
    cur.execute(sql_update % ("xiongda", 3))  # 像sql语句传递参数
    # 提交
    db.commit()
except Exception as e:
    # 错误回滚
    db.rollback()
finally:
    db.close()
