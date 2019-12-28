class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        res = []
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                # continue
                pass
            self.findTwoSum(nums, i+1, len(nums)-1, -nums[i], res)
        return res

    def findTwoSum(self, nums, start, end, target, res):
        i, j = start, end
        while i < j:
            if nums[i] + nums[j] == target:
                res.append([-target, nums[i], nums[j]])
                i += 1
                j -= 1
                while i < j and nums[i] == nums[i - 1]:
                    i += 1
                while i < j and nums[j] == nums[j + 1]:
                    j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                j -= 1
