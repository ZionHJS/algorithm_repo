class Solution(object):
    def findPeakElement(self, nums):
        if not nums:
            return -1

        left, right = 0, len(nums)-1

        while left + 1 < right:
            mid = left + (right-left)//2

            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            elif nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid

        if nums[right] > nums[left]:
            return right
        else:
            return left

        return -1
