class Solution:
    def getMaximumGold(self, G: List[List[int]]) -> int:
        if not G or not G[0]:
            return 0
        n, m = len(G), len(G[0])
        visited = set()
        nxt = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(cur, i, j):
            cur += G[i][j]
            for o in range(4):
                nxy, nxx = i+nxt[o][0], j+nxt[o][1]
                if 0 <= nxy < n and 0 <= nxx < m and G[nxy][nxx] != 0 and (nxx, nxy) not in visited:
                    visited.add(nxx, nxy)
                    cur = max(cur, dfs(cur, nxy, nxx))
            return cur

        ans = 0
        for i in range(n):
            for j in range(m):
                if G[i][j] not in visited:
                    ans = max(ans, dfs(0, i, j))
        return ans
