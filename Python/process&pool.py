#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ldp'

import os
import random
import time
from multiprocessing import Process, Pool, Queue


# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

def process_test():
    # 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    # 用start()方法启动
    p.start()
    # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    p.join()
    print('Child process end.')

def pool_test():
    # 同时只能跑4个进程，这个与cpu核数有关
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    # 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
    p.close()
    p.join()
    print('All subprocesses done.')

# 下面代码相当于在令行执行命令nslookup，然后手动输入：
# set q=mx
# python.org
# exit
def subprocess_test():
    import subprocess

    print('$ nslookup')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # 通过communicate方法进行输入，并接收输出
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    print(output.decode('utf-8'))
    print('Exit code:', p.returncode)

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

# 进程间通信
def commoncation_test():
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    process_test()
    print('============')
    pool_test()
    print('============')
    subprocess_test()
    print('============')
    commoncation_test()
