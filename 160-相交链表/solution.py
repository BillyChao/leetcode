# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/26 6:54 下午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


# Definition for a binary tree node.
# https://leetcode.cn/problems/intersection-of-two-linked-lists/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        利用set
        :param headA:
        :param headB:
        :return:
        """
        if not headA or not headB:
            return None
        if headA == headB:
            return headA
        ss = {headA, headB}
        while headA and headB:
            headA = headA.next
            headB = headB.next
            if headA and headA in ss:
                return headA
            elif headA:
                ss.add(headA)
            if headB and headB in ss:
                return headB
            elif headB:
                ss.add(headB)

        if headA:
            while headA:
                headA = headA.next
                if headA in ss:
                    return headA
        if headB:
            while headB:
                headB = headB.next
                if headB in ss:
                    return headB
        return None

    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        求出各自长度，长度长的先走 diff步，之后同时走
        :param headA:
        :param headB:
        :return:
        """
        if not headA or not headB:
            return None
        h1, h2 = headA, headB
        lenA = lenB = 0
        while h1:
            lenA += 1
            h1 = h1.next
        while h2:
            lenB += 1
            h2 = h2.next
        if lenA < lenB:
            for i in range(0, lenB - lenA):
                headB = headB.next
        elif lenA > lenB:
            for i in range(0, lenA - lenB):
                headA = headA.next

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None

    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        每个指针遍历完整的headA + headB
        :param headA:
        :param headB:
        :return:
        """
        if not headA or not headB:
            return None
        h1, h2 = headA, headB

        while h1 != h2:
            if not h1:
                h1 = headB
            else:
                h1 = h1.next
            if not h2:
                h2 = headA
            else:
                h2 = h2.next
        return h1
