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
        nums[end] = nums[begin]
        while nums[end] > base_num and begin < end:
            end -= 1
        nums[begin] = nums[end]
    nums[begin] = base_num
    helper(nums, low, begin - 1)
    helper(nums, end + 1, high)



def quick_sort(array, left, right):
    if left >= right:
        return
    low = left
    high = right
    key = array[low]
    while left < right:
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left]
    array[right] = key
    quick_sort(array, low, left - 1)
    quick_sort(array, left + 1, high)


nums = [1,1,3,5]
quick_sort(nums, 0, len(nums) - 1)
print(nums)
