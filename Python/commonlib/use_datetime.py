#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta, timezone

# 获取当前时间:
now = datetime.now()
print('now =', now)
print('type(now) =', type(now))

# 用指定日期时间创建datetime:
dt = datetime(2015, 4, 19, 12, 20)
print('dt =', dt)

# 把datetime转换为timestamp:
# 注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。
print('datetime -> timestamp:', dt.timestamp())

# 把timestamp转换为datetime:
t = dt.timestamp()
# timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的
# fromtimestamp 方法按照当前操作系统设定的时区
print('timestamp -> datetime:', datetime.fromtimestamp(t))
# 可以直接被转换到UTC标准时区的时间
print('timestamp -> datetime as UTC+0:', datetime.utcfromtimestamp(t))

# str转换为datetime:
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print('strptime:', cday)

# 把datetime格式化输出:
print('strftime:', cday.strftime('%a, %b %d %H:%M'))

# 对日期进行加减:
print('current datetime =', cday)
print('current + 10 hours =', cday + timedelta(hours=10))
print('current - 1 day =', cday - timedelta(days=1))
print('current + 2.5 days =', cday + timedelta(days=2, hours=12))

# 把时间从UTC+0时区转换为UTC+8:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
utc8_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('UTC+0:00 now =', utc_dt)
print('UTC+8:00 now =', utc8_dt)