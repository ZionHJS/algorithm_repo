class Solution:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """

    def backPackV(self, A, K):  # K => target
        if not A or not K:
            return 0

        dp = [[0 for j in range(K+1)] for i in range(2)]
        dp[0][0] = 1

        for i in range(1, len(A)):
            for j in range(K+1):
                if j-A[i] >= 0:
                    if i % 2:  # when even  1 3 5 7 9...
                        dp[i % 2][j] = dp[(i-1) % 2][j] + dp[(i-1) % 2][j-A[i]]
                    else:
                        dp[i % 2][j] = dp[(i+1) % 2][j] + \
                            dp[((i+1) % 2)][j-A[i]]
                else:
                    if i % 2:  # when even  1 3 5 7 9...
                        dp[i % 2][j] = dp[(i-1) % 2][j]
                    else:
                        dp[i % 2][j] = dp[(i+1) % 2][j]

        return dp[i % 2][-1] if (len(A)-1) % 2 else dp[(i-1) % 2][-1]


class Solution:
    def change(self, cashbox, amount): -> int
     dp = [[0 for j in range(amount+1)] for i in range(2)]
      dp[0][0] = 1
       for k in range(len(cashbox[0])):
            if cashbox[0][k] <= amount:
                dp[0][cashbox[0][k]] += 1

        for i in range(1, len(cashbox)):
            dp[i % 2] = dp[(i-1) % 2]
            for k in range(len(cashbox[i])):
                for j in range(amount, cashbox[i][k]-1, -1):
                    dp[i % 2][j] += dp[(i-1) % 2][j - cashbox[i % 2][k]]

        return dp[len(cashbox) % 2][-1]
