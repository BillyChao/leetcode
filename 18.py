class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """
        给定一个二叉树，找出其最小深度。最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
        思路：
        叶子节点的定义是左孩子和右孩子都为 null 时叫做叶子节点
        当 root 节点左右孩子都为空时，返回 1
        当 root 节点左右孩子有一个为空时，返回不为空的孩子节点的深度
        当 root 节点左右孩子都不为空时，返回左右孩子较小深度的节点值
        :param root:
        :return:
        """
        if not root:
            return 0
        d1 = self.minDepth(root.left)
        d2 = self.minDepth(root.right)
        if root.left is None or root.right is None:
            return d1+d2+1
        else:
            return 1 + min(d1, d2)
