# -*- coding: utf-8 -*-

"""
@Time    : 2023/3/2 下午11:17
@Author  : mc
@File    : solution2023.py
@Software: PyCharm
"""
from random import randint


class Solution:
    def sortArray(self, nums: list):
        left, right = 0, len(nums) - 1
        self.quickSort(nums, left, right)

    def quickSort(self, nums: list, left, right):
        if left < right:
            value = nums[left]
            l, r = left, right
            while l <= r:
                while l <= r and nums[l] <= value:
                    l += 1
                while l <= r and nums[r] >= value:
                    r -= 1
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp

            nums[r] = value
            self.quickSort(nums, left, r - 1)
            self.quickSort(nums, r + 1, right)


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 5, 3, 4, 8, 2, 19, 20, 3,3,3]
    solution.sortArray(nums)
    print(nums)
