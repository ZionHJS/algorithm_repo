import queue
import math


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        steps = -1
        q = queue.Queue()
        visited = set()
        ans = math.inf
        x_ = [-2, -1, 1, 2, 2, 1, -1, -2]
        y_ = [-1, -2, -2, -1, 1, 2, 2, 1]
        q.put((0, 0))
        visited.add((0, 0))
        while q.qsize():
            steps += 1
            n = q.qsize()
            for i in range(n):
                cur = q.get()
                if (cur[0], cur[1]) == (x, y):
                    ans = min(ans, steps)
                    return ans
                xs, ys = abs(x-cur[0]), abs(y-cur[1])
                if xs == 1 and ys == 1:
                    ans = min(ans, steps+2)
                elif xs <= 1 and ys <= 1:
                    ans = min(ans, steps+3)
                for j in range(8):
                    nxt_x, nxt_y = cur[0]+x_[j], cur[1]+y_[j]
                    nxs, nys = abs(x-nxt_x), abs(y-nxt_y)
                    if (nxs <= xs or nys <= ys) and (nxt_x, nxt_y) not in visited:
                        q.put((nxt_x, nxt_y))
                        visited.add((nxt_x, nxt_y))
