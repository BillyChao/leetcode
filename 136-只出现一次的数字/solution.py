# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/5 2:59 下午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""
from functools import reduce


class Solution:
    def singleNumber(self, nums: list) -> int:
        if len(nums) == 1:
            return nums[0]
        nums = sorted(nums)
        i = 0
        while i < len(nums) - 1:
            if nums[i] != nums[i + 1]:
                return nums[i]
            i += 2
        return nums[i]

    def singleNumber1(self, nums: list) -> int:
        return reduce(lambda x, y: x ^ y, nums)


if __name__ == '__main__':
    nums = [1, 0, 0]
    solution = Solution()
    print(solution.singleNumber1(nums))
