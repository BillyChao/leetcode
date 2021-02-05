# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/4 6:28 下午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


class Solution:
    def findString(self, words: list, s: str):
        for index, item in enumerate(words):
            if item == s:
                return index
        return -1
