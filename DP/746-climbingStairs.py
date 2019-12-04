class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1, 100, 1, 1, 100, 100, 1, 1]

cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

cost = [1, 100, 1]
def rec_minCost(cost):
    length = len(cost)
    opt = [0 for _ in range(len(cost))]
    opt[0] = cost[0]
    opt[1] = min(cost[0], cost[1])

    for i in range(2, len(cost)):
        A = opt[i-2] + cost[i]
        B = opt[i-1] + cost[i]
        opt[i] = min(A,B)
    print(opt)
    print(min(opt[length-1], opt[length-2]))

rec_minCost(cost)
