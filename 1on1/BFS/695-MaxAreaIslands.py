import queue
from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        area_res = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.bfs(grid, i, j, area_res)

        if area_res:
            return max(area_res)
        else:
            return 0

    def bfs(self, grid, y, x, area_res):
        dq = deque([(y, x)])
        help_y = [0, 0, -1, 1]
        help_x = [-1, 1, 0, 0]
        grid[y][x] = 0
        temp_area = 1

        while dq:
            y, x = dq.popleft()

            for i in range(4):
                next_y = y + help_y[i]
                next_x = x + help_x[i]
                if not self.is_valid(grid, next_y, next_x):
                    continue
                else:
                    temp_area += 1
                    dq.append((next_y, next_x))
                    grid[next_y][next_x] = 0

        area_res.append(temp_area)
        print('res_area_list:', area_res)

    def is_valid(self, grid, y, x):
        y_, x_ = len(grid), len(grid[0])
        return 0 <= y < y_ and 0 <= x < x_ and grid[y][x] == 1
