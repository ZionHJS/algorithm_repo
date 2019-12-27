# wrong answer exceed limit time
class Solution(object):
    def search(self, nums, target):
        if not nums:
            return False

        left, right = 0, len(nums) - 1

        while left+1 < right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return True

            # left edge
            if nums[mid] > nums[left]:
                if target <= nums[mid] and target >= nums[left]:
                    right = mid
                else:
                    left = mid

            # right edge
            elif nums[mid] < nums[right]:
                if target >= nums[mid] and target <= nums[right]:
                    left = mid
                else:
                    right = mid

            else:
                if nums[mid] == nums[left] or nums[mid] == nums[right]:
                    if target > nums[mid]:
                        right = mid
                    else:
                        left = mid
                else:
                    if target < nums[mid]:
                        right = mid
                    else:
                        left = mid

        if nums[right] == target:
            return True
        if nums[left] == target:
            return True

        return False

# ？？？ for 循环一次过？？？


class Solution(object):
    def search(self, nums, target):
        if not nums:
            return False

        for item in nums:
            if item == target:
                return True

        return False


# 二分法 解决方法
class Solution(object):
    def search(self, nums, target):
        if not nums:
            return False

        left, right = 0, len(nums) - 1

        while left + 1 < right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return True
            # [1, 2, 1, 1, 1] -> [2, 1, 1]
            while nums[left] == nums[mid] and nums[mid] == nums[right]:  # 抛弃两边但是还保留中间
                left += 1
                right -= 1
                if left > right or left >= len(nums) or right < 0:
                    return False
            # left edge
            if nums[left] <= nums[mid]:
                # target是否在左侧
                if target >= nums[left] and target <= nums[mid]:
                    right = mid
                else:
                    left = mid
            # right edge
            else:
                # target 是否在右侧
                if target >= nums[mid] and target <= nums[right]:
                    left = mid
                else:
                    right = mid
        if nums[left] == target:
            return True
        if nums[right] == target:
            return True
        return False
