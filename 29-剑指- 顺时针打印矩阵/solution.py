# -*- coding: utf-8 -*-

"""
@Time    : 2021/3/21 12:02 上午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


class Solution:
    def spiralOrder(self, matrix: list):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return matrix
        res = []
        left, top, right, down = 0, 0, len(matrix[0]) - 1, len(matrix) - 1
        while left <= right and top <= down:
            for i in range(left, right):
                res.append(matrix[top][i])
            for i in range(top, down + 1):
                res.append(matrix[i][right])
            if left < right and top < down:
                for i in range(right - 1, left, -1):
                    res.append(matrix[down][i])
                for i in range(down, top, -1):
                    res.append(matrix[i][left])
            left += 1
            right -= 1
            top += 1
            down -= 1
        return res


print(Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
