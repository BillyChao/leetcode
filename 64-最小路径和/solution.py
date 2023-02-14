# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/5 5:30 下午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


class Solution:
    def minPathSum(self, grid: list) -> int:
        """
        首先初始化一个矩阵
        :param grid:
        :return:
        """
        m = len(grid)
        n = len(grid[0])
        for i in range(1, len(grid[0])):
            grid[0][i] = grid[0][i] + grid[0][i - 1]
        for j in range(1, len(grid)):
            grid[j][0] = grid[j][0] + grid[j - 1][0]
        for k in range(1, len(grid)):
            for l in range(1, len(grid[k])):
                grid[k][l] = grid[k][l] + min(grid[k - 1][l], grid[k][l - 1])
        return grid[m - 1][n - 1]


if __name__ == '__main__':
    grid = [[1, 2, 3], [4, 5, 6]]
    solution = Solution()
    print(solution.minPathSum(grid))
