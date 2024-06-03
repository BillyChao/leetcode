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

    def lengthOfLongestSubstring3(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        left, right = 0, 1
        max_len = 1
        while left < right and right < len(s):
            tmp = s[left:right]
            if s[right] in tmp:
                max_len = max(max_len, right - left)
                left = s.index(s[right], left, right) + 1
            right += 1
        max_len = max(max_len, right - left)
        return max_len


class LongestConsecutive:
    def longestConsecutive(self, nums) -> int:
        if len(nums) < 2:
            return len(nums)
        nums.sort()
        l = 0
        max_len = tmp = 1
        while l < len(nums) - 1:
            if nums[l + 1] == nums[l] + 1:
                tmp += 1
            elif nums[l + 1] == nums[l]:
                pass
            else:
                tmp = 1
            max_len = max(max_len, tmp)
            l += 1
        return max_len


if __name__ == '__main__':
    s = 'abcabcbb'
    solution = LongestConsecutive()
    # print(solution.longestConsecutive([0, 0, -1]))
    l = [1,2,3]
    print(l.index(1))
