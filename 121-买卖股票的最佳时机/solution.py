# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/19 11:29 下午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


class Solution:
    def maxProfit(self, prices: list) -> int:
        min_price = prices[0]
        max_earn = 0
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                t = prices[i] - min_price
                if t > max_earn:
                    max_earn = t
        return max_earn


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    solution = Solution()
    print(solution.maxProfit(prices))
