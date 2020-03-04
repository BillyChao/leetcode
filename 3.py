import numpy as np


class Solution:
    """
    给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序
    思路：

    """

    def reverseWords(self, s: str) -> str:
        s_split = s.split(' ')
        if len(s_split) < 1:
            return s
        else:
            return ' '.join([item[::-1] for item in s_split])


if __name__ == '__main__':
    s = 'Let\'s take LeetCode contest'
    s1 = 'aaass'
    solution = Solution()
    print(solution.reverseWords(s1))
