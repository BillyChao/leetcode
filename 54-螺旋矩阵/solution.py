# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/22 7:58 下午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


def spiralOrder(matrix: list) -> list:
    if not matrix or not matrix[0]:
        return []
    m = len(matrix)
    n = len(matrix[0])
    left, top, right, bottom = 0, 0, n - 1, m - 1
    res = []
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            res.append(matrix[top][i])
        for i in range(top + 1, bottom + 1):
            res.append(matrix[i][right])
        if left < right and top < bottom:
            for i in range(right - 1, left, -1):
                res.append(matrix[bottom][i])
            for i in range(bottom, top, -1):
                res.append(matrix[i][left])
        left, top, right, bottom = left + 1, top + 1, right - 1, bottom - 1
    return res


print(spiralOrder([[3], [2]]))
