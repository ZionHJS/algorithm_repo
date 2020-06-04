class Solution:
    def trapRainWater(self, H: List[List[int]]) -> int:
        m, n = len(H[0]), len(H)
        W = [[0 for j in range(m)] for i in range(n)]
        ans = 0

        def dfs(y, x, cur_h, visited, min_edge):
            nonlocal W, H, m, n
            for (nxy, nxx) in ((y-1, x), (y, x+1), (y+1, x), (y, x-1)):
                if (0 <= nxy < n) and (0 <= nxx < m):
                    if cur_h >= H[nxy][nxx]:
                        if (nxy, nxx) not in visited:
                            visited.add((nxy, nxx))
                            if W[nxy][nxx] != -1:
                                min_edge = min(min_edge, dfs(
                                    nxy, nxx, cur_h, visited, min_edge))
                            elif W[nxy][nxx] == -1:
                                min_edge = 0
                    else:
                        min_edge = min(min_edge, H[nxy][nxx])
            return min_edge

        # loop to mark
        for i in range(n):
            for j in range(m):
                if(i == 0 or i == n-1) or (j == 0 or j == m-1):
                    W[i][j] = -1
                if W[i][j] == 0:
                    visited = set([(i, j)])
                    min_edge = dfs(i, j, H[i][j], visited, math.inf)
                    print("min_edge:", min_edge)
                    if not min_edge:
                        print("visited:", visited)
                        for v in visited:
                            if H[v[0]][v[1]] >= H[i][j]:
                                W[v[0]][v[1]] = -1
                    else:
                        print("visited:", visited)
                        for v in visited:
                            ans += min_edge-H[v[0]][v[1]]
                            H[v[0]][v[1]] = min_edge
        return ans
