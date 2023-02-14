# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/20 11:37 上午
@Author  : mc
@File    : solution1.py
@Software: PyCharm
"""


def func(nums: list):
    """
    排序数组，平方后，数组当中有多少不同的数字
    :param nums:
    :return:
    """
    i, j = 0, len(nums) - 1
    res = 0
    pre = max(abs(nums[i]), abs(nums[j])) + 1
    while i <= j:
        if abs(nums[i]) > abs(nums[j]):
            if pre != abs(nums[i]):
                res += 1
                pre = abs(nums[i])
            i += 1
        else:
            if pre != abs(nums[j]):
                res += 1
                pre = abs(nums[j])
            j -= 1
    return res


if __name__ == '__main__':
    nums = [0, 0, 1, 1]
    print(func(nums))
