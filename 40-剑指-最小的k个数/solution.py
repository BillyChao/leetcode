# -*- coding: utf-8 -*-

"""
@Time    : 2021/3/18 8:08 下午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""

import heapq


class Solution:
    def getLeastNumbers(self, arr: list, k: int):
        if k == 0:
            return None
        heapq.heapify(arr)
        return [heapq.heappop(arr) for _ in range(k)]


print(Solution().getLeastNumbers([3, 2, 1, 4, 5, 6, 1, ], 3))
