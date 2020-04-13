class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        # find peak
        def find_nxtpeak(idx, nums):
            peak_idx = idx
            for i in range(idx+1, len(nums)-1):
                if nums[i] < nums[i-1]:
                    break
                peak_idx += 1
            return peak_idx

        # main
        nums_min, j = nums[0], 1
        while j < len(nums):
            nums_min = min(nums_min, nums[j])
            if nums[j] > nums[j-1]:
                nxt_idx = find_nxtpeak(j-1, nums)
                for k in range(nxt_idx+1, len(nums)):
                    if nums_min < nums[k] < nums[nxt_idx]:
                        return True
                j = nxt_idx + 1
            else:
                j += 1

        return False
