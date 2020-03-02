# -*- coding:utf-8 -*-


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        验证回文串，不考虑非字母+数字的情况
        :param s:
        :return:
        """
        s = ''.join(filter(str.isalnum, s)).lower()
        begin = 0
        length = len(s)
        end = length - 1
        if length == 0 or s is None:
            return True
        else:
            while begin < end:
                if s[begin] == s[end]:
                    begin += 1
                    end -= 1
                else:
                    return False
        return True


if __name__ == '__main__':
    solution = Solution()
    s = 'ababc'
    print(solution.isPalindrome(s))
