# -*- coding: utf-8 -*-

"""
@Time    : 2021/3/3 7:37 下午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""

# -*- coding:utf-8 -*-
# @FileName  :test.py
# @Time      :2023/9/13 7:22 PM
# @Author    :mengchao01


# 题目：给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母
'''
示例 1：
输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]

示例 2：
输入：digits = ""
输出：[]

示例 3：
输入：digits = "2"
输出：["a","b","c"]
2：abc
3：def
4：ghi
5、jkl
6、mno
7、pqrs
8、tuv
9、wxyz
'''
import itertools
import time

num_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}


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


def getAll(digits):
    result = [[]]
    for i in digits:
        alphas = num_map.get(i)
        l = len(result)
        for j in range(len(result)):
            tmp = result.pop(0)
            for t in alphas:
                result.append(tmp + [t])
        # result = result[l:]
        # result = [x + [t] for x in result for t in alphas]
    return list(map(lambda x: ''.join(x), result))


result = []
word = ''


def getAll2(digits, index, word):
    if index == len(digits):
        result.append(word)
        return
    for i in num_map[digits[index]]:
        word += i
        getAll2(digits, index + 1, word)
        word = word[:-1]


def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if not digits:
        return []

    l_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
             '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    chars = [l_map.get(d) for d in digits]
    return [''.join(x) for x in itertools.product(*chars)]


def letterCombinations2(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    result = list()
    if not digits:
        return result

    l_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
             '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    chars = [l_map.get(d) for d in digits]
    tmp = [[]]
    for pool in chars:
        tmp = [x + [y] for x in tmp for y in pool]

    for prod in tmp:
        result.append(''.join(prod))

    return result


if __name__ == "__main__":
    digits = "222222333333"
    # start = time.time()
    # getAll2(digits, 0, word)
    # print("getAll2 cost:", time.time() - start)
    # start = time.time()
    # letterCombinations(digits)
    # print("letterCombinations cost:", time.time() - start)
    start = time.time()
    result = getAll(digits)
    print(result)
    print("getAll cost:", time.time() - start)
    # start = time.time()
    # letterCombinations2(digits)
    # print("letterCombinations2 cost:", time.time() - start)
