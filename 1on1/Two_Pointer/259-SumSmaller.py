# 错误的解法 O(n3)
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) < 3:
            return False
        nums.sort()
        res = 0
        k = 0
        for k in range(len(nums) - 2):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            self.findTwoSum(nums, k+1, len(nums)-1, target - nums[k], res)
        return res

    def findTwoSum(self, nums, start, end, target_k, res):
        while start < end:
            if nums[start] + nums[end] < target_k:
                tmp_start = start
                tmp_end = end

                while tmp_start < tmp_end:
                    res += 1
                    tmp_end -= 1

                start += 1
            else:
                end -= 1
        return res
