class Solution:
    def orangesRotting(self, grid) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        count = 0
        count_0 = 0
        stack = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    stack.append((i, j))
        while stack:
            stack_len = len(stack)
            for _ in range(stack_len):
                pop = stack.pop(0)
                self.__bfs(grid, m, n, pop[0], pop[1], stack)
            count += 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
                elif grid[i][j] ==0:
                    count_0 += 1
        if count_0 == m*n:
            return 0
        return count-1

    def __bfs(self, grid, m, n, i, j, stack):
        for direcition in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_i = i + direcition[0]
            new_j = j + direcition[1]
            if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == 1:
                grid[new_i][new_j] = 2
                stack.append((new_i, new_j))


if __name__ == '__main__':
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    solution = Solution()
    oranges_rotting = solution.orangesRotting(grid)
    print(oranges_rotting)
