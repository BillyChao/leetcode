# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        给定一个二叉树，判断其是否是一个有效的二叉搜索树。
        假设一个二叉搜索树具有如下特征：
            ①节点的左子树只包含小于当前节点的数。
            ②节点的右子树只包含大于当前节点的数。
            ③所有左子树和右子树自身必须也是二叉搜索树。
        思路：
        不仅右子结点要大于该节点，整个右子树的元素都应该大于该节点，这意味着我们需要在遍历树的同时保留结点的上界与下界，
        在比较时不仅比较子结点的值，也要与上下界比较
        :param root:
        :return:
        """

        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False
            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True
        return helper(root)
