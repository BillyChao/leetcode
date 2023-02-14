# -*- coding: utf-8 -*-

"""
@Time    : 2021/7/23 下午2:05
@Author  : mc
@File    : solution.py
@Software: PyCharm
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

示例 1：
输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
示例 2：

输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof
"""
from functools import reduce


def singleNumbers(nums):
    result = reduce(lambda x, y: x ^ y, nums)
    div = 1
    while result & div == 0:
        div <<= 1
    a, b = 0, 0
    for n in nums:
        if div & n:
            a ^= n
        else:
            b ^= n
    return [a, b]


if __name__ == '__main__':
    print(singleNumbers([1, 2, 1, 10, 3, 3, ]))
