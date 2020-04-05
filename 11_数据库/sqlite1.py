# -*- coding: utf-8 -*-
import sqlite3
import os


db_file1 = os.path.join(os.path.dirname(__file__), "test.tb")
if os.path.isfile(db_file1):
    os.remove(db_file)
conn = sqlite3.connect("db_file1")
cursor = conn.cursor()
cursor.execute("drop table user1")  # 删除一个表格（table）
cursor.execute("create table if not exists user1 (id varchar(20) primary key,name varchar(20),score int)")
cursor.execute("insert into user1 values('1', 'Mike','99')")
cursor.execute("insert into user1 values('2','Job','90')")
cursor.execute("insert into user1 values('3','Lisa','100')")
conn.commit()  # 提交事务

# update 操作 将Mike的分数更新为95
cursor.execute("select * from user1")
print(cursor.fetchall())
cursor.execute("update user1 set score = 95 where id = 1")
cursor.execute("select * from user1")
print(cursor.fetchall())

# delete操作  
cursor.execute("delete from user1 where id = 1")
cursor.execute("select * from user1")
print(cursor.fetchall())
