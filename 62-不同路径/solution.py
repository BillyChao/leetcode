# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/3 2:55 下午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


class Solution:
    def util(self, l, r, m, n):
        if l < m and r < n:
            return self.util(l + 1, r, m, n) + self.util(l, r + 1, m, n)
        if l < m:
            return self.util(l + 1, r, m, n)
        if r < n:
            return self.util(l, r + 1, m, n)
        if l == m and r == n:
            return 1

    def uniquePaths(self, m: int, n: int) -> int:
        l = r = 1
        return self.util(l, r, m, n)

    def uniquePaths2(self, m: int, n: int) -> int:
        """
        动态规划
        :param m:
        :param n:
        :return:
        """
        f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[m - 1][n - 1]


if __name__ == '__main__':
    m = 3
    n = 2
    solution = Solution()
    print(solution.uniquePaths2(m, n))
