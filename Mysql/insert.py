# author:yuan
# contact: test@test.com
# datetime:2020/7/11 16:18
# software: PyCharm

"""
文件说明：
    
"""
from Mysql.connection import *

sql_insert = """insert into user(id,username,password) values(4,'liu','1234')"""

try:
    cur.execute(sql_insert)
    # 提交
    db.commit()
except Exception as e:
    # 错误回滚
    db.rollback()
finally:
    db.close()