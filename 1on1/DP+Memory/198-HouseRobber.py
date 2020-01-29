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
