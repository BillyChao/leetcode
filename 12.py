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
        输入：root = [4,2,7,1,3,6,9]
        输出：[4,7,2,9,6,3,1]
        思路：
        利用递归的思路，先遍历左子树，再遍历右子树，最后交换左右子树的值
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
