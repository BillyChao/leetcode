# -*- coding: utf-8 -*-

"""
@Time    : 2021/3/21 10:39 下午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder and not inorder:
            return None
        base = preorder[0]
        root = TreeNode(base)
        index = inorder.index(base)
        root.left = self.buildTree(preorder[1:index + 1], inorder[0:index])
        root.right = self.buildTree(preorder[index + 1:], inorder[index + 1:])
        return root


def preorder_fun(root: TreeNode):
    if not root:
        return
    print(root.val)
    if root.left:
        preorder_fun(root.left)
    if root.right:
        preorder_fun(root.right)


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
tree = Solution().buildTree(preorder, inorder)
preorder_fun(tree)
