#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 任何模块代码的第一个字符串都被视为模块的文档注释

'这里是模块的文档注释'

# 指定模块的作者
__author__ = 'LDP'

# 获得当前模块名称
print(__file__)

# sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称，例如：
# 运行python3 module.py获得的sys.argv就是['module.py']；
# 运行python3 module.py Michael获得的sys.argv就是['module.py', 'Michael]。
import sys

# 模块搜索路径
# 当我们试图加载一个模块时，Python会在指定的路径下搜索对应的.py文件，如果找不到，就会报错(ImportError)
# 默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中
print(sys.path)

# 要添加自己的搜索目录，有两种方法：
# 一是直接修改sys.path，添加要搜索的目录：
# sys.path.append('/Users/ldp/my_py_scripts')
# 这种方法是在运行时修改，运行结束后失效。
# 第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

# 在命令行运行module模块文件时，Python解释器把一个特殊变量__name__置为__main__，
# 而如果在其他地方导入该模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
if __name__=='__main__':
    test()

# 在Python中，是通过 _ 前缀来命名私有变量及方法。这只是一种习惯，Python本身并没有机制去吧模块内的东西封闭起来，都是有办法直接调用的，但一般不会这么做。

