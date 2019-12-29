class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        if len(nums) == 2:
            if nums[-1] == 0:
                if nums[0] == 1:
                    return 2
                else:
                    return 1
            else:
                return 2

        count = 0
        max_count = 0
        counter_0 = 0
        i, j = 0, 0

        while j < len(nums):
            if counter_0 < 1:
                count += 1
            if nums[j] == 0:
                counter_0 += 1
            max_count = max(max_count, count)

            while i < j and counter_0 >= 1:
                if i > 0 and nums[i-1] == 0:
                    i = i - 1
                    continue

                if nums[i] != 0:
                    while j < len(nums) - 1 and nums[j+1] == 0:
                        j += 1
                    if j < len(nums)-1:
                        count = j - i + 2
                    else:
                        count = j - i + 1
                else:
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
