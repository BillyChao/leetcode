# -*- coding: utf-8 -*-

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: list) -> ListNode:
        """
        利用Python中的最小堆实现heapq
        :param lists:
        :return:
        """
        result = p = ListNode(0)
        heap = []
        import heapq
        # import heapq
        # dummy = ListNode(0)
        # p = dummy
        # head = []
        # for i in range(len(lists)):
        #     if lists[i]:
        #         heapq.heappush(head, (lists[i].val, i))
        #         lists[i] = lists[i].next
        # while head:
        #     val, idx = heapq.heappop(head)
        #     p.next = ListNode(val)
        #     p = p.next
        #     if lists[idx]:
        #         heapq.heappush(head, (lists[idx].val, idx))
        #         lists[idx] = lists[idx].next
        # return dummy.next
        # merge方法
        for i in range(len(lists)):
            tmp = []
            while lists[i]:
                tmp.append(lists[i].val)
                lists[i] = lists[i].next
            heap.append(tmp)
        merge = heapq.merge(*heap)
        for node in merge:
            p.next = ListNode(node)
            p = p.next
        return result.next


if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(4)
    n3 = ListNode(5)
    n1.next = n2
    n2.next = n3

    n11 = ListNode(1)
    n12 = ListNode(3)
    n13 = ListNode(4)
    n11.next = n12
    n12.next = n13

    n21 = ListNode(2)
    n22 = ListNode(6)
    n21.next = n22

    lists = [n1, n11, n21]
    solution = Solution()
    k_lists = solution.mergeKLists(lists)
    while k_lists:
        print(k_lists.val)
        k_lists = k_lists.next
