class Solution:
    def trapRainWater(self, H: List[List[int]]) -> int:
        m, n = len(H[0]), len(H)
        W = [[0 for j in range(m)] for i in range(n)]
        ans = 0

        def dfs(y, x, visited):
            nonlocal W, H, m, n
            if (y == 0 or y == n-1) or (x == 0 or x == m-1) or (W[y][x] == -1):
                cur_min = min(cur_min, H[y][x])
                return False
            check = True
            for (nxy, nxx) in ((y-1, x), (y, x+1), (y+1, x), (y, x-1)):
                if (0 <= nxy < n) and (0 <= nxx < m) and H[y][x] >= H[nxy][nxx] and (nxy, nxx) not in visited:
                    visited.add((nxy, nxx))
                    if not dfs(nxy, nxx):
                        check = False
            return check

        # loop to mark
        for i in range(1, n-1):
            for j in range(1, m-1):
                if W[i][j] != -1:
                    visited = set([(i, j)])
                    cur_min = math.inf
                    if dfs(i, j, visited, cur_min):
                        for v in visited:
                            if H[v[0]][v[1]] <= H[i][j]:
                                W[v[0]][v[1]] = H[i][j]
                    else:
                        for v in visited:
                            if H[v[0]][v[1]] >= cur_min:
                                W[v[0]][v[1]] = -1

        # get res
        for i in range(1, n-1):
            for j in range(1, m-1):
                if W[i][j] != -1:
                    ans += W[i][j] - H[i][j]
        return ans
