# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/3 3:56 下午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


class Solution:
    def canJump(self, nums: list) -> bool:
        """
        right 代表能到达的最远位置
        :param nums:
        :return:
        """
        n, right = len(nums), 0
        for i in range(n):
            if i <= right:
                right = max(i + nums[i],right)
                if right >= (n - 1):
                    return True
        return False


if __name__ == '__main__':
    nums = [0,2,3]
    solution = Solution()
    print(solution.canJump(nums))
