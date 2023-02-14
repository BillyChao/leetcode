# -*- coding: utf-8 -*-

"""
@Time    : 2021/7/22 下午8:13
@Author  : mc
@File    : soluiton.py
@Software: PyCharm
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]
示例 2：

输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def twoSum(nums: list, target: int):
    begin, end = 0, len(nums)-1
    while begin < end:
        if nums[begin] + nums[end] > target:
            end -= 1
        elif nums[begin] + nums[end] < target:
            begin += 1
        else:
            return [nums[begin], nums[end]]
    return None


if __name__ == '__main__':
    print(twoSum([11, 20, 20, 31, 47, 60], 40))
