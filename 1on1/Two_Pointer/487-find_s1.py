class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        count = 0
        max_count = 0
        counter_0 = 0
        i, j = 0, 0

        while j < len(nums):
            count += 1
            if nums[j] == 0:
                counter_0 += 1
            max_count = max(max_count, count)

            while i < j and counter_0 >= 1:
                if i > 0 and nums[i-1] == 0:
                    i = i - 1
                    continue

                if j < len(nums)-1 and nums[j+1] == 1:
                    count = j - i + 1
                else:
                    count = j - i

                counter_0 -= 1
                i = j

                max_count = max(max_count, count)
                count = 0

            j += 1

        return max_count
