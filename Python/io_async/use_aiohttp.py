#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# aiohttp是基于asyncio实现的HTTP框架。需要先安装：pip install aiohttp

import asyncio

from aiohttp import web


async def index(request):
    print('index')
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>', headers=[('Content-Type', 'text/html')])

async def hello(request):
    print('hello')
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'), headers=[('Content-Type', 'text/html')])

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()