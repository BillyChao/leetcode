# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/3 11:01 上午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


class Solution(object):
    def threeSum(self, nums):
        result = []
        if len(nums) < 3:
            return result
        nums.sort()
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                temp = [nums[i], nums[j], nums[k]]
                if sum(temp) == 0:
                    if temp not in result:
                        result.append(temp)
                    j += 1
                    k -= 1
                elif sum(temp) > 0:
                    k -= 1
                else:
                    j += 1
        return result

    def threeSum1(self, nums):
        result = []
        nums.sort()
        i = 0
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                while i + 1 < j < k and nums[j] == nums[j - 1]:
                    j += 1
                while j < k and nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                while k > j and nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                if j == k:
                    break
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
            i += 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
        return result


if __name__ == '__main__':
    nums = [1, 1, -2]
    solution = Solution()
    print(solution.threeSum(nums))
