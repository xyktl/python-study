# -*- coding: utf-8 -*-
# mysql 语句要大写
# 参照  https://blog.csdn.net/n950814abc/article/details/82284838
import mysql.connector
# 使用buffered游标执行查询语句时 ,取行方法（如fetchone()，fechcall()等返回的是
# 缓冲区中的行。nonbuffered游标不从服务器获取数据,直到调用了某个获取数据行的方法,
# 在使用nonbuffered游标时,必须确保取出的结果是结果集中的所有行，才能再用同一连接
# 执行其他语句,否则会报错

conn = mysql.connector.connect(host="localhost", user="root", passwd="c1635976271", database="runoob_db", buffered=True)
cursor = conn.cursor()
cursor.execute("SHOW DATABASES")
print(cursor.fetchall())

cursor.execute("CREATE DATABASE if not exists runoob_db")

# 插入，两种写法
cursor.execute("CREATE table if not exists sites (id int auto_increment primary key,name varchar(255),url varchar(255))")
#cursor.execute("insert into sites (name,url) values(%s,%s)", ("RUNOOB", "https: // www.runoob.com"))
sql = "replace  into sites (name,url) values(%s,%s)"
val = ("runoob", "https://www.runoob.com")
cursor.execute(sql, val)

# 批量插入

val1 = [("Google", "https://www.google.com"),
        ("Github", "https://www.github.com"),
        ("Taobao", "https://www.taobao.com"),
        ("stackoverflow", "https://www.stackoverflow.com/")]
cursor.executemany(sql, val1)

# 将表中重复的数据去掉
# 1.先创建临时表newsites ,新表newsites 中的数据时从sites 表中分组查询出来的
cursor.execute("CREATE table if not exists newsites select name, url from sites group by name,url ")
# 2.创建一个与表sites 相同结构的tab 表
cursor.execute("CREATE table if not exists tab like sites")
#cursor.execute("CREATE table if not exists tab (id int auto_increment primary key,name varchar(255),url varchar(255))")
# 3.会发现 newsites表中没有id，我们需要加上id，所以就将newsites 表中的数据插入tab 表中
cursor.execute("INSERT into tab select null,name,url from newsites")
conn.commit()


cursor.execute("select * from sites")
print(cursor.fetchall())
print("---------------")
cursor.execute("select * from newsites")
print(cursor.fetchall())
print("---------------")
cursor.execute("select * from tab")
print(cursor.fetchall())
print("-----------")
# 将三个表都删除
cursor.execute("drop table sites")
cursor.execute("drop table newsites")
#cursor.execute("drop table tab")


# 查找表中重复的name 和次数
cursor.execute("SELECT name,count(1) from tab group by name having count(1) > 1")
print(cursor.fetchall())
print("----------")
# 查找表中所有重复的name
cursor.execute("SELECT  name from tab where name in  (select name from tab group by name having count(1) > 1)")
print(cursor.fetchall())
print("----------")


# 查找表中重复的url ,只留下id 最小的一条
cursor.execute(
    "SELECT url from tab where id  in (select dt.minid from (select min(id) as minid from tab group by name having count(1) > 1)dt)")
print(cursor.fetchall())
print("---------")
# 更新（delete update）表的同时又查询了这个表，查询这个表的同时又去更新了这个表，会报错可以理解为死锁。mysql不支持这种更新查询同一张表的操作
# cursor.execute("DELETE  from tab where name in  (select name from tab group by name having count(1) > 1)")

# 解决办法：把要更新的几列数据查询出来做为一个第三方表t ，然后筛选更新。
# 删除表中重复的数据 只留下id 最小的一条
cursor.execute(
    "DELETE  from tab where id not in (select dt.minid from (select min(id) as minid from tab group by name having count(1) > 1)dt)")
cursor.execute("SELECT * from tab")
print(cursor.fetchall())
print("---------")

# 删除表中所有重复的数据，如果都有重复，表只剩下空表
cursor.execute("DELETE  from tab where name in (select t.name from (select name from tab group by name having count(1) > 1)t)")
cursor.execute("SELECT * from tab")
print(cursor.fetchall())
print("---------")


# 提交事务，执行数据库操作
conn.commit()
cursor.close()
conn.close()
