# -*- coding: utf-8 -*-

"""
@Time    : 2021/3/3 7:37 下午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


class Solution:
    def letterCombinations(self, digits: str) -> list:
        alpha_map = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'],
                     7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}
        res = []
        for ch in digits:
            if not res:
                res = alpha_map[int(ch)][:]
            else:
                l = len(res)
                index = 0
                for item in res:
                    index += 1
                    for c in alpha_map[int(ch)]:
                        res.append(item + c)
                    if index == l:
                        res = res[l:]
                        break
        return res


print(Solution().letterCombinations('22'))
