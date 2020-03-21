class Solution:
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        marked = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i not in [0, m - 1] and j not in [0, n - 1] and board[i][j] == 'o' and marked[i][j] is False:
                    pos_set = set()
                    self.__helper(board, i, j, m, n, pos_set, marked)
                    l = list(filter(lambda x: x[0] in [0, m - 1] or x[1] in [0, n - 1], pos_set))
                    for k, h in pos_set:
                        if l:
                            marked[k][h] = True
                        else:
                            board[k][h] = 'x'
        print(board)

    def __helper(self, board, i, j, m, n, pos_set, marked):
        marked[i][j] = True
        pos_set.add((i, j))
        for direction in self.directions:
            new_i = i + direction[0]
            new_j = j + direction[1]
            if 0 <= new_i < m and 0 <= new_j < n and board[new_i][new_j] == 'o' and not marked[new_i][new_j]:
                self.__helper(board, new_i, new_j, m, n, pos_set, marked)


if __name__ == '__main__':
    grid = [['x', 'x', 'x', 'x'],
            ['x', 'o', 'o', 'x'],
            ['x', 'x', 'o', 'x'],
            ['x', 'o', 'x', 'x']]
    solution = Solution()
    solution.solve(grid)
