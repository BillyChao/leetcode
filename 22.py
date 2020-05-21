# -*- coding:utf-8 -*-
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        解法一:两层for循环遍历
        :param s:
        :return:
        """
        max_len = 0
        result = ''
        s_len = len(s)
        for i in range(s_len + 1):
            if (s_len - i) < max_len:
                break
            for j in range(i + 1, s_len + 1):
                if s[i:j] == s[i:j][::-1] and (j - i) > max_len:
                    result = s[i:j]
                    max_len = max(max_len, len(result))
        return result

    def longestPalindrome2(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        # 枚举子串的长度 l+1
        for l in range(n):
            # 枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
            for i in range(n):
                j = i + l
                if j >= len(s):
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and l + 1 > len(ans):
                    ans = s[i:j + 1]
        return ans

    def spread(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]

    def longestPalindrome3(self, s: str) -> str:
        if s == s[::-1]:
            return s
        res = s[:1]
        for i in range(len(s)):
            odd = self.spread(s, i, i)
            even = self.spread(s, i, i + 1)
            res = max(odd, even, res, key=len)
        return res

if __name__ == '__main__':
    grid = "babad"
    solution = Solution()
    oranges_rotting = solution.longestPalindrome2(grid)
    print(oranges_rotting)
