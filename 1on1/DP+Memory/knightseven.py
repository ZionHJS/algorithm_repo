def getNumberOfWays(self, n, m, limit, cost):
    if n == 1:
        return 1

    dp = [[0 for j in range(m+1)] for i in range(n+1)]
    dp[0][m] = 1

    for i in range(1, n+1):
        for k in range(i-1, i-limit-1, -1):
            for j in range(m+1):
                if j >= cost[i]:
                    dp[i][j-cost[i]] += dp[k][j]

    print("dp:", dp)
    return sum(dp[-1])
