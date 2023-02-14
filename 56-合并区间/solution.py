# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/5 10:33 上午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


class Solution:
    def merge(self, intervals: list):
        intervals.sort(key=lambda x: x[0])

        merged = []
        for item in intervals:
            if not merged:
                merged.append(item)
            elif merged[-1][1] >= item[0]:
                merged[-1] = [merged[-1][0], item[1] if merged[-1][1] < item[1] else merged[-1][1]]
            else:
                merged.append(item)
        return merged


if __name__ == '__main__':
    intervals = [[1, 4], [2, 3]]
    solution = Solution()
    print(solution.merge(intervals))
