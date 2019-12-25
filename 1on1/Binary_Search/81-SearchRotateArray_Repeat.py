# wrong answer
class Solution(object):
    def search(self, nums, target):
        if not nums:
            return False

        left, right = 0, len(nums) - 1
        max = 0

        while left + 1 < right:
            mid = left + (right - left)//2

            if nums[mid] >= nums[mid+1] and nums[mid] <= nums[mid-1]:
                right = mid
            elif nums[mid] <= nums[mid+1] and nums[mid] >= nums[mid-1]:
                left = mid
            else:
                max = mid

        if nums[right] >= nums[left]:
            max = right
        else:
            max = left

        if target <= nums[max]:
            left, right = 0, max

            while left+1 < right:
                mid = left+(right-left)//2
                if nums[mid] == target:
                    return True
                if nums[mid] < target:
                    left = mid
                else:
                    right = mid
            if nums[right] == target:
                return True
            if nums[left] == target:
                return True
        else:
            left, right = max+1, len(nums)-1

            while left+1 < right:
                mid = left + (right-left)//2

                if nums[mid] == target:
                    return True
                if nums[mid] < target:
                    left = mid
                else:
                    right = mid
            if nums[right] == target:
                return True
            if nums[left] == target:
                return True

        return -1
