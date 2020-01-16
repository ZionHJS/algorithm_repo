from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.bfs(grid, i, j)
                    islands += 1
        return islands

    def bfs(self, grid, x, y):
        dqueue = deque([(x, y)])
        grid[x][y] = '0'
        dx = [0, 0, 1, -1]  # helper_x
        dy = [1, -1, 0, 0]  # helper_y
        while dqueue:
            x, y = dqueue.popleft()

            for i in range(4):  # get the up down left right next_point
                next_x = x + dx[i]
                next_y = y + dy[i]
                if not self.is_valid(grid, next_x, next_y):
                    continue
                dqueue.append((next_x, next_y))
                grid[next_x][next_y] = '0'

    def is_valid(self, grid, x, y):
        n, m = len(grid), len(grid[0])
        return 0 <= x < n and 0 <= y < m and grid[x][y] == '1'


d = deque([(1, 2), (3, 4)])
print(d)

print "length:", len(d)
print "left end:", d[0]
print "right end:", d[-1]

d.remove('b')
print d
