# -*- coding: utf-8 -*-

"""
@Time    : 2021/7/26 下午7:22
@Author  : mc
@File    : solution.py
@Software: PyCharm
在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。
示例 1：

输入：nums = [3,4,3,3]
输出：4
示例 2：

输入：nums = [9,1,7,9,7,9,7]
输出：1
限制：

1 <= nums.length <= 10000
1 <= nums[i] < 2^31
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof
"""


def singleNumber(nums: list):
    counts = [0] * 32
    for num in nums:
        for j in range(32):
            counts[j] += num & 1
            num >>= 1
    res, m = 0, 3
    for i in range(32):
        res <<= 1
        res |= counts[31 - i] % m
    return res if counts[31] % m == 0 else ~(res ^ 0xffffffff)
