class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度
        输入: "abcabcbb"
        输出: 3
        解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
        思路：
        滑动窗口，当end指向元素不在[start,end]窗口内的话，则增加max_len
        当end出现在当前窗口内，移动start指针到窗口内该重复元素的下一个位置，end指针始终向前+1移动
        :type s: str
        :rtype: int
        """
        start = 0
        end = 0
        max_len = 1
        length = len(s)
        if s is None or length == 0:
            return 0
        while True:
            end += 1
            if max_len > length - start or end >= length:
                break
            if s[end] not in s[start:end]:
                if (end - start + 1) > max_len:
                    max_len = end - start + 1
            else:
                start = s.find(s[end], start) + 1
        return max_len


if __name__ == '__main__':
    s = 'pwwkew'
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s))
