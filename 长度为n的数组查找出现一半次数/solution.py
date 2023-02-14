# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/26 12:05 下午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


def findHalfNum(nums: list):
    if not nums:
        return None
    count, cadidate = 1, nums[0]
    for i in range(1, len(nums)):
        if nums[i] != cadidate:
            count -= 1
            if count < 0:
                cadidate = nums[i]
                count = 1
        else:
            count += 1
    return cadidate


print(findHalfNum([1, 1, 3, 4, 5, 1, 1]))
