# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/2 3:29 下午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


class Solution:
    def searchRange(self, nums: list, target: int):
        result = [-1, -1]
        if len(nums) == 0:
            return result
        index_total = 0
        for index, item in enumerate(nums):
            if target == item:
                if index_total == 0:
                    result[0] = result[1] = index
                    index_total += 1
                else:
                    result[1] = index
        return result


if __name__ == '__main__':
    nums = []
    target = 6
    solution = Solution()
    print(solution.searchRange(nums, target))
