# -*- coding: utf-8 -*-

"""
@Time    : 2021/3/2 4:25 下午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007

    def fib1(self, n: int) -> int:
        cur, nxt = 0, 1
        for _ in range(n):
            cur, nxt = nxt, cur + nxt
        return cur % 1000000007


print(Solution().fib1(3))
