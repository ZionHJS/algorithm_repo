class Solution:
    def cherryPickup(self, G: List[List[int]]) -> int:
        if not len(G) or G[0][0] == -1:
            return 0
        elif len(G) == 1:
            return G[0][0]

        n = len(G)
        self.ans = 0
        memo = set()

        print("cnts:", cnts)

        def dfs(y, x, n, cur_sum, target, G, path, memo):  # O(2n * 2^2n) too much
            #print("y:", y, "x:", x, "cur_sum:", cur_sum)
            if target == (0, 0) and (y, x) == target:
                self.ans = max(self.ans, cur_sum)
                #print("cur_sum:", cur_sum, "ans:", self.ans)
                return

            nxt_target = target
            if target == (n-1, n-1) and (y, x) == target:
                nxt_target = (0, 0)

            if nxt_target == (n-1, n-1):
                nxts = ((y, x+1), (y+1, x))  # right | down
            else:
                nxts = ((y, x-1), (y-1, x))  # left | up

            for (nxy, nxx) in nxts:
                if 0 <= nxy < n and 0 <= nxx < n and G[nxy][nxx] != -1:
                    prev = G[nxy][nxx]
                    G[nxy][nxx] = 0
                    nxt_path = path
                    if prev != 0:
                        nxt_path += y
                        nxt_path += x
                    if (nxt_path, (y, x)) not in memo:
                        memo.add((nxt_path, (y, x)))
                        dfs(nxy, nxx, n, cur_sum+prev,
                            nxt_target, G, nxt_path, memo)
                    G[nxy][nxx] = prev

        start = G[0][0]
        G[0][0] = 0
        if start != 0:
            memo.add(("0"+"0", (0, 0)))
        dfs(0, 0, n, start, (n-1, n-1), G, path, memo)
        G[0][0] = start

        return self.ans
