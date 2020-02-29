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
