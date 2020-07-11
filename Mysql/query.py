# author:yuan
# contact: test@test.com
# datetime:2020/7/11 15:53
# software: PyCharm

"""
文件说明：
    
"""
from Mysql.connection import *

# 1.查询操作
# 编写sql 查询语句  user 对应我的表名
sql = "select * from wms_t_saleout limit 50"
try:
    cur.execute(sql)  # 执行sql语句

    results = cur.fetchall()  # 获取查询的所有记录
    print("id", "storehouse_id", "saleout_no", "type", "ext_no")
    # 遍历结果
    for row in results:
        id = row[0]
        storehouse_id = row[1]
        saleout_no = row[2]
        type = row[3]
        ext_no = row[4]
        print(id, storehouse_id, saleout_no, type, ext_no)
except Exception as e:
    raise e
finally:
    db.close()  # 关闭连接

