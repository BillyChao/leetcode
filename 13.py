import queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:

    def levelOrder(self, root: TreeNode):
        """
        从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
        思路：
        利用queue队列的性质，先进先出
        queue中存放节点，取出节点后，将二叉树中节点对应的值append到列表中
        :param root:
        :return:
        """
        if not root: return []
        res, queue = [], [root]
        while queue:
            tree_node = queue.pop(0)
            res.append(tree_node.val)
            if tree_node.left: queue.append(tree_node.left)
            if tree_node.right: queue.append(tree_node.right)
        return res


if __name__ == '__main__':
    node7 = TreeNode(4)
    node15 = TreeNode(5)
    node9 = TreeNode(2, node7, node15)
    node20 = TreeNode(3)
    root = TreeNode(1, node9, node20)
    level_order = Solution().levelOrder(root=root)
    print('result: ', level_order)
