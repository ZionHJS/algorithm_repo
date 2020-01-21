from collections import deque


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        res = []

        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                self.bfs(matrix, y, x)

        return max(res)

    # bfs instead of bfs
    def bfs(self, matrix, y, x):
        dq = deque([(matrix[y][x])])
        temp_res = []
        help_y = [0, 0, -1, 1]
        help_x = [-1, 1, 0, 0]

        while dq:
            cur = dq.popleft()

            for i in range(4):
                next_y = y + help_y[i]
                next_x = x + help_x[i]
                if self.is_valid(matrix, next_y, next_x):
                    temp_res.append(matrix[next_y][next_x])

    def dfs(self, matrix, y, x):
        help_y = [0, 0, -1, 1]
        help_x = [-1, 1, 0, 0]
        temp_res = []

        for i in range(4):
            next_y = y + help_y[i]
            next_x = x + help_x[i]
            if maxtrix[next_y][next_x] > matrix[y][x]:
                temp_res.append(matrix[next_y][next_x])
                self.dfs(matrix, next_y, next_x)
                temp_res.pop()
            else:

    def is_valid(self, matrix, y, x):
        y_, x_ = len(matrix), len(matrix[0])
        return 0 <= y < y_ and 0 <= x < x_
