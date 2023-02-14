# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/26 9:45 上午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


def findContinuousSequence(target: int):
    end = int(target / 2) + 1
    left, right = 1, 2
    res = []
    sum = left + right
    while right <= end:
        if sum < target:
            right += 1
            sum += right
        else:
            if sum == target:
                res.append(list(range(left, right + 1, 1)))
            sum -= left
            left += 1
    return res
    # left, right = 1, 2
    # result = []
    # while left < right:
    #     sum = (left + right) * (right - left + 1) / 2
    #     if sum == target:
    #         result.append([i for i in range(left, right + 1)])
    #         left += 1
    #     elif sum < target:
    #         right += 1
    #     else:
    #         left += 1
    # return result


print(findContinuousSequence(9))
