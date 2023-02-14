# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/21 11:17 上午
@Author  : mc
@File    : solution-已排序数组.py
@Software: PyCharm
"""


def twoSum(nums: list, target):
    left, right = 1, len(nums)
    while left < right:
        sum = nums[left - 1] + nums[right - 1]
        if sum == target:
            return [left, right]
        elif sum < target:
            left += 1
        else:
            right -= 1
    return []


print(twoSum([2, 7, 11, 15], 9))
