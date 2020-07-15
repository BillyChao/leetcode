# -*- coding: utf-8 -*-

"""
@Time    : 2020/7/13 下午11:33
@Author  : mc
@File    : 19-删除链表的倒数第N个节点.py
@Software: PyCharm
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 空间复杂度较高，需要额外空间存放每个节点元素，第一次遍历将所有元素保存在list中
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
        nodes.pop(-n)
        result = tmp = ListNode(0)
        for value in nodes:
            tmp.next = ListNode(value)
            tmp = tmp.next
        return result.next

    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        # 双指针，一次遍历，且空间复杂度低O(1) 两个指针间隔为n,当后指针指向null的时候，前指针在要删除节点的前一位置
        node = ListNode(0)
        node.next = head
        left = right = node
        # 这里不需要检查right是否为空，因为n始终是有效的数字
        for i in range(n + 1):
            right = right.next
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return node.next
