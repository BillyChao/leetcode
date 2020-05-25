# -*- coding: utf-8 -*-

class Solution:
    def fourSum(self, nums, target):
        result = []
        length = len(nums)
        if not nums or length < 4:
            return result
        nums.sort()
        for i in range(length - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            min1 = nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3]
            if min1 > target:
                break
            max1 = nums[i] + nums[length - 1] + nums[length - 2] + nums[length - 3]
            if max1 < target:
                continue
            for k in range(i + 1, length - 2):
                if k > (i + 1) and nums[k] == nums[k - 1]:
                    continue
                j = k + 1
                h = length - 1
                min2 = nums[i] + nums[k] + nums[j] + nums[j + 1]
                if min2 > target:
                    break
                max2 = nums[i] + nums[k] + nums[h] + nums[h - 1]
                if max2 < target:
                    continue
                while j < h:
                    cur = nums[i] + nums[k] + nums[j] + nums[h]
                    if cur == target:
                        result.append([nums[i], nums[k], nums[j], nums[h]])
                        j += 1
                        while j < h and nums[j] == nums[j - 1]:
                            j += 1
                        h -= 1
                        while j < h and nums[h] == nums[h + 1]:
                            h -= 1
                    elif cur > target:
                        h -= 1
                    else:
                        j += 1
        return result


if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    solution = Solution()
    print(solution.fourSum(nums, target))
