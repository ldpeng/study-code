#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# psutil = process and system utilities，它不仅可以通过一两行代码实现系统监控，还可以跨平台使用，支持Linux／UNIX／OSX／Windows等

import psutil

# 获取CPU的信息：
# CPU逻辑数量
print(psutil.cpu_count())
# CPU物理核心
print(psutil.cpu_count(logical=False))

# 统计CPU的用户／系统／空闲时间：
print(psutil.cpu_times())

# 实现类似top命令的CPU使用率，每秒刷新一次，累计10次：
for x in range(10):
    print(psutil.cpu_percent(interval=1, percpu=True))


# 获取物理内存信息(返回的是字节为单位的整数)
print(psutil.virtual_memory())
# 获取交换内存信息
print(psutil.swap_memory())


# 磁盘分区信息
print(psutil.disk_partitions())
# 磁盘使用情况
print(psutil.disk_usage('/'))
# 磁盘IO
print(psutil.disk_io_counters())


# 获取网络读写字节／包的个数
print(psutil.net_io_counters())
# 获取网络接口信息
print(psutil.net_if_addrs())
# 获取网络接口状态
print(psutil.net_if_stats())

# 获取当前网络连接信息
# 可能会报错，原因是psutil获取信息也是要走系统接口，而获取网络连接信息需要root权限，需要通过root权限运行Python
# print(psutil.net_connections())


# 获取进行信息
# 所有进程ID
print(psutil.pids())

# p = psutil.Process(3776) # 获取指定进程ID=3776，其实就是当前Python交互环境。获取一个root用户的进程需要root权限
# p.name() # 进程名称
# p.exe() # 进程执行文件的路径
# p.cwd() # 进程工作目录
# p.cmdline() # 进程启动的命令行
# p.ppid() # 父进程ID
# p.parent() # 父进程
# p.children() # 子进程列表
# p.status() # 进程状态
# p.username() # 进程用户名
# p.create_time() # 进程创建时间
# p.terminal() # 进程终端
# p.cpu_times() # 进程使用的CPU时间
# p.memory_info() # 进程使用的内存
# p.open_files() # 进程打开的文件
# p.connections() # 进程相关网络连接
# p.num_threads() # 进程的线程数量
# p.threads() # 所有线程信息
# p.environ() # 进程环境变量
# p.terminate() # 结束进程

# psutil还提供了一个test()函数，可以模拟出ps命令的效果
psutil.test()
