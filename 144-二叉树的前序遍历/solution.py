# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/26 6:54 下午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode):
        """
        递归实现
        :param root:
        :return:
        """
        res = []

        def preorder(root, res):
            if not root:
                return
            res.append(root.val)
            if root.left:
                preorder(root.left, res)
            if root.right:
                preorder(root.right, res)

        preorder(root, res)
        return res

    def preorderTraversal(self, root: TreeNode):
        """
        非递归实现
        :param root:
        :return:
        """
        res = []
        stack = []
        while stack or root:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        return res
