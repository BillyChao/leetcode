# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
        tree_map = {}
        result = []
        self.treeUtil(root, 0, 0, tree_map)
        flag = -10000
        tmp = []
        for x, y in sorted(tree_map.keys()):
            if x != flag:
                result.append(tmp)
                tmp = []
                flag = x
            tmp.extend(sorted(item for item in tree_map[(x, y)]))
        result.pop(0)
        result.append(tmp)
        return result

    def treeUtil(self, node: TreeNode, x, y, tree_map):
        if not node:
            return
        self.treeUtil(node.left, x - 1, y + 1, tree_map)
        self.treeUtil(node.right, x + 1, y + 1, tree_map)
        if tree_map.get((x, y)):
            tree_map.get((x, y)).append(node.val)
        else:
            tree_map[(x, y)] = [node.val]


if __name__ == '__main__':
    root = TreeNode(3)
    left = TreeNode(9)
    right = TreeNode(20)
    root.left = left
    root.right = right
    solution = Solution()
    traversal = solution.verticalTraversal(root=root)
    print(traversal)
