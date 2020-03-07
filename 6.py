# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle_1(self, head):
        """
        给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
        思路:定义一个set，遍历链表，如果存在环，那么set会包含环的入点，否则不存在环直接返回None
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        length = 0
        set_node = set()
        loop = False
        while temp:
            if temp in set_node:
                loop = True
                break
            else:
                set_node.add(temp)
                temp = temp.next
                length += 1
        if loop:
            while head != temp:
                head = head.next
            return head
        else:
            return None

    def detectCycle_2(self, head):
        """
        给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
        思路:第一次相遇后，one节点和head节点分别一步一步走，当head和one再次相遇时，就是环的入点
        :type head: ListNode
        :rtype: ListNode
        """
        one = head
        two = head
        while True:
            if not (two and two.next):
                return None
            one = one.next
            two = two.next.next
            if one == two:
                break
        two = head
        while two != one:
            two = two.next
            one = one.next
        return two


if __name__ == '__main__':
    n4 = ListNode(-4)
    n3 = ListNode(0)
    n2 = ListNode(2)
    head = ListNode(3)
    head.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2
    solution = Solution()
    solution.detectCycle_2(head=head)
