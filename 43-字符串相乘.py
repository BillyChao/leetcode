# -*- coding: utf-8 -*-

"""
@Time    : 2020/7/14 下午11:41
@Author  : mc
@File    : 43-字符串相乘.py
@Software: PyCharm
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        mid = []
        count = 0
        for i in num1[::-1]:
            carry = 0
            tmp = ['0' for _ in range(count)]
            for j in num2[::-1]:
                j_ = int(i) * int(j)
                carry, res = divmod(j_ + carry, 10)
                tmp.append(res)
            if carry > 0:
                tmp.append(carry)
            mid.append(''.join(map(lambda x: str(x), tmp[::-1])))
            count += 1
        result = mid[0]
        for i in range(1, len(mid)):
            result = self.strSum(result, mid[i])
        return result

    def strSum(self, s1, s2):
        s1 = s1[::-1]
        s2 = s2[::-1]
        tmp = []
        carry = 0
        i = j = 0
        while i < len(s1) or j < len(s2):
            c1 = '0'
            if i < len(s1):
                c1 = s1[i]
                i += 1
            c2 = '0'
            if j < len(s2):
                c2 = s2[j]
                j += 1
            c_ = int(c1) + int(c2)
            carry, res = divmod(c_ + carry, 10)
            tmp.append(res)
        if carry > 0:
            tmp.append(carry)
        return ''.join(map(lambda x: str(x), tmp[::-1]))


if __name__ == '__main__':
    solution = Solution()
    str_sum = solution.multiply('9', '9')
    print(str_sum)
