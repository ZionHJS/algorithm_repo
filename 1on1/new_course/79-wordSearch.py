# bfs() not working
import queue


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board[0]), len(board)
        sw = set(word)
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if self.check(i, j, board, word, m, n):
                        return True
        return False

    def check(self, i, j, board, word, m, n):
        x_ = [0, 0, -1, 1]
        y_ = [-1, 1, 0, 0]
        visited = set()
        idx = 1
        q = queue.Queue()
        q.put((i, j))
        while q.qsize() and idx < len(word):
            #idx += 1
            l = q.qsize()
            check = False
            for k in range(l):
                x, y = q.get()
                visited.add((x, y))
                for o in range(4):
                    nxt_x = x+x_[o]
                    nxt_y = y+y_[o]
                    if (nxt_x, nxt_y) not in visited and self.is_valid(nxt_x, nxt_y, m, n) and board[nxt_x][nxt_y] == word[idx]:
                        check = True
                        q.put((nxt_x, nxt_y))
            if check:
                idx += 1
        return idx == len(word)

    def is_valid(self, x, y, m, n):
        return 0 <= x < n and 0 <= y < m
