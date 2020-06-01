class Solution:
    def knightDialer(self, N: int) -> int:
        ans = 0
        visited = set()
        # B => 3*4 -2

        def dfs(cur, cur_N, y, x, visited):
            if cur_N == N:
                ans += 1
                ans %= 10**9+7
                return
            for nxt in ((y-1, x-2), (y-2, x-1), (y-2, x+1), (y-1, x+2), (y+1, x+2), (y+2, x+1), (y+2, x-1), (y+1, x-2)):
                if 0 <= nxt[0] < 3 and 0 <= nxt[1] < 4 and nxt != ((3, 0) or (3, 2)):
                    if cur+str((nxt[0]*3+nxt[1]+1)) not in visited:
                        visited.add(cur+str((nxt[0]*3+nxt[1]+1)))
                        dfs(cur+str((nxt[0]*3+nxt[1]+1)),
                            cur_N+1, nxt[0], nxt[1], visited)

        for i in range(4):
            for j in range(3):
                dfs("", 0, i, j, visited)

        return ans
