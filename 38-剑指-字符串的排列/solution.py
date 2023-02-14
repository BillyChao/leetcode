# -*- coding: utf-8 -*-

"""
@Time    : 2021/3/2 4:53 下午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


class Solution:
    def permutation(self, s: str) -> list:
        c, res = list(s), []

        def dfs(x):
            if x == len(s) - 1:
                res.append(''.join(c))
                return
            ss = set()
            for i in range(x, len(c)):
                # 用set记录当前固定位置已经设置的值
                if c[i] in ss:
                    continue
                ss.add(c[i])
                # 将c[i] 固定在x位置
                c[x], c[i] = c[i], c[x]
                dfs(x + 1)
                # 结束递归后，恢复位置
                c[x], c[i] = c[i], c[x]

        dfs(0)
        return res


print(Solution().permutation('abac'))
