class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return False

        total_sum = 0
        for i in range(len(nums)):
            total_sum += nums[i]
        if total_sum % 2 != 0:
            return False

        target = total_sum//2

        # dp
        dp = [[False for j in range(target+1)] for i in range(len(nums)+1)]

        for i in range(len(nums)):
            dp[i][0] = True

        for i in range(1, len(nums)+1):
            for j in range(target+1):
                if j >= nums[i-1]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]  # 核心代码
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[len(nums)][target]
