# -*- coding: utf-8 -*-

"""
@Time    : 2021/3/4 9:43 上午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


class Solution:
    def sumNums(self, n: int) -> int:
        if n == 0:
            return 0
        else:
            return n + self.sumNums(n - 1)


print(Solution().sumNums(5))
