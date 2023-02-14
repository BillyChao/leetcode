# -*- coding: utf-8 -*-

"""
@Time    : 2021/3/20 11:40 下午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        s = list(s)
        for _ in range(n):
            s.append(s.pop(0))
        return ''.join(s)


print(Solution().reverseLeftWords("abcdefg", 2))
