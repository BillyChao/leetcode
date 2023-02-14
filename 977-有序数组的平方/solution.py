# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/20 11:22 上午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


class Solution:
    def sortedSquares(self, nums: list) -> list:
        ss = []
        i, j = 0, len(nums) - 1
        while i <= j:
            a = abs(nums[i])
            b = abs(nums[j])
            if a > b:
                ss.insert(0, a)
                i += 1
            else:
                ss.insert(0, b)
                j -= 1

        return [i ** 2 for i in ss]



if __name__ == '__main__':
    nums = [-7,-3,2,3,11]
    solution = Solution()
    print(solution.sortedSquares(nums))
