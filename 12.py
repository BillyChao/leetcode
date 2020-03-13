# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        """
        请完成一个函数，输入一个二叉树，该函数输出它的镜像。
        :param root:
        :return:
        """
        if not root:
            return root
        if root.left:
            self.mirrorTree(root.left)
        if root.right:
            self.mirrorTree(root.right)
        root.left, root.right = root.right, root.left
        return root
