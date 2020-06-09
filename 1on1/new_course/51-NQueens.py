class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        B = [["." for j in range(n)] for i in range(n)]
        seeds_mid = set()
        seeds_left = set()
        seeds_right = set()
        res = []

        def dfs(cur_i, B):
            nonlocal n, seeds_mid, seeds_left, seeds_right
            if cur_i >= n:
                tmp_res = []
                for row in B:
                    row = "".join(row)
                    tmp_res.append(row)
                res.append(tmp_res)
                return
            for j in range(n):
                if (j not in seeds_mid) and (j-cur_i not in seeds_left) and (j+cur_i not in seeds_right):
                    seeds_mid.add(j)
                    seeds_left.add(j-cur_i)
                    seeds_right.add(j+cur_i)
                    B[cur_i][j] = "Q"
                    dfs(cur_i+1, B)
                    B[cur_i][j] = "."
                    seeds_mid.discard(j)
                    seeds_left.discard(j-cur_i)
                    seeds_right.discard(j+cur_i)
        dfs(0, B)
        return res
