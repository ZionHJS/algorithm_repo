class Solution:
    def pacificAtlantic(self, M: List[List[int]]) -> List[List[int]]:
        if not M or not M[0]:
            return []
        m, n = len(M[0]), len(M)
        G = defaultdict(lambda: set())
        pq = []
        aq = []
        visited_p, visited_a = set(), set()
        for i in range(n):
            pq.append([i, 0])
            visited_p.add((i, 0))
            aq.append([i, m-1])
            visited_a.add((i, m-1))
        for j in range(m):
            pq.append([0, j])
            visited_p.add((0, j))
            aq.append([n-1, j])
            visited_a.add((n-1, j))
        # res
        res = set()
        # bfs()
        while pq or aq:
            new_pq, new_aq = [], []
            while pq:
                [y, x] = pq.pop()
                G[(y, x)].add("P")
                if len(G[(y, x)]) == 2:
                    res.add((y, x))
                for (nxy, nxx) in ((y-1, x), (y+1, x), (y, x-1), (y, x+1)):
                    if 0 <= nxy < n and 0 <= nxx < m and (nxy, nxx) not in visited_p and M[nxy][nxx] >= M[y][x]:
                        visited_p.add((nxy, nxx))
                        new_pq.append([nxy, nxx])
            while aq:
                [y, x] = aq.pop()
                G[(y, x)].add("A")
                if len(G[(y, x)]) == 2:
                    res.add((y, x))
                for (nxy, nxx) in ((y-1, x), (y+1, x), (y, x-1), (y, x+1)):
                    if 0 <= nxy < n and 0 <= nxx < m and (nxy, nxx) not in visited_a and M[nxy][nxx] >= M[y][x]:
                        visited_a.add((nxy, nxx))
                        new_aq.append([nxy, nxx])
            pq = new_pq
            aq = new_aq

        return res
