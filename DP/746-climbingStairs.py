class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1, 100, 1, 1, 100, 100, 1, 1]

cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

def rec_minCost(cost):
    _len = len(cost)
    if _len < 2:
        return 0
    else:
        opt = [0]*_len
        opt[0] = cost[0]
        opt[1] = min(cost[0], cost[1])
        for i in range(2, len(cost)):
            A = opt[i-2]
            B = opt[i-1]
            opt[i] = min(A, B) + cost[i]
    print(min(opt[_len-1], opt[_len-2]))
rec_minCost(cost)


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        _len = len(cost)
        if _len < 2:
            return 0
        else:
            dp = [0]*_len
            dp[:2] = cost[:2]
            for i in range(2, _len):
                dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
            return min(dp[-1], dp[-2])
