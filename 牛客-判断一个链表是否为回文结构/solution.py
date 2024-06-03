# -*- coding: utf-8 -*-

"""
@Time    : 2021/3/2 11:52 下午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
#
# @param head ListNode类 the head
# @return bool布尔型
#
class Solution:
    def isPail(self, head: ListNode):
        """
        快慢指针，找到中点，将[中点 结尾]列表反转，头尾双指针往回走，一直走到中间都相等则为回文链表
        :param head:
        :return:
        """
        if not head:
            return False
        stack = []
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        while slow:
            stack.append(slow.val)
            slow = slow.next
        while stack:
            if head.val != stack.pop():
                return False
            head = head.next
        return True


n0 = ListNode(0)
n1 = ListNode(2)
n2 = ListNode(2)
n3 = ListNode(0)
n0.next = n1
n1.next = n2
n2.next = n3
print(Solution().isPail(n0))
