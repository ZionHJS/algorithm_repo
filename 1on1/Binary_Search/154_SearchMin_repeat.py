class Solution(object):
    def findMin(self, nums):
        if not nums:
            return False

        left, right = 0, len(nums)-1

        while left + 1 < right:
            mid = left + (right - left)//2
            if nums[mid] == nums[left] and nums[mid] == nums[right]:
                left += 1
                right -= 1
            else:
                if nums[left] < nums[right]:
                    return nums[left]
                elif nums[mid] >= nums[left]:
                    left = mid
                else:
                    right = mid

        if nums[left] <= nums[right]:
            return nums[left]
        else:
            return nums[right]
