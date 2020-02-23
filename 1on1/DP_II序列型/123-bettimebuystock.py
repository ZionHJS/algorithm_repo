class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)

        dp = [[0 for j in range(3)] for i in range(n)]

        min_ = prices[0]
        # for 循环 从第二天开始循环 i == 1
        for i in range(1, n):
            min_ = min(min_, prices[i])

            # 第0次交易
            j = 0
            dp[i][j] = 0

            # 第一次交易
            j = 1
            dp[i][1] = max(dp[i][1], prices[i] - min_)
            print("dp[i][1]:", dp[i][1])

            # 第二次交易
            j = 2
            max_sub = prices[i] - prices[i-1]
            #max_sub = max_ - min_
            for k in range(i-1, -1, -1):
                max_sub = max(max_sub, prices[i] - prices[k])
                dp[i][2] = max(dp[i][2], dp[k][1]+max_sub)

            dp[i][2] = max(dp[i][j-1], dp[i][2], dp[i-1]
                           [2]+prices[i]-prices[i-1])

        res = 0
        for i in range(n):
            res = max(res, dp[i][2])

        return res
