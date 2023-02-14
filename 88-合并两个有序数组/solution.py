# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/22 2:11 下午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        空间复杂度为O(m)
        时间复杂度为O(m+n)
        """
        nums1_copy = nums1[:m]
        index = index1 = index2 = 0
        while index1 < m or index2 < n:
            if index1 == m:
                nums1[index] = nums2[index2]
                index2 += 1
            elif index2 == n:
                nums1[index] = nums1_copy[index1]
                index1 += 1
            elif nums1_copy[index1] < nums2[index2]:
                nums1[index] = nums1_copy[index1]
                index1 += 1
            else:
                nums1[index] = nums2[index2]
                index2 += 1
            index += 1
        return nums1

    def merge1(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        空间复杂度为O(1)
        时间复杂度为O(m+n)
        """
        p = m - 1
        p1 = m + n - 1
        q = n - 1
        while p >= 0 and q >= 0:
            if nums1[p] < nums2[q]:
                nums1[p1] = nums2[q]
                q -= 1
            else:
                nums1[p1] = nums1[p]
                p -= 1
            p1 -= 1
        nums1[:q + 1] = nums2[:q + 1]
        return nums1

    def merge2(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        空间复杂度为O(1)
        时间复杂度为O(m+n)
        """
        p = m - 1
        q = n - 1
        z = m + n - 1
        while p >= 0 and q >= 0:
            if nums1[p] <= nums2[q]:
                nums1[z] = nums2[q]
                q -= 1
            else:
                nums1[z] = nums1[p]
                p -= 1
            z -= 1
        if q >= 0:
            nums1[:q+1] = nums2[:q+1]


print(Solution().merge2([1, 2, 3,0,0,0], 3, [2, 5, 6], 3))
