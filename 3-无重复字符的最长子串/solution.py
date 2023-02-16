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

    def f(self, s: str):
        if not s:
            return 0
        left, right = 0, 1
        max_len = 1
        while left < right and right < len(s):
            if s[right] in s[left:right]:
                max_len = max(max_len, right - left)
                left = s.index(s[right], left, right) + 1
            right += 1
        max_len = max(max_len, right - left)
        return max_len

    def lengthOfLongestSubstring2(self, s: str) -> int:
        """
       :type s: str
       :rtype: int
       """
        if len(s) <= 1:
            return len(s)
        left = 0
        right = 1
        max_len = 0
        while left < right and right < len(s):
            tmp = s[left:right]
            if s[right] in tmp:
                max_len = (right - left) if max_len < (right - left) else max_len
                left = s.index(s[right], left, right) + 1
            right += 1
        max_len = max(max_len, right - left)
        return max_len


if __name__ == '__main__':
    s = 'aaaaaabbbc'
    solution = Solution()
    print(solution.lengthOfLongestSubstring2(s))
