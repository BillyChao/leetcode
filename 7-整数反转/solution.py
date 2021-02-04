# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/2 6:23 下午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x *= sign
        result = 0
        while x > 0:
            result = result * 10 + (x % 10)
            x //= 10
        result = sign * result
        if result <= -2 ** 31 or result >= 2 ** 31 - 1:
            return 0
        else:
            return result


if __name__ == '__main__':
    x = 12435
    solution = Solution()
    print(solution.reverse(x))
