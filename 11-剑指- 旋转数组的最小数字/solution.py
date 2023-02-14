# -*- coding: utf-8 -*-

"""
@Time    : 2021/3/3 10:44 下午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


class Solution:
    def minArray(self, numbers: list) -> int:
        """
        二分查找思路，最小值左边的数据一定比numbers[-1]大，右边的数据比numbers[-1]小
        :param numbers:
        :return:
        """
        left, right = 0, len(numbers) - 1
        while left < right:
            mid = (left + right) // 2
            if numbers[mid] < numbers[right]:
                right = mid
            elif numbers[mid] > numbers[right]:
                left = mid + 1
            else:
                right -= 1
        return numbers[left]


print(Solution().minArray([3, 1, 3]))
