class Solution(object):
    def searchInsert(self, nums, target):
        if not nums:
            return -1

        left, right = 0, len(nums) - 1

        while left + 1 < right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid

        if nums[right] == target:
            return right
        elif nums[left] == target:
            return left
        elif nums[left] < target and nums[right] > target:
            return left + 1
        elif nums[right] < target:
            return right + 1
        else:
            return left
