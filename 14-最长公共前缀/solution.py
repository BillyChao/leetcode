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


if __name__ == '__main__':
    solution = Solution()
    strs = ["dog", "dog", "dog"]
    print(solution.longestCommonPrefix(strs))
