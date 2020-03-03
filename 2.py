# -*- coding:utf-8 -*-


import numpy as np


class Solution:
    """亲密字符串
    给定两个由小写字母构成的字符串 A 和 B ，只要我们可以通过交换 A 中的两个字母得到与 B 相等的结果，
    就返回 true ；否则返回 false
    """

    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        elif A == B:
            return len(set(A)) < len(A)
        else:
            i_ = [''.join([A[i], B[i]]) for i in range(len(A)) if A[i] != B[i]]
            if len(i_) == 2 and i_[0] == i_[1][::-1]:
                return True
            return False


if __name__ == '__main__':
    A = 'abab'
    B = 'abab'
    solution = Solution()
    print(solution.buddyStrings(A, B))
