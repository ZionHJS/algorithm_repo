class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        memo = [0 for _ in range(len(nums) + 1)]  # n+1
        memo[0], memo[1] = nums[0]

        return self.dfs(len(nums), nums, memo)

    def dfs(self, index, nums, memo):
        if index == 0 or index == 1 or nums[index] != 0:
            return memo[index]

        for i in range(index, -1, -1):
            res_1 = nums[index-1] + self.dfs(index-2, nums[:index-2], memo)
            res_2 = self.dfs(index-2, nums[:index-2], memo)

            memo[index] = max(res_1, res_2)

        return memo[index]

# dp 无敌了


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [-1 for _ in range(len(nums) + 1)]  # n+1
        dp[0] = 0
        dp[1] = nums[0]

        for i in range(2, len(nums)+1):
            dp[i] = max((nums[i-1] + dp[i-2]), dp[i-1])

        return dp[-1]
