class Solution:
    def trapRainWater(self, H: List[List[int]]) -> int:
        m, n = len(H[0]), len(H)
        W = [[0 for j in range(m)] for i in range(n)]
        ans = 0

        def dfs(y, x, cur_h, visited):
            nonlocal W, H, m, n
            if W[y][x] == -1:
                return False
            check = True
            for (nxy, nxx) in ((y-1, x), (y, x+1), (y+1, x), (y, x-1)):
                if (0 <= nxy < n) and (0 <= nxx < m) and cur_h >= H[nxy][nxx] and (nxy, nxx) not in visited:
                    visited.add((nxy, nxx))
                    if not dfs(nxy, nxx, cur_h, visited):
                        check = False
            return check

        # loop to mark
        for i in range(n):
            for j in range(m):
                if(i == 0 or i == n-1) or (j == 0 or j == m-1):
                    W[i][j] = -1
                if W[i][j] != -1:
                    visited = set([(i, j)])
                    if not dfs(i, j, H[i][j], visited):
                        for v in visited:
                            if H[v[0]][v[1]] >= H[i][j]:
                                W[v[0]][v[1]] = -1
        for w in W:
            print(w)
        # get res
        for i in range(1, n-1):
            print("i:", i)
            for j in range(1, m-1):
                print("j:", j)
                if W[i][j] == 0:
                    print("find_pool!", "i:", i, "j:", j)
                    q = [(i, j)]
                    visited = set([(i, j)])
                    min_edge = math.inf
                    while q:
                        nxt_q = []
                        for i in range(len(q)):
                            for (nxy, nxx) in ((q[i][0]-1, q[i][1]), (q[i][0], q[i][1]+1), (q[i][0]+1, q[i][1]), (q[i][0], q[i][1]+1)):
                                if 0 <= nxy < n and 0 <= nxx < m:
                                    if W[nxy][nxx] == 0 and (nxy, nxx) not in visited:
                                        visited.add((nxy, nxx))
                                        nxt_q.append((nxy, nxx))
                                    elif W[nxy][nxx] == -1:
                                        min_edge = min(min_edge, H[nxy][nxx])
                        q = nxt_q
                    print("visited:", visited, "min_edge:", min_edge)
                    for v in visited:
                        W[v[0]][v[1]] = -1
                        ans += min_edge-H[v[0]][v[1]]
        for w in W:
            print(w)
        return ans
