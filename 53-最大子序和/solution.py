# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/3 7:43 下午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


class Solution:
    def maxSubArray(self, nums: list):
        """
        时间复杂度为O(n^2)
        :param nums:
        :return:
        """
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

    def maxSubArray1(self, nums: list):
        """
        动态规划，时间复杂度为O(n)
        :param nums:
        :return:
        """
        if not nums:
            return 0
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        res = nums[0]
        for i in range(len(nums)):
            if nums[i] > res:
                res = nums[i]
        return res


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    solution = Solution()
    print(solution.maxSubArray1(nums))
