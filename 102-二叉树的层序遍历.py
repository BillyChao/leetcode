# -*- coding: utf-8 -*-

"""
@Time    : 2020/7/10 下午5:41
@Author  : mc
@File    : 102-二叉树的层序遍历.py
@Software: PyCharm
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        # 利用栈结构
        result = []
        if not root:
            return result
        nodes = [root]
        while nodes:
            tmp = [item for item in nodes]
            nodes.clear()
            for node in tmp:
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            result.append(list(map(lambda x: x.val, tmp)))
        return result

    def levelOrder2(self, root: TreeNode):
        result = []
        if not root:
            return result
        nodes = [root]
        while nodes:
            _len = len(nodes)
            tmp = []
            for i in range(_len):
                tree_node = nodes.pop(0)
                tmp.append(tree_node.val)
                if tree_node.left:
                    nodes.append(tree_node.left)
                if tree_node.right:
                    nodes.append(tree_node.right)
            result.append(tmp)
            tmp.clear()
        return result
