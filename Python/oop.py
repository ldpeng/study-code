#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ldp'

# 通过class关键字定义一个类，类名后添加一对括号，里面写入所继承的父类，如果没有父类，就写成object，这时所有类的父类（注意不写object会代表其他意思）
# Python中支持多继承，在类定义中通过逗号隔开
class Student(object):

    # 用tuple定义允许绑定的属性名称（对子类无效）。试图添加其他属性会报AttributeError
    # __slots__ = ('name', 'age')

    # 在类上定义的属性属于类属性
    name = 'Student'

    # __init__ 方法相当于构造函数，第一个参数固定为self，表示当前实例
    def __init__(self, name, score):
        # 通过两个下划线（__）命名的成员变量，是私有变量，外部不能通过实例对象直接访问。注意不用用两个下划线结尾，可能会与特殊变量冲突。
        # 其实私有变量还是可以被外部直接访问的，但是需要换一种方式。如：通过_Student__name（根据编译器不同或）来访问__name。
        # 这是Python编译器做的小聪明，来限制不直接访问私有变量。
        self.__name = name
        self.__score = score

    # 要定义一个方法，除了第一个参数是self外，其他和普通函数一样。
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    # 重写__str__方法，指定打印对象时输出的内容
    def __str__(self):
        return 'Student object (name: %s)' % self.__name

    # 有一个__repr__方法与__str__方法类似
    # 区别是，str 返回用户看到的字符串，而 repr 返回程序开发者看到的字符串 repr 是为调试服务的。
    __repr__ = __str__

    # 当访问在类中没有定义的属性时，Python会调用__getattr__方法。
    # 注意：要让class只响应特定的几个属性，要按照约定，抛出AttributeError的错误
    def __getattr__(self, attr):
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

    # 重写__call__方法可以把对象实例当作函数使用，这里还可以传参
    # 通过callable()函数可以判断变量是否可被调用
    def __call__(self):
        print('My name is %s.' % self.name)


# 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去
bart = Student('Bart Simpson', 59)
bart.print_score()
print(bart.get_grade())

# 不建议这样访问私有变量
print(bart._Student__name)

print(bart)

# 判断是否可被调用
print(callable(bart))
print(callable([1, 2, 3]))


print('=====类属性与实例属性=======')
s = Student('aaa', 11) # 创建实例s
print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(Student.name) # 打印类的name属性
s.name = 'Michael' # 给实例绑定name属性
print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
del s.name # 如果删除实例的name属性
print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
print('=====类属性与实例属性=======')


# 可以通过 type() 函数检查对象类型
print(type(123))
print(type('123'))
print(type(bart))

print(type(123)==int)
print(type('abc')==str)

# 判断基本数据类型可以直接写int，str等，但如果要判断复杂类型，可以使用types模块中定义的常量：
import types

def fn():
    pass

print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x: x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)

print('============instance===========')

# 如果要判断继承关系，使用type就不方便了，通常使用isinstance()函数
# 同时instance函数也可以判断类型，并且还可以判断一个变量是否是某些类型中的一种
print(isinstance('a', str))
print(isinstance(123, int))
print(isinstance(b'a', bytes))
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

# dir()函数可以获得一个对象的所有属性和方法
print(dir(bart))

# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数，实际上，在len()函数内部，它自动去调用该对象的__len__()方法，下面的代码是等价的：
print(len('ABC'))
print('ABC'.__len__())

# hasattr()判断对象是否有某个属性。注意判断不了私有属性
print(hasattr(bart, '__name'))
bart.x = 'x'
print(hasattr(bart, 'x'))

# getattr()获取对象属性。如果试图获取不存在的属性，会抛出AttributeError的错误
print(getattr(bart, 'x'))
# 如果获取的属性不存在，可以通过第三个参数设置返回的默认值
print(getattr(bart, 'y', 'yy'))
# 也可以获得对象方法
print(getattr(bart, 'get_grade'))


# @property 可以将get方法作为一个属性对外暴露，同样的 @属性名.setter 可以将set方法调用改为直接用等于号赋值
class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height


s = Screen()
s.width = 100
s.height = 200
print(s.resolution)


# 如果一个类想被用于for ... in循环，必须实现一个__iter__()方法，该方法返回一个迭代对象，
# 然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
# 要想实现同下标调用，则需要实现 __getitem__() 方法
# 此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。
# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。

# 以斐波那契数列为例
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片，可能传入的是切片语法
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f = Fib()

for n in f:
    print(n)

print(f[1])
print(f[5])
print(f[0:5])

