def backPackIV(self, nums, target):
    if target == 0 or not nums:
        return 0

    n = len(nums)
    m = target

    dp = [0 for j in range(m+1)]

    for i in range(n):
        for j in range(1, m+1):
            if i == 0:
                print("j:", j)
                if j == nums[0]:
                    dp[j] = 1
                elif j > nums[0]:
                    dp[j] += dp[j-nums[0]]
                print("dp:", dp)
            if j >= nums[i]:
                dp[j] += dp[j-nums[i]]
                #print("dp[j]:", dp[j])

    #print("dp:", dp)

    return dp[-1]


# 563
class Solution:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """

    def __init__(self):
        self.count = 0

    def backPackV(self, nums, target):
        if not nums or not target:
            return 0

        n = len(nums)
        m = target

        dp = [[0 for j in range(m+1)] for i in range(2)]
        for i in range(2):
            dp[i][0] = 1

        for i in range(n):
            for j in range(m+1):
                if i == 0:
                    if j == nums[0]:
                        dp[0][j] = 1
                else:
                    dp[i % 2][j] = dp[(i-1) % 2][j]
                    if j >= nums[i]:
                        dp[i % 2][j] += dp[(i-1) % 2][j-nums[i]]

        print("dp:", dp)
        return max(dp[0][-1], dp[1][-1])
