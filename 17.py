# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        """
        描述：给定一棵二叉搜索树，请找出其中第k大的节点
        思路：
        ①中序遍历的结果逆序后取k-1 索引位置数据
        :param root:
        :param k:
        :return:
        """
        l = []

        def mid_traverse(root: TreeNode, nodes: list):
            if not root:
                return nodes
            if root.left:
                mid_traverse(root.left, nodes)
            nodes.append(root.val)
            if root.right:
                mid_traverse(root.right, nodes)

        mid_traverse(root, l)
        return l[::-1][k - 1]

    def kthLargest1(self, root: TreeNode, k: int) -> int:
        """
        思路：
        ① 用stack记录二叉树的所有节点，每次都将所有右节点入栈，没出栈一个元素，index++，当index==k
        表示已经遍历到第k大的数，直接返回
        ②比中序遍历要快，因为不需要将所有的节点都遍历一遍
        :param root:
        :param k:
        :return:
        """
        if not root:
            return None
        stack = []
        index = 0
        while stack or root:
            while root:
                stack.append(root)
                root = root.right
            pop = stack.pop()
            index += 1
            if index == k:
                return pop.val
            root = pop.left


if __name__ == '__main__':
    root = TreeNode(10)
    kth_largest = Solution().kthLargest(root, 1)
    print(kth_largest)
