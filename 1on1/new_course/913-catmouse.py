class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        def dfs(midx, cidx, prevm, prevc, T, path, circle):  # T => mouse / not T => cat
            if (midx, cidx, T) in path:
                #print("repeat!", "midx:", midx, "cidx:", cidx)
                return path[(midx, cidx, T)]
            # when draw
            if (midx, cidx, T) in circle:
                # print("circled!")
                path[(midx, cidx, T)] = 0
                return 0

            cur_res = -1
            cur_idx = midx if T else cidx
            prev = prevm if T else prevc
            #print("cur_idx:", cur_idx)
            # 先看看前面还有路没有  没路走 必输
            if len(graph[cur_idx]) == 1 and prev[-1] != -1:
                #Aprint("Dead End!")
                path[(midx, cidx, T)] = -1
                return -1
            # 向前dfs()每一种可能性 看看能否获胜
            for nidx in graph[cur_idx]:
                if nidx == 0 and T:  # Mouse wins
                    #print("M wins")
                    path[(midx, cidx, T)] = 1
                    return 1
                elif nidx == midx and not T:  # Cat wins
                    #print("C wins")
                    path[(midx, cidx, T)] = 1
                    return 1
                if nidx != prev[-1] and nidx != 0 and nidx != cidx:
                    #print("nxt_idx:", nidx)
                    nxt_res = dfs(nidx, cidx, prevm+[midx], prevc, False, path, circle) if T else dfs(
                        midx, nidx, prevm, prevc+[cidx], True, path, circle)
                    nxt_res = 1 if nxt_res == -1 else -1 if nxt_res == 1 else 0  # cal current
                    # -1 loose / 0 draw / 1 win
                    cur_res = max(cur_res, nxt_res)
                    if cur_res == 1:
                        #print("CurWins Break!", "cur_idx:", cur_idx)
                        path[(midx, cidx, T)] = 1
                        return 1
                # else:
                #     print("nidx:", nidx, "empty!")

            # 前面都是输 那就试着往回走吧 看看能否有平局产生
            if cur_res == -1 and prev[-1] != -1:
                circle.add((midx, cidx, T))
                previdx = prev.pop()
                #print("try go back!", "cur_idx:", cur_idx, "cur_T", T, "prev_idx:", previdx)
                nxt_res = dfs(previdx, cidx, prevm, prevc, False, path, circle) if T else dfs(
                    midx, previdx, prevm, prevc, True, path, circle)
                cur_res = 1 if nxt_res == -1 else -1 if nxt_res == 1 else 0
                #print("cur_res:", cur_res, "dis_card:", (midx, cidx, T))
                circle.discard((midx, cidx, T))
                #print("append:", previdx)
                prev.append(previdx)

            path[(midx, cidx, T)] = cur_res
            return cur_res

        res = dfs(1, 2, [-1], [-1], True, {}, set())

        return 1 if res == 1 else 2 if res == -1 else 0
