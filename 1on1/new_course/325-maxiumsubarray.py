class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        ans = 0
        prefix = [0 for i in range(len(nums)+1)]
        for i in range(1, len(prefix)):
            prefix[i] = prefix[i-1] + nums[i-1]
        print("prefix:", prefix)
        for i in range(len(nums))[::-1]:
            for j in range(1, len(prefix)-i):
                #print("i:", i, "j:", j)
                if prefix[j+i] - prefix[j-1] == k:
                    return i

        return 0
