class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = len(nums)
        smaller_count = 0

        for i in range(count):
            left = i + 1
            right = count - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]

                if curr_sum < target:
                    smaller_count += (right-left)
                    left += 1
                else:
                    right -= 1

        return smaller_count
