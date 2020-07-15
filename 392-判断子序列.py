# -*- coding: utf-8 -*-

"""
@Time    : 2020/7/15 下午5:08
@Author  : mc
@File    : 392-判断子序列.py
@Software: PyCharm
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        建立一个n*26的二维数组，n表示t的长度，26表示26个字母在t中每个位置上，下一次出现的位置
        :param s:
        :param t:
        :return:
        """
        t = ' ' + t
        vec = [[0 for _ in range(26)] for _ in range(len(t))]
        for j in range(26):
            pos = -1
            for i in range(len(t) - 1, -1, -1):
                vec[i][j] = pos
                if t[i] == chr(ord('a') + j):
                    pos = i
        index = 0
        for c in s:
            index = vec[index][ord(c) - ord('a')]
            if index == -1:
                return False
        return True
