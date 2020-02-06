# memo
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        memo = [0 for _ in range(len(prices)+1)]
        self.dfs(len(prices), prices, memo)
        print('memo:', memo)
        return max(memo)

    def dfs(self, n, prices, memo):
        if n == 0 or n == 1 or memo[n] != 0:
            return memo[n]

        for i in range(n, 1, -1):
            for j in range(i-1, 0, -1):
                if prices[j-1] < prices[i-1]:
                    if j > 2:
                        memo[i] = max((prices[i-1] - prices[j-1]) +
                                      self.dfs(j-2, prices, memo), memo[i])
                    else:
                        memo[i] = max(prices[i-1] - prices[j-1], memo[i])

        return memo[n]

# dp


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        memo = [0 for _ in range(len(prices)+1)]

        for i in range(2, len(memo)):
            for j in range(1, i-1, -1):
                if prices[j-1] < prices[i-1]:
                    if j > 3:
                        memo[i] = max(
                            memo[i], (prices[i-1] - prices[j-1])+memo[j-3])
                    else:
                        memo[i] = max(memo[i], prices[i-1] - prices[j-1])

        print('memo:', memo)
        return max(memo)
