max_nums = max(1, 2, 3, 4, 5, 6)
print('max_nums:', max_nums)


num = -1234
num_str = str(abs(num))
print('num_str:', num_str)
num_num_str = int(num_str)
print('num_num_str:', num_num_str)

print('res:', int('000111'))


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        dp = [[0 for j in range(5)] for i in range(n)]

        # for 循环 从第一天开始循环
        for i in range(1, n):
            # 手中未持有股票的状态 0/2/4  0可以完全摒除不算
            for j in range(2, 5, 2):
                # 前一天未持股票 或 前一天持有(并不一定是前一天买入 可能是很多天前买入的) 今天卖出计算收益
                # if j > 1:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] +
                               prices[i] - prices[i-1])

            # 手中持有股票的状态 1/3   因为持有的状况要成为未持有的状况的基数 所以持有的情况必须记录最大值 计算了潜在最大值
            for j in range(1, 5, 2):
                dp[i][j] = max(dp[i][j-1], dp[i-1][j] +
                               prices[i] - prices[i-1])

        res = 0
        for j in range(0, 5, 2):  # j => 0/2/4 未持有的时候才能计算收益
            res = max(res, dp[n-1][j])  # 最后一row的最大值
        return res
