# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/20 10:45 上午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""

import math


class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3: return n - 1
        a, b = n // 3, n % 3
        if b == 0:
            return int(math.pow(3, a))
        elif b == 1:
            return int(math.pow(3, a - 1) * 4)
        else:
            return int(math.pow(3, a) * 2)
