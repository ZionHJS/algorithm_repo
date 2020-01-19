class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        res = []
        temp = []

        self.dfs(nums, 0, temp, res)
        return res

    def dfs(self, nums, index, temp, res):
        if index == len(nums):  # => exit condition
            res.append(temp[:])  # => deep copy
            return

        # select
        temp.append(nums[index])
        self.dfs(nums, index+1, temp, res)
        temp.pop()
        # not-select
        self.dfs(nums, index+1, temp, res)
