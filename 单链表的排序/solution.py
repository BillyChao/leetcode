# -*- coding: utf-8 -*-

"""
@Time    : 2023/2/19 下午10:58
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# https://www.nowcoder.com/practice/f23604257af94d939848729b1a5cda08?tpId=295&tqId=1008897&ru=%2Fpractice%2Fb49c3dc907814e9bbfa8437c251b028e&qru=%2Fta%2Fformat-top101%2Fquestion-ranking&sourceUrl=%2Fexam%2Foj
#
# @param head ListNode类 the head node
# @return ListNode类
#
class Solution:
    def sortInList(self, head: ListNode) -> ListNode:
        # write code here
        tmp = []
        tmp.append(head.val)
        # 遍历链表存储到数组中
        while head.next:
            head = head.next
            tmp.append(head.val)
        # 数组排序
        tmp.sort()
        # 重新构造新链表结点
        result = ListNode(-1)
        temp = result
        # 遍历数组，将数组中元素添加到新的链表中
        for i in tmp:
            tt = ListNode(i)
            temp.next = tt
            temp = temp.next
        return result.next
