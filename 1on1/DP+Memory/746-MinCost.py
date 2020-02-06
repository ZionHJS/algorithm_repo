# Memo
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0

        memo = [0 for _ in range(len(cost)+1)]  # len(memo) == len(cost) + 1
        memo[0] = cost[0]
        memo[1] = cost[1]
        cost.append(0)

        self.dfs(len(cost)-1, cost, memo)
        print('memo:', memo)
        return memo[-1]

    def dfs(self, n, cost, memo):
        if n == 0 or n == 1 or memo[n] != 0:
            return memo[n]

        for i in range(n, 0, -1):  # 针对memo
            memo[i-1] = self.dfs(i-1, cost, memo)
            memo[i-2] = self.dfs(i-2, cost, memo)
            memo[i] = min(memo[i-2]+cost[i], memo[i-1]+cost[i])

        return memo[n]

# DP


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0

        memo = [0 for _ in range(len(cost)+1)]  # len(memo) == len(cost) + 1
        memo[0] = cost[0]
        memo[1] = cost[1]
        cost.append(0)

        for i in range(2, len(memo)):
            memo[i] = min(memo[i-1]+cost[i], memo[i-2]+cost[i])

        return memo[-1]
