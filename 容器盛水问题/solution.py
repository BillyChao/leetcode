# -*- coding: utf-8 -*-

"""
@Time    : 2021/3/2 11:43 下午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


#
# max water
# @param arr int整型一维数组 the array
# @return long长整型
#
class Solution:
    def maxWater(self, arr):
        res = 0
        left, right = 0, len(arr) - 1
        while left < right:
            left_hei = arr[left]
            right_hei = arr[right]
            if left_hei < right_hei:
                while left < right and arr[left] <= left_hei:
                    res += left_hei - arr[left]
                    left += 1
            else:
                while left < right and arr[right] <= right_hei:
                    res += right_hei - arr[right]
                    right -= 1
        return res


print(Solution().maxWater([4,5,1,3,2]))
