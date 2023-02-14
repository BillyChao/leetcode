# -*- coding: utf-8 -*-

"""
@Time    : 2021/3/2 6:44 下午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


class Solution:
    def verifyPostorder(self, postorder: list) -> bool:
        def recur(i, j):
            if i >= j:
                return True
            p = i
            while postorder[p] < postorder[j]:
                p += 1
            m = p
            while postorder[p] > postorder[j]:
                p += 1
            return p == j and recur(i, m - 1) and recur(m, j - 1)

        return recur(0, len(postorder) - 1)


print(Solution().verifyPostorder([1, 2, 5, 10, 6, 9, 4, 3]))
