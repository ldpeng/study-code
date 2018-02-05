#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python已经内置了urllib模块，用于访问网络资源。但是，它用起来比较麻烦，而且，缺少很多实用的高级功能。
# 更好的方案是使用requests。它是一个Python第三方库，处理URL资源特别方便。

import requests

# GET访问一个页面

r = requests.get('https://www.douban.com/') # 豆瓣首页
print(r.status_code)
# 返回内容
# print(r.text)

# 对于带参数的URL，传入一个dict作为params参数：
r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r.url) # 实际请求的URL
# requests自动检测编码，可以使用encoding属性查看：
print(r.encoding)

# 无论响应是文本还是二进制内容，我们都可以用content属性获得bytes对象：
print(r.content)

# 对于特定类型的响应，例如JSON，可以直接获取：
r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
print(r.json())

# 需要传入HTTP Header时，传入一个dict作为headers参数：
r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
#print(r.text)


# POST请求，只需要把get()方法变成post()，然后传入data参数作为POST请求的数据：
r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})

# requests默认使用application/x-www-form-urlencoded对POST数据编码。
# 如果要传递JSON数据，可以直接传入json参数，内部会自动序列化为JSON：
# r = requests.post(url, json={'key': 'value'})

# 类似的，上传文件需要更复杂的编码格式，但是requests把它简化成files参数：
# 在读取文件时，注意务必使用'rb'即二进制模式读取，这样获取的bytes长度才是文件的长度。
# upload_files = {'file': open('report.xls', 'rb')}
# r = requests.post(url, files=upload_files)

# requests同样支持PUT或DELETE方式请求资源，使用对应的方法名即可


# 获取响应头：
print(r.headers)
print(r.headers['Content-Type'])

# requests对Cookie做了特殊处理，使得我们不必解析Cookie就可以轻松获取指定的Cookie：
# print(r.cookies['ts'])

# 要在请求中传入Cookie，只需准备一个dict传入cookies参数：
# r = requests.get(url, cookies={'token': '12345', 'status': 'working'})

# 要指定超时，传入以秒为单位的timeout参数：
# r = requests.get(url, timeout=2.5) # 2.5秒后超时


