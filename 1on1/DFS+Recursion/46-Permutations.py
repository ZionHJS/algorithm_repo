class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        res = []
        temp = []
        visited = []

        self.dfs(nums, res, temp, visited)
        return res

    def dfs(self, nums, res, temp, visited):
        if len(temp) == len(nums):
            res.append(temp[:])
            return

        for i in range(len(nums)):
            if nums[i] in temp:
                i += 1
                continue
            temp.append(nums[i])
            # visited.append(nums[i])

            self.dfs(nums, res, temp, visited)
            temp.pop()
            # visited.pop()
