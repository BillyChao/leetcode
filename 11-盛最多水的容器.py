# -*- coding: utf-8 -*-

"""
@Time    : 2020/7/14 下午11:23
@Author  : mc
@File    : 11-盛最多水的容器.py
@Software: PyCharm
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        # 双指针移动，当头比尾小，头向前移动，此时才有机会使得面积更大， 当头比尾大，尾向后移动，此时才有机会使得面积更大
        area = 0
        begin = 0
        end = len(height) - 1
        while begin < end:
            if height[begin] < height[end]:
                area = max(area, height[begin] * (end - begin))
                begin += 1
            else:
                area = max(area, height[end] * (end - begin))
                end -= 1
        return area
