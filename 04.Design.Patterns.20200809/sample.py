__author__ = 'Chetan'

"""
对象：
1.表示所开发的应用程序内的实体
2.实体之间可通过交互来解决现实世界的问题
eg. Person是实体，而Car也是实体，Persion可以驾驶Car，从一个地方开到另一个地方

类：
1.类可定义对象的属性和行为，属性是数据成员，行为由成员函数表示
2.类包含了构造函数，这些函数的作用是为对象提供初始状态
3.类就像模板一样，非常易于重复使用
eg.类Person可带有属性name和age，同时提供成员函数gotOffice()，以定义去办公室工作的行为

方法：
1.表示对象的行为
2.方法可对属性进行处理，从而实现所需的功能
"""


class Person(object):

    def __init__(self, name, age):  # constructor
        self.name = name  # data members/ attributes
        self.age = age

    def get_person(self, ):  # member function
        return "<Person (%s, %s)>" % (self.name, self.age)


p = Person("John", 32)  # p is an object of type Person
print("Type of Object:", type(p), "Memory Address:", id(p))

q = p.get_person()
print(q)
