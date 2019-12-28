class Solution(object):
    def findMin(self, nums):
        if not nums:
            return False
        if nums[0] < nums[-1]:
            return nums[0]

        left, right = 0, len(nums)-1

        while left+1 < right:
            mid = left+(right-left)//2
            if nums[mid] > nums[0]:
                left = mid
            else:
                right = mid

        if nums[left] <= nums[right]:
            return nums[left]
        else:
            return nums[right]
