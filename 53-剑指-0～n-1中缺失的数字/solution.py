# -*- coding: utf-8 -*-

"""
@Time    : 2021/3/21 8:32 下午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


class Solution:
    def missingNumber(self, nums: list):
        if len(nums) == 0:
            return 0
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)


print(Solution().missingNumber([0, 1, 2, 3, 4, 5, 6, 7, 8]))
