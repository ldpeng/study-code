#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# sqlalchemy是一个ORM框架

# 导入:
from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

    # 一对多:
    books = relationship('Book')

class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(String(20), ForeignKey('user.id'))

# 初始化数据库连接:
# 格式：数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名
engine = create_engine('mysql+mysqlconnector://root:Ldp*8888@localhost:3306/mysqltest')

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = User(id='5', name='Bob')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()


# 有了ORM，查询出来的可以不再是tuple，而是User对象
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.name)
# 关闭Session:
session.close()


# 创建book表，并添加几本书
session = DBSession()
session.execute('create table book (id varchar(20) primary key, name varchar(20), user_id varchar(20))')
new_book = Book(id='1', name='Java', user_id='1')
new_book1 = Book(id='2', name='Python', user_id='1')
new_book2 = Book(id='3', name='JavaScript', user_id='5')
session.add(new_book)
session.add(new_book1)
session.add(new_book2)
session.commit()
session.close()


# 查询user，自动带出所关联的books
session = DBSession()
users = session.query(User).all()
# 打印类型和对象的name属性:
for u in users:
    print(u.id, u.name, 'has book:')
    for book in u.books:
        print('\t', book.id, book.name)
# 关闭Session:
session.close()