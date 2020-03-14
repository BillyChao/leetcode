# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        """
        特例处理： 当树的根节点为空，则直接返回空列表 [] ；
        初始化： 打印结果列表 res = [] ，包含根节点的队列 queue = [root] ；
        BFS 循环： 当队列 queue 为空时跳出；
        新建一个临时列表 tmp ，用于存储当前层打印结果；
        当前层打印循环： 循环次数为队列 queue 长度（队列中元素为所有当前层节点）；
        出队： 队首元素出队，记为 node；
        打印： 将 node.val 添加至列表 tmp 尾部；
        添加子节点： 若 node 的左（右）子节点不为空，则将左（右）子节点加入队列 queue ；
        偶数层倒序： 若 res 的长度为 奇数 ，说明当前是偶数层，则对 tmp 执行 倒序 操作。
        将当前层结果 tmp 添加入 res 。
        返回值： 返回打印结果列表 res 即可。
        :param root:
        :return:
        """
        if not root:
            return []
        res, queue_l, queue_r = [], [root], []
        while queue_l or queue_r:
            temp = []
            while queue_l:
                pop = queue_l.pop()
                temp.append(pop.val)
                if pop.left: queue_r.append(pop.left)
                if pop.right: queue_r.append(pop.right)
            if temp:
                res.append(temp)
                continue
            while queue_r:
                pop = queue_r.pop()
                temp.append(pop.val)
                if pop.right: queue_l.append(pop.right)
                if pop.left: queue_l.append(pop.left)
            if temp:
                res.append(temp)
                continue
        return res
