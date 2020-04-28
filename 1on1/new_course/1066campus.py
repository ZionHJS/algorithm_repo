class Solution:
    def assignBikes(self, W: List[List[int]], B: List[List[int]]) -> int:
        dis = math.inf
        visited = set()

        def dfs(idx_w, W, B, cur_dis, cur_visited):
            nonlocal dis
            if cur_dis > dis:
                return
            #print("idx_w:", idx_w, "len_visited:", len(cur_visited))
            # if len(cur_visited) == len(B):
            if idx_w == len(W):
                dis = min(dis, cur_dis)
                return

            for i in range(len(B)):
                if i not in cur_visited:
                    new_dis = abs(W[idx_w][0]-B[i][0])+abs(W[idx_w][1]-B[i][1])
                    cur_visited.add(i)
                    dfs(idx_w+1, W, B, cur_dis+new_dis, cur_visited)
                    cur_visited.remove(i)
        dfs(0, W, B, 0, visited)

        return dis
