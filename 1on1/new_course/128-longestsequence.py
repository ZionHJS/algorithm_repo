import collections


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return 1

        s_dp, e_dp, ans = {}, {}, 0
        #s_dp, e_dp, ans = collections.defaultdict(lambda:[]), collections.defaultdict(lambda:[]), 0
        for num in nums:
            if num+1 in s_dp:
                new_list = [num] + s_dp[num+1]
                ans = max(ans, len(new_list))
                s_dp[num] = new_list
                e_dp[new_list[-1]] = new_list
            if num-1 in e_dp:
                new_list = e_dp[num-1] + [num]
                ans = max(ans, len(new_list))
                e_dp[num] = new_list
                s_dp[new_list[0]] = new_list
            if num not in s_dp:
                s_dp[num] = [num]
            if num not in e_dp:
                e_dp[num] = [num]

        for s in s_dp:
            if s-1 in e_dp:
                new_list = e_dp[s-1]+s_dp[s]
                ans = max(ans, len(new_list))
                s_dp[new_list[0]] = new_list
                e_dp[new_list[-1]] = new_list
        for e in e_dp:
            if e+1 in s_dp:
                new_list = e_dp[e]+s_dp[e+1]
                ans = max(ans, len(new_list))
                s_dp[new_list[0]] = new_list
                e_dp[new_list[-1]] = new_list

        return ans if ans else 1
