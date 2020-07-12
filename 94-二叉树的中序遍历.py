# -*- coding: utf-8 -*-

"""
@Time    : 2020/7/12 上午11:33
@Author  : mc
@File    : 94-二叉树的中序遍历.py
@Software: PyCharm
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        # 递归版本
        result = []
        if root:
            self.inorderUtil(root, result)
        return result

    def inorderUtil(self, root: TreeNode, result: list[int]):
        # 利用递归实现
        if root.left:
            self.inorderUtil(root.left, result)
        result.append(root.val)
        if root.right:
            self.inorderUtil(root.right, result)

    def inorderTraversal2(self, root: TreeNode) -> list[int]:
        # 非递归版本,将左节点全部入栈，之后逐个出栈
        result = []
        nodes = []
        curr = root
        while curr or nodes:
            while curr:
                nodes.insert(0, curr)
                curr = curr.left
            _pop = nodes.pop(0)
            result.append(_pop.val)
            # 右节点的处理方式与root类似
            curr = _pop.right
        return result
