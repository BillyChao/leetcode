# -*- coding: utf-8 -*-

"""
@Time    : 2021/3/2 10:59 下午
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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        先分别计算两个链表的长度，长的先走m-n步，如果相交一定可以碰到
        :param headA:
        :param headB:
        :return:
        """
        if not headA or not headB:
            return None
        tmpA, tmpB = headA, headB
        a, b = 0, 0
        while tmpA:
            a += 1
            tmpA = tmpA.next
        while tmpB:
            b += 1
            tmpB = tmpB.next
        diff = abs(a - b)
        if a < b:
            while diff > 0:
                headB = headB.next
                diff -= 1
        else:
            while diff > 0:
                headA = headA.next
        while headA and headB:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        return None
