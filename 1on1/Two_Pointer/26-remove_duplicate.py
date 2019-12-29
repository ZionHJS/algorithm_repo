class Solution(object):
    def removeDuplicates(self, nums):
        if not nums or len(nums) == 1:
            return nums

        tmp = nums[0]
        i, j = 0, 1

        while j <= len(nums) - 1:
            if nums[j] > tmp:
                if i + 1 < j:
                    i += 1
                    tmp = nums[j]
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1
                    continue
                else:
                    j += 1
            else:
                j += 1

        return nums[:i]
