# -*- coding: utf-8 -*-

"""
@Time    : 2020/7/10 下午1:57
@Author  : mc
@File    : 29-前 K 个高频元素.py
@Software: PyCharm
"""


class Solution:
    def topKFrequent(self, nums, k):
        # 该解法不满足时间复杂度
        dic_num = dict()
        for i in nums:
            dic_num[i] = 0
        for i in nums:
            dic_num[i] += 1
        l = sorted(dic_num.items(), key=lambda x: x[1], reverse=True)
        return list(map(lambda x: x[0], l))[:k]

    def topKFrequent2(self, nums, k):
        # 利用最小堆排序
        dic_num = dict()
        for i in nums:
            dic_num[i] = 0
        for i in nums:
            dic_num[i] += 1
        import heapq
        items_ = [(-v, k) for k, v in dic_num.items()]
        heapq.heapify(items_)
        result = []
        for i in range(k):
            result.append(heapq.heappop(items_)[1])
        return result


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    solution = Solution()
    print(solution.topKFrequent2(nums, k))
