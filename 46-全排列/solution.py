# -*- coding: utf-8 -*-

"""
@Time    : 2021/3/3 10:38 上午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


class Solution:
    def permute(self, nums: list) -> list:
        res = []

        def dfs(x):
            if x == len(nums) - 1:
                res.append(nums[:])
            for i in range(x, len(nums)):
                nums[i], nums[x] = nums[x], nums[i]
                dfs(x + 1)
                nums[i], nums[x] = nums[x], nums[i]

        dfs(0)
        return res


print(Solution().permute([1, 2]))
