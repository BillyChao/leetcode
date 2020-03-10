import copy


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __deepcopy__(self, memo):
        return ListNode(copy.deepcopy(self.val, memo))


class Solution(object):
    def sortList(self, head):
        """
        在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head  # termination.
        # cut the LinkedList at the mid index.
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None  # save and cut.
        # recursive for cutting.
        left, right = self.sortList(head), self.sortList(mid)
        # merge `left` and `right` linked list and return it.
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                h.next, left = left, left.next
            else:
                h.next, right = right, right.next
            h = h.next
        h.next = left if left else right
        return res.next


if __name__ == '__main__':
    n5 = ListNode(0)
    n4 = ListNode(4)
    n3 = ListNode(3)
    n2 = ListNode(5)
    head = ListNode(-1)
    head.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    solution = Solution()
    new_head = solution.sortList(head=head)
    while new_head:
        print(new_head.val)
        new_head = new_head.next
