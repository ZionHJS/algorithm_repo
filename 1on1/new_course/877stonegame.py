class Solution:
    def stoneGame(self, P: List[int]) -> bool:
        memo = {}

        def dfs(s_idx, e_idx, T):
            if (s_idx, e_idx, T) in memo:
                return memo[(s_idx, e_idx, T)]
            if e_idx == s_idx:
                return (asm+P[s_idx]) > lsm if T else lsm+P[s_idx] > asm

            nxt1 = dfs(s_idx+1, e_idx, asm+P[s_idx], lsm, False) if T else dfs(
                s_idx+1, e_idx, asm, lsm+P[s_idx], True)
            nxt2 = dfs(s_idx, e_idx-1, asm+P[e_idx], lsm, False) if T else dfs(
                s_idx, e_idx-1, asm, lsm+P[e_idx], True)

            nxt1 = False if nxt1 else True
            nxt2 = False if nxt2 else True

            memo[(s_idx, e_idx, T)] = nxt1 or nxt2
            return memo[(s_idx, e_idx, T)]

        ans = dfs(0, len(P)-1, 0, 0, True)

        return ans
