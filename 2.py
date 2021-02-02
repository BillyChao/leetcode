# -*- coding:utf-8 -*-


class Solution:
    """亲密字符串
    给定两个由小写字母构成的字符串 A 和 B ，只要我们可以通过交换 A 中的两个字母得到与 B 相等的结果
    两个字母的位置不一定是相邻的，可以是任意俩位置的字母
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

    def buddyStrings2(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if A == B and len(set(A)) < len(A):
            return True
        s = [''.join([A[i], B[i]]) for i in range(len(A)) if A[i] != B[i]]
        if len(s) == 2 and s[0] == s[1][::-1]:
            return True
        return False

    def buddyStrings_20210201(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if A == B and len(A) > len(set(A)):
            return True
        a = b = ''
        for i in range(len(A)):
            if A[i] != B[i]:
                a += A[i]
                b += B[i]
        if len(a) == 2 and a[::-1] == b:
            return True
        return False


if __name__ == '__main__':
    A = 'aba'
    B = 'baa'
    solution = Solution()
    print(solution.buddyStrings3(A, B))
