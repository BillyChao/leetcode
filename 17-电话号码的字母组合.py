# -*- coding: utf-8 -*-

"""
@Time    : 2020/7/12 下午12:01
@Author  : mc
@File    : 17-电话号码的字母组合.py
@Software: PyCharm
"""
import copy


class Solution:
    def letterCombinations(self, digits: str):
        alpha_map = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'],
                     7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}
        tmp = []
        for letter in digits:
            tmp.append(alpha_map[int(letter)])
        result = []
        if tmp:
            result = copy.deepcopy(tmp[0])
        for i in range(1, len(tmp)):
            for j in range(len(result)):
                l = result.pop(0)
                result.extend([l + item for item in tmp[i]])
        return result


if __name__ == '__main__':
    s = '22'
    combinations = Solution().letterCombinations(digits=s)
    print(combinations)
