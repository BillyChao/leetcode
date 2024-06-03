# -*- coding:utf-8 -*-
# @FileName  :滑动窗口最大值.py
# @Time      :2023/9/19 12:01 AM
# @Author    :mengchao01

import heapq
import math
from io import StringIO


class Solution:
    def maxSlidingWindow(self, nums: list, k: int) -> list:
        """
        最小堆解法
        :param nums:
        :param k:
        :return:
        """
        _tmp = [(-v, i) for i, v in enumerate(nums)]
        heapq.heapify(_tmp)
        result = [-_tmp[0][0]]
        for i in range(k, len(nums)):
            heapq.heappush(_tmp, (-nums[i], i))
            while _tmp[0][1] <= i - k:
                heapq.heappop(_tmp)
            result.append(-_tmp[0][0])
        return result

    def maxSlidingWindow1(self, nums, k: int):
        if k == len(nums):
            return [max(nums)]
        result = []
        i = 0
        while i + k <= len(nums):
            result.append(max(nums[i:i + k]))
            i += 1
        return result


def getHeap(data: list):
    heap = []
    for n in data:
        print('add {:>3}:'.format(n))
        heapq.heappush(heap, n)
        print(heap)
        show_tree(heap)


def show_tree(tree, total_width=36, fill=' '):
    """Pretty-print a tree.
    tree 最小堆，层序遍历
    """
    output = StringIO()
    last_row = -1
    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i + 1, 2)))
        else:
            row = 0
        if row != last_row:
            output.write('\n')
        columns = 2 ** row
        col_width = int(math.floor(total_width / columns))
        output.write(str(n).center(col_width, fill))
        last_row = row
    print(output.getvalue())
    print('-' * total_width)
    print()


if __name__ == '__main__':
    # print(Solution().maxSlidingWindow([9, 10, 9, -7, -4, -8, 2, -6], 5))
    getHeap(data=[19, 9, 4, 10, 11])
