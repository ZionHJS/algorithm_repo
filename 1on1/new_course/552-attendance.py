class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 1e9+7
        total = 3**n
        dp = [[1 if i == j or i == 0 else 0 for j in range(
            n+1)] for i in range(n+1)]
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                # for k in range(i-1, j):
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
        #print("dp:", dp, "total:", total)

        # for cnt_A
        cnt_A = 0
        for i in range(2, n+1):
            cnt_A += dp[i][n]*(2**(n-i))
            #print("i:",i, "n:", n, "dp[i][n]:", dp[i][n], "n-i:", n-i, "cur:", dp[i][n]*(2**(n-i)))
        #print("cnt_A:", cnt_A)
        # for cnt_L
        cnt_L = 0
        for i in range(3, n+1):
            union = 0
            if n-i >= 2:
                for k in range(2, n-i+1):
                    union += dp[k][n-i]*(2**(n-i-k))
            #print("union:", union)
            cnt_L += dp[i][n]*(2**(n-i))-dp[i][n]*union
            print("i:", i, "union:", union, "cur:",
                  (dp[i][n]-union)*(2**(n-i)))
        #print("total:", total, "cnt_A:", cnt_A, "cnt_L:", cnt_L)
        # get result
        res = int((total-(cnt_A+cnt_L)) % mod)

        return res
