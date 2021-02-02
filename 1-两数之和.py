# -*- coding: utf-8 -*-

"""
@Time    : 2020/7/11 下午11:01
@Author  : mc
@File    : 1-两数之和.py
@Software: PyCharm
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result = []
        _dic = dict()
        # 题目假设只存在一个答案，这里不需要使用列表存放元素索引index
        for index, item in enumerate(nums):
            _dic[item] = index
        for i in range(len(nums)):
            diff = target - nums[i]
            # 3+3 =6 如果只有一个3的情况下，则不成立
            if diff in _dic.keys() and i != _dic[diff]:
                result = [i, _dic[diff]]
                break
        return result

    def twoSum_20210201(self, nums: list[int], target: int) -> list[int]:
        result = []
