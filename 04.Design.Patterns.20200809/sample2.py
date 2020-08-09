"""
封装：
1.

多态：
1.多态有两种类型：
1.1。对象根据输入参数提供方法的不同实现
1.2.不同类型的对象可使用相同的接口
2.对于python来说，多态是该语言的内置功能
继承：
1.表示一个类可以继承父类的功能
2.被描述为一个重用基类中定义的功能，并允许对原始软件的实现进行独立扩展的选项
3.可利用不同类的对象之间的关系建立层次结构
4.支持多重继承，即继承多个基类

抽象：
1.提供一个简单的客户端接口，客户端可通过该接口与类的对象进行交互，并可调用该接口中定义的各个方法
2.将内部的复杂性抽象为一个接口，这样客户端就不需要知道内部的实现细节

组合：
1.一种将对象或类组合成更复杂的数据结构或软件实现方法
2.在组合中，一个对象可用于调用其他模块中的成员函数，这样一来，就无需通过继承就可实现基本功能的跨模块的使用
"""

"""sample.1.多态"""
a = "Jhon"
b = (1, 2, 3)
c = [3, 4, 5, 6, 7]
print(a[1], b[0], c[2])

"""sample.2.继承"""
class A:
    def a1(self):
        print("a1")


class B(A):
    def b(self):
        print("b")


b = B()
b.a1()
b.b()

"""sample.3.抽象"""


class Adder:
    def __init__(self):
        self.sum = 0

    def add(self, value):
        self.sum += value


acc = Adder()
for i in range(3):
    acc.add(i)

print(acc.sum)

"""sample.4.组合"""


class A(object):
    def a1(self):
        print("a1")


class B(object):
    def b(self):
        print("b")
        A().a1()


objectB = B()
objectB.b()
