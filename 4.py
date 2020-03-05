# -*- coding:utf-8 -*-

from collections import Counter


class Solution:
    """
    给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组
    给定数组 nums = [-1, 0, 1, 2, -1, -4],满足要求的三元组集合为：[[-1, 0, 1],[-1, -1, 2]]
    思路：
    1.首先将列表排序
    2.定义三个指针，i,j,k其中i指向头元素，j=i+1,k指向尾元素，通过移动j,k两个指针求解和为0的解
    3.三个指针在移动中，都需要记录前一个位置是否与后一个位置元素相同，相同的话继续移动
    """
    def threeSum(self, nums: list):
        result = []
        nums.sort()
        length = len(nums)
        i = 0
        pre_i = i
        while i < length - 2:
            j = i + 1
            k = length - 1
            pre_j = j
            pre_k = k
            if pre_i != i and nums[pre_i] == nums[i]:
                pass
            else:
                while j < k:
                    if pre_j != j and nums[pre_j] == nums[j]:
                        pre_j = j
                        j += 1
                    elif pre_k != k and nums[pre_k] == nums[k]:
                        pre_k = k
                        k -= 1
                    elif (nums[i] + nums[j] + nums[k]) < 0:
                        pre_j = j
                        j += 1
                    elif (nums[i] + nums[j] + nums[k]) > 0:
                        pre_k = k
                        k -= 1
                    elif (nums[i] + nums[j] + nums[k]) == 0:
                        result.append([nums[i], nums[j], nums[k]])
                        pre_j = j
                        j += 1
                        pre_k = k
                        k -= 1
            pre_i = i
            i += 1
        return result


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    three_sum = solution.threeSum(nums)
    print(three_sum)
