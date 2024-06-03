# -*- coding:utf-8 -*-
# @FileName  :singleton单例.py
# @Time      :2024/5/30 8:10 PM
# @Author    :mengchao01


from functools import wraps


def singleton(cls):
    """单例类装饰器"""
    instances = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print(self.name)


class SingletonMeta(type):
    """自定义单例元类"""

    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class President(metaclass=SingletonMeta):
    """
    通过自定义元类实现单例
    """

    def __init__(self, name):
        self.name = name


person = Person('lili', 20)
# 重新定义一个person对象，结果会返回之前已经创建的单例对象
person1 = Person('lilei', 30)
print(id(person), id(person1))
print(person.name, person1.name)

#
president = President('mao')
president1 = President('jiang')
print(id(president), id(president1))
print(president.name, president1.name)
