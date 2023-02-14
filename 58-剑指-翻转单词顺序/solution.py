# -*- coding: utf-8 -*-

"""
@Time    : 2021/3/4 10:59 上午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""

import re


class Solution:
    def reverseWords(self, s: str) -> str:
        ss = re.split('\\s+', s)
        return ' '.join(ss[::-1]).strip()


print(Solution().reverseWords('the sky is blue'))
