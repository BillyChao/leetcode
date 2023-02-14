# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/24 9:37 上午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


def sqrt(num: float):
    value = num if num > 1 else 1
    left, right = 0, value
    mid = (left + right) / 2
    precision = 0.00001
    while mid ** 2 > num + precision or mid ** 2 < num - precision:
        if mid ** 2 > num + precision:
            right = mid
        elif mid ** 2 < num + precision:
            left = mid
        else:
            return mid
        mid = (left + right) / 2
    return mid


print(sqrt(4.2))
