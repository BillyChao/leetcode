# -*- coding: utf-8 -*-

"""
@Time    : 2023/2/16 下午10:26
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""

# Definition for singly-linked list.
# https://leetcode.cn/problems/linked-list-cycle-ii/
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        slow = fast = head
        while slow and fast:
            if fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            else:
                return None
            if slow == fast:
                break
        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow