# -*- coding: utf-8 -*-

"""
@Time    : 2021/3/21 11:20 下午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


class Solution:
    def numWays(self, n: int) -> int:
        if n <= 1:
            return 1
        a, b = 1, 1
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return c % 1000000007


print(Solution().numWays(42))
