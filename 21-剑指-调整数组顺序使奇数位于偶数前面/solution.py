# -*- coding: utf-8 -*-

"""
@Time    : 2021/3/20 11:49 下午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


class Solution:
    def exchange(self, nums: list) -> list:
        """
        快排思路
        :param nums:
        :return:
        """
        if len(nums) == 0:
            return nums
        begin, end = 0, len(nums) - 1
        base = nums[end]
        while begin < end:
            while begin < end and nums[begin] % 2 == 1:
                begin += 1
            nums[end] = nums[begin]
            while begin < end and nums[end] % 2 == 0:
                end -= 1
            nums[begin] = nums[end]
        nums[begin] = base
        return nums


print(Solution().exchange([1, 2, 3, 4]))
