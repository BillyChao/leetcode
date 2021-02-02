# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __int__(self):
        self.result = []
        self.array = []

    def pathSum(self, root: TreeNode, sum: int):
        """
        描述：输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径
        思路：先序遍历
        每次访问一个节点，那么就将当前权值求和
        如果当前权值和与期待的和一致，那么说明我们找到了一个路径，保存或者输出
        每次深度遍历到底部，回退一个点
        :param root:
        :param sum:
        :return:
        """
        if not root: return []
        self.array.append(root.val)
        sum -= root.val
        if sum == 0 and not root.left and root.right:
            # self.array[:]这里要用深拷贝
            self.result.append(self.array[:])
        self.pathSum(root.left, sum)
        self.pathSum(root.right, sum)
        self.array.pop()
        return self.result

    def pathSum_20210201(self, root: TreeNode, expectNumber: int):
        if not root:
            return []
        self.array.append(root.val)
        expectNumber -= root.val
        if expectNumber == 0 and not root.left and not root.right:
            self.result.append(self.array[:])
        self.pathSum(root.left, expectNumber)
        self.pathSum(root.right, expectNumber)
        self.array.pop()
        return self.result
