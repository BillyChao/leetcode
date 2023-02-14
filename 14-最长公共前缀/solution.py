# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/2 11:55 上午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        if len(strs) == 0:
            return ''
        for item in strs:
            if len(item) == 0:
                return ''
        result = ''
        min_len = min([len(item) for item in strs])
        for i in range(1, min_len + 1):
            sub_set = {item[:i] for item in strs}
            if len(sub_set) == 1:
                result = strs[0][:i]
            else:
                break
        return result

    def longestCommonPrefix1(self, strs: list) -> str:
        """
        reduce 的想法，先计算 strs[0] strs[1]的 最长公共前缀，再求解上一步结果与 strs[2]的最长公共前缀
        :param strs:
        :return:
        """
        if not strs:
            return ''
        result, count = strs[0], len(strs)
        for i in range(1, count):
            result = self.helper(result, strs[i])
            if not result:
                return ''
        return result

    def helper(self, s1, s2):
        """
        求解两个字符串的最长公共前缀
        :param s1:
        :param s2:
        :return:
        """
        index =0
        while index <min(len(s1), len(s2)):
            if s1[index] != s2[index]:
                break
            index +=1
        return s1[:index]


if __name__ == '__main__':
    solution = Solution()
    strs = ["dog","dog","dog"]
    print(solution.longestCommonPrefix1(strs))
