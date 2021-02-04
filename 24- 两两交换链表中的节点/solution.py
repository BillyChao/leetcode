# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/2 4:22 下午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        dummyHead.next = head
        temp = dummyHead
        while temp.next and temp.next.next:
            node1 = temp.next
            node2 = temp.next.next
            node1.next = node2.next
            node2.next = node1
            temp.next = node2
            temp = node1
        return dummyHead.next
