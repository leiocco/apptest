# author:yuan
# contact: test@test.com
# datetime:2020/7/11 16:20
# software: PyCharm

"""
文件说明：
    
"""
from Mysql.connection import *

sql_delete = "delete from user where id = %d"

try:
    cur.execute(sql_delete % (3))  # 像sql语句传递参数
    # 提交
    db.commit()
except Exception as e:
    # 错误回滚
    db.rollback()
finally:
    db.close()