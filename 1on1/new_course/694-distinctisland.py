import queue
import math


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        if n == 0 or m == 0:
            return 0

        res_str = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    res_str.append(self.record_is(i, j, grid, n, m))
        s = set()
        for island in res_str:
            s.add(island)
        return len(s)

    def record_is(self, y, x, grid, n, m):
        q = queue.Queue()
        q.put([y, x])
        x_ = [0, 0, -1, 1]
        y_ = [-1, 1, 0, 0]
        x_min, x_max, y_min, y_max = x, x, y, y
        while q.qsize():
            cur = q.get()
            grid[cur[0]][cur[1]] = 3
            x_min = min(x_min, cur[1])
            x_max = max(x_max, cur[1])
            y_min = min(y_min, cur[0])
            y_max = max(y_max, cur[0])
            for i in range(4):
                if self.is_valid(cur[0]+y_[i], cur[1]+x_[i], n, m, grid):
                    q.put([cur[0]+y_[i], cur[1]+x_[i]])
        str_is = ""
        for i in range(y_min, y_max+1):
            for j in range(x_min, x_max+1):
                if grid[i][j] == 3:
                    str_is += str(grid[i][j])
                else:
                    str_is += "0"
            str_is += "/"

        return str_is

    def is_valid(self, y, x, n, m, grid):
        return (y >= 0 and y < n) and (x >= 0 and x < m) and (grid[y][x] == 1)


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        visited = set()

        def dfs(i, j, direction=""):
            if 0 <= i < m and 0 <= j < n and grid[i][j] and (i, j) not in visited:
                visited.add((i, j))
                self.shape += direction
                # print(self.shape)
                dfs(i+1, j, "0")
                dfs(i-1, j, "1")
                dfs(i, j+1, "2")
                dfs(i, j-1, "3")
                self.shape += "/"  # when we are doing backtrack we must record it

        shapes = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (i, j) not in visited:
                    self.shape = ""
                    dfs(i, j)
                    shapes.add(self.shape)

        return len(shapes)
