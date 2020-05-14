class Solution:
    def hitBricks(self, G: List[List[int]], H: List[List[int]]) -> List[int]:
        m, n = len(G[0]), len(G)
        # build edges could be better?
        nxt = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        edges = defaultdict(lambda: set())
        for i in range(n):  # O(n^2)
            for j in range(m):
                if G[i][j]:
                    for k in range(4):
                        nxy, nxx = i+nxt[k][0], j+nxt[k][1]
                        if (0 <= nxy < n and 0 <= nxx < m) and G[nxy][nxx]:
                            edges[(i, j)].add((nxy, nxx))
                            edges[(nxy, nxx)].add((i, j))
        #print("edges:", edges)

        # edit brunch
        def change(b):  # b => (y, x)
            nonlocal m, n, G, edges
            q = [b]
            visited = set()
            while q:
                new_q = []
                for i in range(len(q)):
                    cur = q.pop()
                    visited.add(cur)
                    for ngb in edges[cur]:
                        if G[ngb[0]][ngb[1]]:
                            if ngb[0] == 0:
                                return None
                            elif ngb not in visited:
                                new_q.append(ngb)
                q = new_q

            return visited

        # get result
        res = []
        for h in H:  # O(N)
            if G[h[0]][h[1]]:
                G[h[0]][h[1]] = 0
                cnt = 0
                for ngb in edges[(h[0], h[1])]:  # O(4)
                    if G[ngb[0]][ngb[1]]:
                        if ngb[0] == 0:
                            continue
                        tmp = change(ngb)  # O(N^2)
                        #print("tmp:", tmp)
                        if tmp:
                            cnt += len(tmp)
                            for b in tmp:
                                G[b[0]][b[1]] = 0
                                del edges[b]
                del edges[(h[0], h[1])]
                res.append(cnt)

        return res
