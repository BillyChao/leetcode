# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/24 11:17 下午
@Author  : mc
@File    : soluion.py
@Software: PyCharm
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: list) -> int:
        """
        滑动窗口解法
        :param target:
        :param nums:
        :return:
        """
        if not nums:
            return 0
        i, j = 0, 0
        arr_sum = nums[0]
        min_len, index = 0, 1
        while j < len(nums):
            if arr_sum < target:
                j += 1
                if j < len(nums):
                    arr_sum += nums[j]
                    index += 1
            elif arr_sum >= target:
                if index < min_len or min_len == 0:
                    min_len = index
                index -= 1
                arr_sum -= nums[i]
                i += 1

        return min_len

    def minSubArrayLen1(self, target: int, nums: list) -> int:
        """
        滑动窗口解法
        :param target:
        :param nums:
        :return:
        """
        n = len(nums)
        if n == 0:
            return 0
        start = end = 0
        num_sum = 0
        min_len = n + 1
        while end < n:
            num_sum += nums[end]
            while num_sum >= target:
                min_len = min(min_len, end - start + 1)
                num_sum -= nums[start]
                start += 1
            end += 1
        return 0 if min_len == n + 1 else min_len


print(Solution().minSubArrayLen1(11, [1, 2, 3, 4, 5]))
