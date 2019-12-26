class Solution(object):
    def findDuplicate(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if sum(n <= mid for n in nums) > mid:
                right = mid
            else:
                left = mid + 1
        return left

# 完美解决却多一层循环


class Solution(object):
    def findDuplicate(self, nums):
        if len(nums) == 1:
            return False

        left, right = 1, len(nums)-1

        while left + 1 < right:
            mid = left + (right-left)//2  # === (left+right)//2 ???
            if sum(item <= mid for item in nums) > mid:
                right = mid
            else:
                left = mid

        if sum(item == right for item in nums) > 1:
            return right
        else:
            return left
