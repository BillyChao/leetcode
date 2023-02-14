# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/26 11:38 上午
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
    def reversePrint(self, head: ListNode) -> list[int]:
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result[::-1]


def replaceSpace(s: str) -> str:
    ss = []
    for index, ch in enumerate(list(s)):
        if ch == ' ':
            ss.append('%20')
        else:
            ss.append(ch)
    return ''.join(ss)


print(replaceSpace('We are happy.'))
