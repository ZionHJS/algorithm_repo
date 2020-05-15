class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        memo = {}
        points = set()
        for edge in graph:
            points = set.union(points, set(edge))
        #print("points:", points)

        def dfs(midx, cidx, mvisited, cvisited, T):  # T => mouse / not T => cat
            if (midx, cidx, tuple(mvisited), tuple(cvisited), T) in memo:
                return memo[(midx, cidx, tuple(mvisited), tuple(cvisited), T)]
            elif len(mvisited)+len(cvisited) == len(points):
                if T:
                    return 1 if len(mvisited) > len(cvisited) else -1 if len(mvisited) <= len(cvisited) else 0
                else:
                    return 1 if len(mvisited) <= len(cvisited) else -1 if len(mvisited) > len(cvisited) else 0

            cur_res = -math.inf
            cur_idx = midx if T else cidx
            print("cur_idx:", cur_idx, "T:", T)
            for nidx in graph[cur_idx]:
                if nidx == 0 and T:
                    print("M won!", "cur_idx:", cur_idx, "return!")
                    return 1
                if nidx not in mvisited and nidx not in cvisited and nidx != 0:
                    print("next-step:", nidx, "T:", T)
                    mvisited.add(nidx) if T else cvisited.add(nidx)
                    nxt_res = dfs(nidx, cidx, mvisited, cvisited, False) if T else dfs(
                        midx, nidx, mvisited, cvisited, True)
                    nxt_res = 1 if nxt_res == -1 else -1 if nxt_res == 1 else 0  # cal current
                    # -1 loose / 0 draw / 1 win
                    cur_res = max(cur_res, nxt_res)
                    mvisited.discard(nidx) if T else cvisited.discard(nidx)
            if cur_res == -math.inf:
                print("Draw!", "Return!")

            memo[(midx, cidx, tuple(mvisited), tuple(cvisited), T)
                 ] = cur_res if cur_res != -math.inf else 0
            return cur_res if cur_res != -math.inf else 0

        res = dfs(1, 2, set([1]), set([2]), True)
        return 1 if res == 1 else 2 if res == -1 else 0
