import collections


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)  # important!
        # build
        s_dp, e_dp, ans = collections.defaultdict(
            lambda: []), collections.defaultdict(lambda: []), 0
        for num in nums:
            if num+1 in s_dp:
                new_list = [num] + s_dp[num+1]  # 两个list的合并 算法复杂度? 有可能超时
                s_dp[num] = new_list
                #del s_dp[num+1]
                e_dp[new_list[-1]] = new_list
            if num-1 in e_dp:
                new_list = e_dp[num-1] + [num]
                e_dp[num] = new_list
                #del e_dp[num-1]
                s_dp[new_list[0]] = new_list
            if not s_dp[num]:
                s_dp[num] = [num]
            if not e_dp[num]:
                e_dp[num] = [num]

        # merge
        for s in s_dp:  # 最大的问题是遍历的时候s_dp /e_dp 一直在改变/一直在变没关系 只是value变了key并没有变
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
