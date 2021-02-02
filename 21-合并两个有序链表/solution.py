# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/2 2:09 下午
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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        head = tmp = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        if l1:
            tmp.next = l1
        if l2:
            tmp.next = l2
        return head.next


if __name__ == '__main__':
    n0 = ListNode(0)
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n0.next = n1
    n1.next = n2
    n2.next = n3
    n00 = ListNode(4)
    n11 = ListNode(5)
    n22 = ListNode(7)
    n00.next = n11
    n11.next = n22

    solution = Solution()
    head = solution.mergeTwoLists(n0, n00)
    while head:
        print(head.val)
        head = head.next
