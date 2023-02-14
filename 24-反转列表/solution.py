# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/22 11:52 上午
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
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        left = None
        right = head
        while right:
            tmp = right.next
            right.next = left
            left = right
            right = tmp
        return left


n0 = ListNode(0)
n1 = ListNode(1)
n0.next = n1
solution = Solution()
res = solution.reverseList(n0)
while res:
    print(res.val)
    res = res.next
