# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null
        :type head: Node
        :rtype: Node
        """
        temp = head
        node_list = []
        node_map = {}
        index = 0
        while temp:
            node_list.append((Node(temp.val), temp.random))
            node_map[temp] = index
            temp = temp.next
        for i in range(len(node_list)):
            if i < len(node_list) - 1:
                node_list[i][0].next = node_list[i + 1][0]
            node_list[i][0].random = None if node_list[i][1] is None else node_list[node_map[node_list[i][1]]][0]
        return node_list[0][0]


if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n1.next = n2
    n1.random = None
    n2.random = n1
    random_list = Solution.copyRandomList(n1)
