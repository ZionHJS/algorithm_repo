import queue
import math


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        self.res = math.inf
        if not grid or not grid[0]:
            return -1
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    cnt += 1
        n, m = len(grid), len(grid[0])

        # bfs
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    tmp_res = self.bfs(i, j, m, n, grid, cnt)
                    if tmp_res:
                        self.res = min(self.res, self.bfs(
                            i, j, m, n, grid, cnt))

        if self.res != math.inf:
            return self.res
        else:
            return -1

    def bfs(self, i, j, m, n, grid, cnt):
        y_ = [0, 0, 1, -1]
        x_ = [1, -1, 0, 0]
        q = queue.Queue()
        visited = set()
        q.put((i, j))
        visited.add((i, j))
        cur_steps_cnt = 0
        cur_cnt = 0
        steps = -1
        while q.qsize():
            steps += 1
            k = q.qsize()
            for o in range(k):
                cur = q.get()
                if grid[cur[0]][cur[1]] == 1:
                    cur_steps_cnt += steps
                    if cur_steps_cnt >= self.res:
                        return self.res
                    cur_cnt += 1
                    continue
                for l in range(4):
                    if 0 <= cur[0]+y_[l] < n and 0 <= cur[1]+x_[l] < m:
                        if (cur[0]+y_[l], cur[1]+x_[l]) not in visited:
                            if grid[cur[0]+y_[l]][cur[1]+x_[l]] == 0 or grid[cur[0]+y_[l]][cur[1]+x_[l]] == 1:
                                q.put((cur[0]+y_[l], cur[1]+x_[l]))
                                visited.add((cur[0]+y_[l], cur[1]+x_[l]))
            if cur_cnt == cnt:
                return cur_steps_cnt
        return 0
