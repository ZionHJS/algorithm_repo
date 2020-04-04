import queue


class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        m, n = len(M[0]), len(M)
        ans = 0
        self.direction_cnt = [
            [[-1 for _ in range(8)] for j in range(m)] for i in range(n)]

        for i in range(n):
            for j in range(m):
                ans = max(ans, self.cnt_bfs(i, j, M))

        return ans

    def cnt_bfs(self, y, x, M):
        cur_cnt, tmp_cnt = 1, 1
        y_ = [-1, -1, -1, 0, 0, 1, 1, 1]
        x_ = [-1, 0, 1, -1, 1, -1, 0, 1]
        q = queue.Queue()
        for k in range(8):
            if not self.direction_cnt[y][x][k]:
                if self.is_valid(y, x, M) and M[y+y_[k]][x+x_[k]] == M[y][x]:
                    q.put((y+y_[k], x+x_[k], k))
                    self.direction_cnt[y][x][k] = 1
            else:
                tmp_cnt = max(tmp_cnt, self.direction_cnt[y][x][k])
        while q.qsize():
            cur_cnt += 1
            n = q.qsize()
            for i in range(n):
                cur_node = q.get()
                self.direction_cnt[y][x][cur_node[2]] += 1
                for k in range(8):
                    if not self.direction_cnt[cur_node[0]][cur_node[1]][k]:
                        if self.is_valid(cur_node[0], cur_node[1], M) and M[cur_node[0]+y_[k]][cur_node[1]+x_[k]] == M[y][k]:
                            q.put((cur_node[0]+y_[k], cur_node[1]+x_[k], k))
                    else:
                        tmp_cnt = max(
                            tmp_cnt, cur_cnt-1+self.direction_cnt[cur_node[0]][cur_node[1]][k])
        return max(cur_cnt, tmp_cnt)

    def is_valid(self, y, x, M):
        return (y >= 0 and y < len(M)) and (x >= 0 and x < len(M[0]))
