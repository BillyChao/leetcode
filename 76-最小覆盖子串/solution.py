# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/21 11:31 上午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0
        res = ''
        need = dict()
        for c in t:
            need[c] = need.get(c, 0) + 1
        window = dict()
        valid = 0
        while right < len(s):
            if s[right] in need:
                window[s[right]] = window.get(s[right], 0) + 1
                if window[s[right]] == need[s[right]]:
                    valid += 1
            right +=1
            while valid == len(need):
                if not res or (right - left ) < len(res):
                    res = s[left:right ]
                if s[left] in need:
                    window[s[left]] = window.get(s[left], 1) - 1
                    if window[s[left]]< need[s[left]]:
                        valid -= 1
                left += 1
        return res


solution = Solution()
print(solution.minWindow('bba', 'ab'))
