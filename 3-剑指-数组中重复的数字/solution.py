# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/26 8:48 上午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


def findRepeatNumber(nums: list) -> int:
    index_num = dict()
    for item in nums:
        index_num[item] = index_num.get(item, 0) + 1
    for k, v in index_num.items():
        if v > 1:
            return k
    return None


def findRepeatNumber1(nums: list) -> int:
    """
    i位置应该存放nums[i]
    :param nums:
    :return:
    """
    for i in range(len(nums)):
        while nums[i] != i:
            if nums[i] == nums[nums[i]]:
                return nums[i]
            temp = nums[i]
            nums[i] = nums[nums[i]]
            nums[temp] = temp
    return None


def findRepeatNumber2(nums: list) -> int:
    if not nums:
        return None
    num = 0
    while num < len(nums):
        if nums[num] == num:
            num += 1
        else:
            tmp = nums[num]
            if nums[tmp] == tmp:
                return tmp
            else:
                nums[num] = nums[tmp]
                nums[tmp] = tmp

    return None


print(findRepeatNumber2([2, 3, 1, 0, 2, 5, 3]))
