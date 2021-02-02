# -*- coding: utf-8 -*-

"""
@Time 2021/02/01
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


class Solution:
    def twoSum(self, nums: list, target):
        """
        注意：数组中同一个元素不能使用两遍
        :param nums:
        :param target:
        :return:
        """

        index_map = {}
        for index, item in enumerate(nums):
            if item in index_map:
                index_map[item].append(index)
            else:
                index_map[item] = [index]
        for index, item in enumerate(nums):
            i = target - item
            if i in index_map:
                for j in index_map[i]:
                    if index != j:
                        return [index, j]
        return []


if __name__ == '__main__':
    solution = Solution()
    nums = [3, 2, 4]
    target = 6
    print(solution.twoSum(nums, target))
