# -*- coding:utf-8 -*-
# @FileName  :找重复元素.py
# @Time      :2024/6/3 8:01 PM
# @Author    :mengchao01

# 列表中有1000000个元素，取值范围是[1000, 10000)，设计一个函数找出列表中的重复元素。

def find_dup(items: list):
    dups = [0] * 9000
    for item in items:
        dups[item - 1000] += 1
    for i, v in enumerate(dups):
        if v > 1:
            yield i + 1000


if __name__ == '__main__':
    for i in find_dup([1000, 2000, 1000, 2000, 4000, 1003, 1003]):
        print(i)
