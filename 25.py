# -*- coding:utf-8 -*-

class Solution:
    def intToRoman(self, num: int) -> str:
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        index = 0
        res = ''
        while index < len(nums):
            # 注意：这里是等于号，表示尽量使用大的"面值"
            while num >= nums[index]:
                res += romans[index]
                num -= nums[index]
            index += 1
        return res

    def intToRoman2(self, num: int) -> str:
        trans_map = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M', 4: 'IV', 9: 'IX', 40: 'XL',
                     90: 'XC', 400: 'CD', 900: 'CM'}
        res = ''
        for i in sorted(trans_map.keys(), reverse=True):
            div, num = divmod(num, i)
            if div > 0:
                res += trans_map[i] * div
            if num == 0:
                break
        return res
