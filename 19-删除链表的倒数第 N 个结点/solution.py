# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/5 6:01 下午
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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        双指针，其中一个先走n步
        :param head:
        :param n:
        :return:
        """
        result = ListNode(0)
        result.next = head
        temp = temp1 = result
        while n > 0:
            temp = temp.next
            n -= 1
        while temp.next:
            result = result.next
            temp = temp.next
        result.next = result.next.next
        return temp1.next


if __name__ == '__main__':
    n0 = ListNode(1)
    n1 = ListNode(2)
    n0.next = n1
    solution = Solution()
    head = solution.removeNthFromEnd(n0, 2)
    while head:
        print(head.val)
        head = head.next
