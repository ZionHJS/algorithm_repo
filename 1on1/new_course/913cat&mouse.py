class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        memo = {}
        points = set()
        for edge in graph:
            points = set.union(points, set(edge))
        print("points:", points)

        def dfs(midx, cidx, mvisited, cvisited, T):  # T => mouse / not T => cat
            if T:
                mvisited.add(midx)
                if (midx, cidx, tuple(mvisited), tuple(cvisited), T) in memo:
                    return memo[(midx, cidx, tuple(mvisited), tuple(cvisited), T)]
                elif len(mvisited)+len(cvisited) == len(points):
                    return 1 if len(mvisited) > len(cvisited) else -1 if len(mvisited) < len(cvisited) else 0
                mtmp = -math.inf
                for nidx in graph[midx]:
                    if nidx == 0:
                        return 1
                    if nidx not in mvisited and cvisited:
                        nxt_res = dfs(nidx, cidx, mvisited, cvisited, False)
                        nxt_res = 1 if nxt_res == -1 else -1 if nxt_res == 1 else 0
                        mtmp = max(mtmp, nxt_res)  # -1 loose / 0 draw / 1 win
                memo[(midx, cidx, tuple(mvisited), tuple(cvisited), T)
                     ] = mtmp if mtmp != -math.inf else 0
                return mtmp if mtmp != -math.inf else 0
            else:
                cvisited.add(cidx)
                if (midx, cidx, tuple(mvisited), tuple(cvisited), T) in memo:
                    return memo[(midx, cidx, tuple(mvisited), tuple(cvisited), T)]
                elif len(mvisited)+len(cvisited) == len(points):
                    return 1 if len(cvisited) > len(mvisited) else -1 if len(cvisited) < len(mvisited) else 0
                ctmp = -math.inf
                for nidx in graph[cidx]:
                    if nidx not in cvisited and mvisited and nidx != 0:
                        nxt_res = dfs(midx, nidx, mvisited, cvisited, True)
                        nxt_res = 1 if nxt_res == -1 else -1 if nxt_res == 1 else 0
                        ctmp = max(ctmp, nxt_res)  # -1 loose / 0 draw / 1 win
                memo[(midx, cidx, tuple(mvisited), tuple(cvisited))
                     ] = ctmp if ctmp != -math.inf else 0
                return ctmp if ctmp != -math.inf else 0

        res = dfs(1, 2, set(), set(), True)
        return 1 if res == 1 else 2 if res == -1 else 0
