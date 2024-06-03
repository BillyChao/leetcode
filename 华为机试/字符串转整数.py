# -*- coding:utf-8 -*-
# @FileName  :test.py
# @Time      :2023/9/20 7:44 PM
# @Author    :mengchao01


def myAtoi(s: str) -> int:
    if len(s) == 0:
        return None

    max_int = 2 ** 31 - 1
    min_int = - 2 ** 31
    s = s.lstrip(' ')
    sign = '+'
    result = 0
    for i in range(len(s)):
        if i == 0 and s[i] == '-':
            sign = '-'
        elif i == 0 and s[i] == '+':
            sign = '+'
        else:
            if s[i].isdigit():
                if sign == '+':
                    if result * 10 + int(s[i]) > max_int:
                        break
                if sign == '-':
                    if -(result * 10 + int(s[i])) < min_int:
                        break
                result = result * 10 + int(s[i])
            else:
                break
    result = result if sign == '+' else -1 * result
    return result


if __name__ == "__main__":
    s = "-422323"
    print(myAtoi(s))
