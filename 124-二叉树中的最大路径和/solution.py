# -*- coding: utf-8 -*-

"""
@Time    : 2021/2/24 10:37 下午
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
    def maxPathSum(self, root: TreeNode) -> int:
        max_sum = float('-inf')

        def maxGain(node: TreeNode):
            nonlocal max_sum
            if not node:
                return 0
            left_gain = max(maxGain(node.left), 0)
            right_gain = max(maxGain(node.right), 0)
            new_path_sum = node.val + left_gain + right_gain
            max_sum = max(max_sum, new_path_sum)
            return node.val + max(left_gain, right_gain)

        maxGain(root)
        return max_sum

