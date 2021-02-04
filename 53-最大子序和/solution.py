# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/3 7:43 下午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


class Solution:
    def maxSubArray(self, nums: list):
        max_sub_sum = max(nums)
        for i in range(len(nums)):
            tmp = nums[i]
            for j in range(i + 1, len(nums)):
                if (tmp + nums[j]) > 0:
                    tmp += nums[j]
                    if max_sub_sum < tmp:
                        max_sub_sum = tmp
                else:
                    break
        return max_sub_sum


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    solution = Solution()
    print(solution.maxSubArray(nums))
