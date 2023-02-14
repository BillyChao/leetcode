# -*- coding: utf-8 -*-

"""
@Time    : 2021/3/21 8:47 下午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


class Solution:
    def translateNum(self, num: int) -> int:
        nums = list(str(num))
        nums = list(map(int, nums))
        return self.helper(nums)

    def helper(self, nums: list):
        if len(nums) <= 1:
            return 1
        else:
            if nums[0] != 0 and (10 * nums[0] + nums[1]) < 26:
                return self.helper(nums[1:]) + self.helper(nums[2:])
            else:
                return self.helper(nums[1:])


print(Solution().translateNum(18580))
