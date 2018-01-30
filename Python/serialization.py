#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ldp'

# Python提供了pickle模块来实现序列化和反序列化。
# 注意：序列化处理的东西只能被Python解析，并且可能不同版本的Python彼此都不兼容
import pickle

d = dict(name='Bob', age=20, score=88)
# 把任意对象序列化成一个bytes
print(pickle.dumps(d))

from io import BytesIO

f = BytesIO()
# 直接把对象序列化后写入一个file-like Object
pickle.dump(d, f)
print(f.getvalue())

# 反序列化可以先将内容读成一个 bytes，然后通过 pickle.loads()方法反序列化出对象；或者直接用pickle.load()方法从一个file-like Object中直接反序列化出对象
d1 = pickle.loads(f.getvalue())
print(d1)

print('==========json===========')

# json模块提供了非常完善的Python对象到JSON格式的转换
# JSON标准规定JSON编码是UTF-8，不需要转码
import json

# dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。
print(json.dumps(d))

from io import StringIO

s = StringIO()
json.dump(d, s)
print(s.getvalue())

# JSON反序列化为Python对象，用loads()JSON的字符串反序列化；对应的load()方法，从file-like Object中读取字符串并反序列化
print(json.loads(s.getvalue()))

print('=====对象与json互转====')


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


# 定义一个函数，将student对象转化成dict
# def student2dict(std):
#     return {
#         'name': std.name,
#         'age': std.age,
#         'score': std.score
#     }

s = Student('Bob', 20, 88)
# print(json.dumps(s, default=student2dict)) 这样做不通用

# 因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。
print(json.dumps(s, default=lambda obj: obj.__dict__))

# 要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例：
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))

# 通过ascii序列化
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)