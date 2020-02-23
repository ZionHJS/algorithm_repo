import math


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [[math.inf for j in range(m+1)] for i in range(n+1)]
        # pre_sum
        pre_sum = [0 for _ in range(n+1)]
        pre_sum[0] = nums[0]
        for i in range(n):
            pre_sum[i+1] = pre_sum[i] + nums[i]

        dp[0][0] = 0

        for i in range(1, n+1):
            for j in range(1, m+1):
                for k in range(i):
                    if dp[k][j-1] < math.inf:  # optimization
                        dp[i][j] = min(dp[i][j], max(
                            dp[k][j-1], pre_sum[i] - pre_sum[k]))

        return dp[n][m]
