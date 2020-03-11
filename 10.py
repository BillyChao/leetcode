# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
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


if __name__ =='__main__':
    n1 = Node(1)
    n2 = Node(2)
    n1.next = n2
    n1.random = None
    n2.random = n1
    random_list = Solution.copyRandomList(n1)

