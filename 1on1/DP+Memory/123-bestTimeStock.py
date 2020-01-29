class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        memo = [0 for _ in range(len(prices)+1)]

        self.dfs(len(prices), prices, memo)
        print('memo:', memo)
        return memo[-1]

    def dfs(self, index, prices, memo):
        if index == 0 or index == 1 or memo[index] != 0:
            return memo[index]

        if prices[index - 1] > prices[index - 2]:
            dif = prices[index-1] - prices[index-2]
            memo[index] = self.dfs(index-1, prices, memo) + dif
        else:
            for i in range(index-2, -1, -1):
                if prices[i] < prices[index-1]:
                    memo[index] = max(
                        (prices[index-1] - prices[i]), memo[index])

            if memo[index] != 0:
                return memo[index]
            else:
                memo[index] = self.dfs(index-1, prices, memo)

        return memo[index]
