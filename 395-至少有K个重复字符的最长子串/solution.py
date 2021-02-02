# -*- coding: utf-8 -*-

"""
@Time    : 2020/7/18 下午12:27
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        max_len = 0
        _dic = {}
        if k < 2:
            return len(s)
        for c in s:
            if c in _dic:
                _dic[c] += 1
            else:
                _dic[c] = 1
        i = 0
        while i < len(s):
            tmp = {s[i]: 1}
            j = i + 1
            while j < len(s):
                if _dic[s[j]] < k:
                    break
                if s[j] in tmp:
                    tmp[s[j]] += 1
                else:
                    tmp[s[j]] = 1
                j += 1
            if len(list(filter(lambda x: x[1] < k, tmp.items()))) == 0:
                tmp_len = 0
                for _, v in tmp.items():
                    tmp_len += v
                if tmp_len > max_len:
                    max_len = tmp_len
            i += 1
        return max_len

    def longestSubstring2(self, s, k):
        from collections import Counter
        c = Counter()
        n = len(s)
        prefix = [c.copy()]
        for i in range(n):
            c[s[i]] += 1
            prefix.append(c.copy())

        def check(tmp):
            for val in tmp.values():
                if val < k:
                    return False
            return True

        res = 0
        for i in range(n + 1):
            for j in range(i):
                if check(prefix[i] - prefix[j]):
                    res = max(res, i - j)
                    break
        return res

    def longestSubstring3(self, s, k):
        """
        最优解，分治法
        :param s:
        :param k:
        :return:
        """
        if len(s) < k:
            return 0
            # 找个字符串个数最少的字符
        t = min(set(s), key=s.count)
        # 最少字符的个数都大于等于k
        if s.count(t) >= k:
            return len(s)
        return max(self.longestSubstring3(a, k) for a in s.split(t))


if __name__ == '__main__':
    s = 'aaabb'
    k = 3
    solution = Solution()
    i = solution.longestSubstring3(s, k)
    print(i)
