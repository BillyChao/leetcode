# -*- coding: utf-8 -*-

"""
@Time    : 2020/7/17 上午11:16
@Author  : mc
@File    : 46-全排列.py
@Software: PyCharm
"""

import operator
from functools import reduce


class Solution:
    def permute(self, nums):
        if not nums:
            return []
        elif len(nums) == 1:
            return [[nums[0]]]
        else:
            return reduce(operator.add,
                          list(map(lambda x: self.add(x, nums[0]), self.permute(nums[1:]))))

    def add(self, x, num):
        res = []
        for i in range(len(x) + 1):
            x.insert(i, num)
            res.append([item for item in x])
            x.pop(i)
        return res


if __name__ == '__main__':
    nums = [1]
    solution = Solution()
    result = solution.permute(nums)
    print(result)
    print(len(result))
