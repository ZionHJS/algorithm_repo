class Solution:
    def knightDialer(self, N: int) -> int:
        ans = 0
        visited = set()
        # B => 3*4 -2

        def dfs(cur, cur_N, y, x, visited):
            nonlocal ans, N
            if cur_N == N:
                if tuple((cur, y, x)) not in visited:
                    ans += 1
                    ans %= 10**9+7
                    visited.add(tuple((cur, y, x)))
                return
            for nxt in ((y-1, x-2), (y-2, x-1), (y-2, x+1), (y-1, x+2), (y+1, x+2), (y+2, x+1), (y+2, x-1), (y+1, x-2)):
                if 0 <= nxt[0] < 4 and 0 <= nxt[1] < 3 and nxt != (3, 0) and nxt != (3, 2):
                    if tuple((cur, nxt[0], nxt[1])) not in visited:
                        visited.add(tuple((cur, nxt[0], nxt[1])))
                        dfs(cur+str((nxt[0]*3+nxt[1]+1)),
                            cur_N+1, nxt[0], nxt[1], visited)

        for i in range(4):
            for j in range(3):
                if (i, j) != (3, 0) and (i, j) != (3, 2):
                    dfs(str(i*3+j+1), 1, i, j, visited)

        return ans
