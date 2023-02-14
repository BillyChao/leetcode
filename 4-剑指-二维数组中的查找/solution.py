# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/26 10:36 上午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""

import heapq


class Solution:
    def findNumberIn2DArray(self, matrix: list, target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m, n = 0, len(matrix[0]) - 1
        while m < len(matrix) and n >= 0:
            if matrix[m][n] > target:
                n -= 1
            elif matrix[m][n] == target:
                return True
            else:
                m += 1
        return False


def getLeastNumbers(arr: list, k: int) -> list:
    if k == 0:
        return list()

    # hp = [-x for x in arr[:k]]
    heapq.heapify(arr)

    return [heapq.heappop(arr) for _ in range(k)]


matrix = [[5], [6]]
# print(getLeastNumbers([3, 2, 1], 2))
print(Solution().findNumberIn2DArray(matrix, 6))
