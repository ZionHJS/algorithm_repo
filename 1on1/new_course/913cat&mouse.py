class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        def dfs(midx, cidx, prevm, prevc, T, path):  # T => mouse / not T => cat
            if (midx, cidx, T) in path:
                print("repeat!")
                return 0
            path.add((midx, cidx, T))

            cur_res = -1
            cur_idx = midx if T else cidx
            print("cur_idx:", cur_idx, "T:", T)
            for nidx in graph[cur_idx]:
                if (nidx == midx and not T) or (nidx == 0 and T):
                    path.discard((midx, cidx, T))
                    return 1
                if nidx != ((prevm or cidx) if T else prevc) and nidx != 0:
                    print("nxt:", nidx, "prevm:", prevm, "prevc:", prevc)
                    nxt_res = dfs(nidx, cidx, midx, prevc, False, path) if T else dfs(
                        midx, nidx, prevm, cidx, True, path)
                    nxt_res = 1 if nxt_res == -1 else -1 if nxt_res == 1 else 0  # cal current
                    # -1 loose / 0 draw / 1 win
                    cur_res = max(cur_res, nxt_res)
            if cur_res == -1 and (prevm != -1 if T else prevc != -1):
                print("go back", "prevm:", prevm, "prevc:",
                      prevc, "midx:", midx, "cidx:", cidx)
                cur_res = dfs(prevm, cidx, midx, prevc, False, path) if T else dfs(
                    midx, prevc, prevm, cidx, True, path)
            path.discard((midx, cidx, T))
            return cur_res

        res = dfs(1, 2, -1, -1, True, set())
        return 1 if res == 1 else 2 if res == -1 else 0
