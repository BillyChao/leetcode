# -*- coding: utf-8 -*-

"""
@Time    : 2020/7/19 上午12:02
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


def quick_sort(nums, left, right):
    if left < right:
        par = helper(nums, left, right)
        quick_sort(nums, left, par - 1)
        quick_sort(nums, par + 1, right)


def helper(nums, begin, end):
    if begin >= end:
        return
    low = begin
    high = end
    base_num = nums[end]
    while begin < end:
        while nums[begin] < base_num and begin < end:
            begin += 1
        if begin < end:
            nums[end] = nums[begin]
            end -= 1
        while nums[end] > base_num and begin < end:
            end -= 1
        if begin < end:
            nums[begin] = nums[end]
            begin += 1
    nums[begin] = base_num
    helper(nums, low, begin - 1)
    helper(nums, end + 1, high)


if __name__ == '__main__':
    nums = [2, 4, 7, 10, 3, 12, 56, 23, 45]
    helper(nums, 0, len(nums) - 1)
    print(nums)
