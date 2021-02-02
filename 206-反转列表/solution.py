# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/1 4:14 下午
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
    def reverseList(self, head: ListNode) -> ListNode:
        """
        双指针
        :param head:
        :return:
        """
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

    def reverseList1(self, head: ListNode) -> ListNode:
        """
        双指针
        :param head:
        :return:
        """
        if not head:
            return None
        nodes = [None]
        while head:
            nodes.append(head)
            head = head.next
        new_head = None
        result = nodes[-1]
        while nodes:
            nodes_pop = nodes.pop()
            if new_head:
                new_head.next = nodes_pop
            new_head = nodes_pop
        return result


if __name__ == '__main__':
    n1 = ListNode(0)
    n2 = ListNode(1, n1)
    n3 = ListNode(2, n2)
    n4 = ListNode(3, n3)
    n5 = ListNode(4, n4)
    solution = Solution()
    reverse_list = solution.reverseList1(n5)
    while reverse_list:
        print(reverse_list.val)
        reverse_list = reverse_list.next
