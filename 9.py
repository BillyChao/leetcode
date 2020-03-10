# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字
        :type head: ListNode
        :rtype: ListNode
        """
        ph = ListNode(0)
        ph.next = head
        p = ph
        while p:  # p 是当前处理的节点的前一个节点，只有保存前一个节点才有办法删掉当前节点
            if not p.next: break
            q = p.next  # q 是当前处理的节点
            r = q.next
            while r:  # 使用 r 往后查找是否有与当前节点（q）重复的节点
                if r.val != q.val:
                    break
                r = r.next
            if r != q.next:  # 如果有重复的，删除这些节点
                p.next = r
            else:
                p = p.next
        return ph.next

    def deleteDuplicates_self(self,head):
        """
        自己的解法，思路不清晰
        :param head:
        :return:
        """
        if head is None:
            return None
        temp = head
        new_head = None
        pre_temp = None
        while True:
            if temp == head and (temp.next is None or temp.next.val != temp.val):
                new_head = temp
                pre_temp = temp
            if temp.next and temp.val != temp.next.val:
                if temp.next.next is None or temp.next.val != temp.next.next.val:
                    if new_head is None:
                        new_head = temp.next
                        pre_temp = temp.next
                    else:
                        pre_temp.next = temp.next
                        pre_temp = temp.next
            temp = temp.next
            if temp is None:
                break
        if pre_temp:
            pre_temp.next = None
        return new_head


if __name__ == '__main__':
    n7 = ListNode(5)
    n6 = ListNode(4)
    n5 = ListNode(3)
    n4 = ListNode(2)
    n3 = ListNode(1)
    n2 = ListNode(1)
    head = ListNode(1)
    head.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    solution = Solution()
    new_head = solution.deleteDuplicates(head=head)
    while new_head:
        print(new_head.val)
        new_head = new_head.next
