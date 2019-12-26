class Solution(object):
    def search(self, nums, target):
        if not nums:
            return -1

        left, right = 0, len(nums)-1

        while left+1 < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            # left edge
            if nums[mid] > nums[left]:
                # target in left or not
                if target <= nums[mid] and target >= nums[left]:
                    right = mid
                else:
                    left = mid

            # right edge
            else:
                # target is in right or not
                if target >= nums[mid] and target <= nums[right]:
                    left = mid
                else:  # else is the key situation
                    right = mid

        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1
