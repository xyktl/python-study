# -*- coding: utf-8 -*-
import sqlite3
import os

# 获取文件所在目录的完整路径：os.path.dirname(__file__)
db_file = os.path.join(os.path.dirname(__file__), "test.tb")
if os.path.isfile(db_file):
    os.remove(db_file)
conn = sqlite3.connect("db_file")
cursor = conn.cursor()
cursor.execute("drop table user")  # 删除一个表格（table）
cursor.execute("create table if not exists user (id varchar(20) primary key,name varchar(20),score int)")
# insert 操作
cursor.execute("insert into user values('1', 'Mike','99')")
cursor.execute("insert into user values('2','Job','90')")
cursor.execute("insert into user values('3','Lisa','100')")
cursor.close()
conn.commit()  # 提交事务
conn.close()


def get_name_in(low, high):
    '''返回指定分数之间的名字，按分数从低到高排序'''
    conn = sqlite3.connect("db_file")
    cursor = conn.cursor()
    # select 查找操作
    cursor.execute("select name,score from user where score>=? and score<=?", (low, high))
    # featchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录。
    values = cursor.fetchall()
    cursor.close()
    conn.close()
    # 按分数高低排序
    x = sorted(values, key=lambda x: x[1])
    y = list(map(lambda x: x[0], x))
    return y


# def get_name_in(low, high):
#     '''返回指定分数之间的名字，按分数从低到高排序'''
#     conn = sqlite3.connect("db_file")
#     cursor = conn.cursor()
#     # select 查找操作
#     cursor.execute("select name,score from user where score>=? and score<=? order by score", (low, high))
#     # featchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录。
#     values = cursor.fetchall()
#     lis = []
#     for i in values:
#         lis.append(i[0])
#     return lis


if __name__ == "__main__":
    name = get_name_in(50, 100)
    print(name)
