# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/21 6:15 下午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


def checkInclusion(s1: str, s2: str) -> bool:
    left = right = 0
    need = {}
    window = {}
    for c in s1:
        need[c] = need.get(c, 0) + 1
    valid = 0
    while right < len(s2):
        if s2[right] in s1:
            window[s2[right]] = window.get(s2[right], 0) + 1
            if window[s2[right]] == need[s2[right]]:
                valid += 1
        right += 1
        while right - left >= len(s1):
            if valid == len(need):
                return True
            c = s2[left]
            if c in s1:
                if window[c] == need[c]:
                    valid -= 1
                window[c] = window.get(c, 1) - 1
            left += 1
    return False


print(checkInclusion('abcdxabcde', 'abcdeabcdx'))

