# -*- coding: utf-8 -*-

"""
@Time    : 2020/7/16 上午10:45
@Author  : mc
@File    : 393-UTF-8 编码验证.py
@Software: PyCharm
"""


class Solution:
    def validUtf8(self, data) -> bool:
        binary = []
        # 将数组中的十进制数，都转为二进制，且保留8位，不足8位用0填充
        for number in data:
            binary.append(format(number, '#010b')[-8:])
        index = 0
        while index < len(data):
            if binary[index].startswith('0'):
                index += 1
            elif binary[index].startswith('1'):
                num = 0
                for i in range(len(binary[index])):
                    if binary[index][i] == '1':
                        num += 1
                    else:
                        break
                if (len(data) - index) < num or num > 4 or num == 1:
                    return False
                for j in range(index + 1, index + num):
                    if not binary[j].startswith('10'):
                        return False
                index = index + num
        return True


if __name__ == '__main__':
    data = [145]
    solution = Solution()
    print(solution.validUtf8(data))
