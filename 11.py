# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        给定一个二叉树，判断它是否是高度平衡的二叉树
        思路：
        用递归方式实现，从底向上计算
        检查子树是否平衡。如果平衡，则使用它们的高度判断父节点是否平衡，并计算父节点的高度，子树不平衡直接返回false结束
        :type root: TreeNode
        :rtype: bool
        """
        return self.isBalancedHelper(root)[0]

    def isBalancedHelper(self, root: TreeNode) -> (bool, int):
        # An empty tree is balanced and has height -1
        if not root:
            return True, -1

        # Check subtrees to see if they are balanced.
        leftIsBalanced, leftHeight = self.isBalancedHelper(root.left)
        if not leftIsBalanced:
            return False, 0
        rightIsBalanced, rightHeight = self.isBalancedHelper(root.right)
        if not rightIsBalanced:
            return False, 0

        # If the subtrees are balanced, check if the current tree is balanced
        # using their height
        return (abs(leftHeight - rightHeight) < 2), 1 + max(leftHeight, rightHeight)
