# -*- coding: utf-8 -*-

"""
@Time    : 2021/6/5 下午9:32
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip().lower()
        if not s:
            return False
        if 'e' in s:
            index = s.index('e')
            before_e = self.isFloat(s[:index]) or self.isInt(s[:index]) if s[:index] else False
            after_e = self.isInt(s[index + 1:]) if s[index + 1:] else False
            return before_e and after_e
        else:
            return self.isInt(s) or self.isFloat(s)

    def isInt(self, s):
        if '+' == s or '-' == s:
            return False
        for i, c in enumerate(s):
            if c in ['+', '-'] and i == 0:
                continue
            elif not '0' <= c <= '9':
                return False
        return True

    def isFloat(self, s: str):
        if '.' == s:
            return False
        if s[0] == '+':
            s = s.replace('+', '', 1)
        elif s[0] == '-':
            s = s.replace('-', '', 1)
        if '.' in s:
            index = s.index('.')
            if not s[:index]:
                if s[index + 1:] and self.isInt(s[index + 1:]) and '+' not in s[index + 1:] and '-' not in s[index + 1:]:
                    return True
                return False
            elif not s[index + 1:]:
                if self.isInt(s[:index]):
                    return True
                else:
                    return False
            else:
                return self.isInt(s[:index]) and self.isInt(s[index + 1:])
        else:
            return False


if __name__ == '__main__':
    print(Solution().isNumber('+.8'))
