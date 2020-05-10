class Solution:
    def minFlips(self, M: List[List[int]]) -> int:
        m, n = len(M[0]), len(M)
        if m == n == 1:
            return 1 if M[0][0] == 1 else 0
        nxt = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        memo = set()
        steps = 0
        ans = math.inf
        q = []
        cors = set()
        for i in range(n):
            for j in range(m):
                cors.add((i, j))
                if M[i][j] == 1:
                    q.append((i, j))
        Q = [tuple(q)]
        memo.add(tuple(q))
        while Q:
            steps += 1
            newQ = []
            for q in Q:
                for cor in cors:
                    nxt_q = []
                    for q_ in q:
                        nxt_q.append(q_)
                    if cor in nxt_q:
                        nxt_q.remove(cor)
                    else:
                        nxt_q.append(cor)
                    for k in range(4):
                        nyy, nxx = cor[0]+nxt[k][0], cor[1]+nxt[k][1]
                        if 0 <= nyy < n and 0 <= nxx < m:
                            if (nyy, nxx) not in nxt_q:
                                nxt_q.append((nyy, nxx))
                            else:
                                nxt_q.remove((nyy, nxx))
                    if not nxt_q:
                        return steps
                    nxt_q = tuple(nxt_q)
                    if nxt_q not in memo:
                        newQ.append(nxt_q)
                        memo.add(nxt_q)
            Q = newQ

        return -1
