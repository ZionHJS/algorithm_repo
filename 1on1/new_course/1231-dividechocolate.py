import math


class Solution:
    def maximizeSweetness(self, A: List[int], K: int) -> int:
        n = len(A)
        if not n:
            return 0
        elif K == 0:
            return sum(A)
        # dp
        dp = [[-math.inf for j in range(K+1)] for i in range(n)]
        dp[0][0] = A[0]

        for i in range(1, n):
            dp[i][0] = dp[i-1][0]+A[i]

        for i in range(1, n):
            for j in range(1, K+1):
                for o in range(i):
                    # find max out of the mins
                    dp[i][j] = max(dp[i][j], min(
                        dp[o][j-1], dp[i][0]-dp[o][0]))

        return dp[-1][-1]
