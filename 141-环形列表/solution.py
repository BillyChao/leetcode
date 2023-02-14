# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/5 10:50 上午
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
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        temp1 = temp2 = head
        while temp1 and temp2:
            if not temp1.next:
                return False
            temp1 = temp1.next
            if not temp2.next:
                return False
            temp2 = temp2.next.next
            if temp1 == temp2:
                return True
        return False


if __name__ == '__main__':
    n0 = ListNode(0)
    n1 = ListNode(1)
    n2 = ListNode(1)
    n3 = ListNode(1)
    n4 = ListNode(1)
    n0.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n3

    solution = Solution()
    print(solution.hasCycle(n0))
