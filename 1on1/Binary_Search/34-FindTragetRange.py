class Solution(object):
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]

        start_index, end_index = 0, 0

        left, right = 0, len(nums) - 1

        while left+1 < right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                while mid-1 >= left and nums[mid-1] >= nums[mid]:
                    mid -= 1
                start_index = mid

                while mid+1 <= right and nums[mid+1] <= nums[mid]:
                    mid += 1
                end_index = mid

                return [start_index, end_index]
            else:
                if nums[mid] < target:
                    left = mid
                else:
                    right = mid

        if nums[left] == target and nums[right] == target:
            return [left, right]
        else:
            if nums[left] == target and nums[right] != target:
                return [left, left]
            elif nums[right] == target and nums[left] != target:
                return [right, right]
            else:
                return [-1, -1]
