#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 导入MySQL驱动
import mysql.connector

conn = mysql.connector.connect(user='root', password='Ldp*8888', database='mysqltest')

# 创建一个Cursor:
cursor = conn.cursor()

# 创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'LDP'])

# 使用Cursor对象执行insert，update，delete语句时，执行结果由rowcount返回影响的行数，就可以拿到执行结果。
print(cursor.rowcount)

# 提交事务:
conn.commit()
cursor.close()

# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
# 使用Cursor对象执行select语句时，通过featchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录。
values = cursor.fetchall()
print(values)

# 关闭Cursor和Connection，应该放在finally块中
cursor.close()
conn.close()