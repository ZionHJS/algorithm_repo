import queue


class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        if not M or not M[0]:
            return 0
        m, n = len(M[0]), len(M)
        ans = 0
        self.direction_cnt = [
            [[0 for _ in range(8)] for j in range(m)] for i in range(n)]

        for i in range(n):
            for j in range(m):
                if M[i][j] == 1:
                    tmp_res = self.cnt_bfs(i, j, M)
                    ans = max(ans, tmp_res)

        return ans

    def cnt_bfs(self, y, x, M):
        cur_cnt, tmp_cnt = 1, 1
        visited = set()
        y_ = [-1, -1, -1, 0, 0, 1, 1, 1]
        x_ = [-1, 0, 1, -1, 1, -1, 0, 1]
        q = queue.Queue()
        for k in range(8):
            if self.is_valid(y+y_[k], x+x_[k], M):
                if not self.direction_cnt[y][x][k]:
                    if M[y+y_[k]][x+x_[k]] == M[y][x]:
                        q.put((y+y_[k], x+x_[k], k))
                        visited.add((y+y_[k], x+x_[k]))
                        self.direction_cnt[y][x][k] = 1
                else:
                    tmp_cnt = max(tmp_cnt, self.direction_cnt[y][x][k])
        while q.qsize():
            cur_cnt += 1
            n = q.qsize()
            for i in range(n):
                cur_node = q.get()
                #print("cur_node:", cur_node)
                self.direction_cnt[y][x][cur_node[2]] += 1
                if self.is_valid(cur_node[0]+y_[cur_node[2]], cur_node[1]+x_[cur_node[2]], M) and (cur_node[0]+y_[cur_node[2]], cur_node[1]+x_[cur_node[2]]) not in visited:
                    if not self.direction_cnt[cur_node[0]][cur_node[1]][cur_node[2]]:
                        if M[cur_node[0]+y_[cur_node[2]]][cur_node[1]+x_[cur_node[2]]] == M[y][x]:
                            q.put(
                                (cur_node[0]+y_[cur_node[2]], cur_node[1]+x_[cur_node[2]], cur_node[2]))
                            visited.add(
                                (cur_node[0]+y_[cur_node[2]], cur_node[1]+x_[cur_node[2]]))
                    else:
                        tmp_cnt = max(
                            tmp_cnt, cur_cnt-1+self.direction_cnt[cur_node[0]][cur_node[1]][cur_node[2]])
        return max(cur_cnt, tmp_cnt)

    def is_valid(self, y, x, M):
        return (y >= 0 and y < len(M)) and (x >= 0 and x < len(M[0]))
