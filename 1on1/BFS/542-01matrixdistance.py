import queue
from collections import deque


class Solution:
    def __init__(self):
        self.new_matrix = []

    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []

        x = len(matrix[0])
        y = len(matrix)

        self.new_matrix = [[] for _ in range(y)]
        for i in range(y):
            self.new_matrix[i] = [0 for _ in range(x)]

        # print(self.new_matrix)   #works here

        for i in range(y):
            for j in range(x):
                if matrix[i][j] == 0:
                    continue
                else:
                    self.new_matrix[i][j] = self.diszero(
                        matrix, i, j)  # i=>y / j=>x

        return self.new_matrix

    def diszero(self, matrix, y, x):
        min_dis = 0
        dis = 0
        dequeue = deque([(y, x)])  # dequeue => [(y,x), (y,x)...]
        help_y = [0, 0, 1, -1]
        help_x = [-1, 1, 0, 0]

        # bfs
        while dequeue:
            len_dequeue = len(dequeue)
            dis += 1
            for k in range(len_dequeue):
                y, x = dequeue.popleft()
                for i in range(4):
                    next_y = y + help_y[i]
                    next_x = x + help_x[i]

                    if self.is_valid(matrix, next_y, next_x):
                        if matrix[next_y][next_x] == 0:
                            return dis  # return => return to the outside of while
                        else:
                            dequeue.append((next_y, next_x))
                    else:
                        continue

    def is_valid(self, matrix, y, x):
        m, n = len(matrix), len(matrix[0])
        return 0 <= y < m and 0 <= x < n
