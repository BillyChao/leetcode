# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/24 3:08 下午
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
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        存储所有的父节点信息，root的父节点None，之后从p开始查找一直到根节点，并记录途中的所有节点
        从q 开始查找父节点一直到跟，期间遇到p途中的节点，为最近公共祖先，返回
        :param root:
        :param p:
        :param q:
        :return:
        """
        parent = {root.val: None}

        def dfs(root: TreeNode):
            if root.left:
                parent[root.left.val] = root
                dfs(root.left)
            if root.right:
                parent[root.right.val] = root
                dfs(root.right)

        dfs(root)
        ss = dict()
        while p:
            ss[p.val] = True
            # p跳转到父节点
            p = parent[p.val]
        while q:
            if q.val in ss:
                return q
            # q跳转到父节点
            q = parent[q.val]


if __name__ == '__main__':
    root = TreeNode(10)
    left = TreeNode(1)
    root.left = left
    right = TreeNode(2)
    root.right = right
    left1 = TreeNode(3)
    left.left = left1
    right1 = TreeNode(4)
    left.right = right1
    print(Solution().lowestCommonAncestor(root=root, p=left1, q=right))
