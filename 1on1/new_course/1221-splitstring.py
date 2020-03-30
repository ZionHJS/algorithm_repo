class Solution:
    def balancedStringSplit(self, s: str) -> int:
        n = len(s)
        if n <= 2:
            return 0

        def is_valid(sub_s):
            left = 0
            for i in range(len(sub_s)):
                if sub_s[i] == "L":
                    left += 1
                else:
                    left -= 1
            return left == 0

        dp = [0 for i in range(len(s)+1)]
        memo = set()

        for i in range(2, len(dp)):
            for j in range(i-2, -1, -1):
                tmp_s = s[j:i]
                if tmp_s in memo:
                    dp[i] = max(dp[i], dp[j]+1)
                else:
                    if is_valid(s[j:i]):
                        memo.add(s[j:i])
                        dp[i] = max(dp[i], dp[j]+1)

        return dp[-1]
