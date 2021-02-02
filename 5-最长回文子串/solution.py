# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/2 10:06 上午
@Author  : mc
@File    : olution.py
@Software: PyCharm
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        超时间限制
        :param s:
        :return:
        """
        if len(set(s)) == 1:
            return s
        if len(s) == len(set(s)):
            return s[0]
        max_len = 1
        max_str = s[0]
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                if s[i:j] == s[i:j][::-1] and max_len < (j - i):
                    max_len = (j - i)
                    max_str = s[i:j]
        return max_str

    def spread(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]

    def longestPalindrome1(self, s: str) -> str:
        if s == s[::-1]:
            return s
        res = s[:1]
        for i in range(len(s)):
            odd = self.spread(s, i, i)
            even = self.spread(s, i, i + 1)
            res = max(odd, even, res, key=len)
        return res


if __name__ == '__main__':
    s = 'a'
    solution = Solution()
    print(solution.longestPalindrome(s))
    print(solution.longestPalindrome1(s))
