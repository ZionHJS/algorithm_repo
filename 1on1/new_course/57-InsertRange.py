class Solution:
    def insert(self, I: List[List[int]], N: List[int]) -> List[List[int]]:
        if not I:
            return I + [N]
        # dfs()

        def dfs(idx, CI):
            if idx == len(CI)-1:
                return CI
            elif CI[idx][1] < CI[idx+1][0]:
                return CI
            else:
                CI[idx+1] = [min(CI[idx][0], CI[idx+1][0]),
                             max(CI[idx][1], CI[idx+1][1])]
                CI.pop(idx)
                CI = dfs(idx, CI)
            return CI

        # binary search
        idx = bisect.bisect_left(I, N)
        if idx > 0:
            if idx <= len(I)-1:
                if I[idx-1][1] >= N[0]:
                    I[idx-1] = [I[idx-1][0], max(I[idx-1][1], N[1])]
                    I = dfs(idx-1, I)
                else:
                    if N[1] >= I[idx][0]:
                        I[idx] = [N[0], max(N[1], I[idx][1])]
                        I = dfs(idx, I)
                    else:
                        I = I[:idx] + [N] + I[idx:]
            else:
                I += [N]
                I = dfs(idx-1, I)
        else:
            if N[1] >= I[idx][0]:
                I[idx] = [N[0], max(N[1], I[idx][1])]
            else:
                I = [N] + I
            dfs(idx, I)

        return I
