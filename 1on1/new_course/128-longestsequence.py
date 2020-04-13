class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return []
        s_dp, e_dp, ans = {}, {}, 0
        for num in nums:
            if num+1 in s_dp:
                new_str = str(num) + dp[num+1]
                s_dp[new_str[0]] = new_str
                e_dp[new_str[-1]] = new_str
            if num-1 in e_dp:
                new_str = dp[num-1] + str(num)
                e_dp[new_str[-1]] = new_str
                s_dp[new_str[0]] = new_str
            if num not in s_dp:
                s_dp[num] = str(num)
            if num not in e_dp:
                e_dp[num] = str(num)

        for s in s_dp:
            if s-1 in e_dp:
                new_str = e_dp[s-1]+s_dp[s]
                ans = max(ans, len(new_str))
                s_dp[new_str[0]] = new_str
                e_dp[new_str[-1]] = new_str
        for e in e_dp:
            if e+1 in s_dp:
                new_str = e_dp[e]+s_dp[e+1]
                ns = max(ans, len(new_str))
                s_dp[new_str[0]] = new_str
                e_dp[new_str[0]] = new_str

        return ans
