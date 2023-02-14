# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/22 5:36 下午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


def findKth(a, n, K):
    return find(a, 0, n - 1, K)


def find(a: list, start, end, K):
    if start == end:
        return a[start]
    n = len(a)
    target = n - K
    index = partition(a, start, end)
    if target == index:
        return a[index]
    if target < index:
        return find(a, start, index - 1, K)
    else:
        return find(a, index + 1, end, K)


def partition(a, start, end):
    base = a[end]
    while start < end:
        while start < end and a[start] < base:
            start += 1
        a[end] = a[start]
        while start < end and a[end] >= base:
            end -= 1
        a[start] = a[end]
    a[start] = base
    return start


print(findKth([1, 3, 5, 6, 7], 5, 3))
