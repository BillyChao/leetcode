# -*- coding:utf-8 -*-

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        s_len = len(s)
        step = numRows * 2 - 2
        zig = list()
        if numRows == 1:
            return s
        for line in range(numRows):
            index = line
            add = line * 2
            while index < s_len:
                zig.append(s[index])
                add = step - add
                index = index + (step if line in [0, numRows - 1] else add)
        return ''.join(zig)


if __name__ == '__main__':
    grid = "PAYPALISHIRING"
    solution = Solution()
    oranges_rotting = solution.convert(grid, 4)
    print(oranges_rotting)
