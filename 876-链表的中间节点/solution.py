# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/21 11:06 上午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        left = right = head
        while right and right.next:
            left = left.next
            right = right.next.next
        return left
