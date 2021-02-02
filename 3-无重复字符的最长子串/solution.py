# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/1 6:30 下午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        if len(set(s)) == len(s):
            return len(s)
        left = 0
        right = 1
        max_len = 0
        while right < len(s):
            if s[right] in s[left:right]:
                if (right - left) > max_len:
                    max_len = (right - left)
                left = s.index(s[right], left, right) + 1
            right += 1
        if (right - left) > max_len:
            max_len = (right - left)
        return max_len


if __name__ == '__main__':
    s = 'abcabcbb'
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s))
