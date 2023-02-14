# -*- coding: utf-8 -*-

"""
@Time    : 2021/3/4 10:20 上午
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
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        # if not head:
        #     return None
        # tmp = ListNode()
        # tmp.next = head
        # pre = tmp
        # while head:
        #     if head.val != val:
        #         pre = head
        #         head = head.next
        #     else:
        #         pre.next = head.next
        #         break
        # return tmp.next
        if not head:
            return None
        tmp = ListNode()
        tmp.next = head
        pre = tmp
        while head:
            if head.val == val:
                pre.next = head.next
                break
            else:
                pre = head
                head = head.next
        return tmp.next
