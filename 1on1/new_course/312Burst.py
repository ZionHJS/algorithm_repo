class Solution:
    def maxCoins(self, N: List[int]) -> int:
        if not N:
            return 0
        N = list(filter(lambda x: x != 0, N))
        ans = 0

        # 从这里开始都是dfs()
        l, r = 0, len(N)-1
        while N[l] == 1 and l < r:
            l += 1
        while N[r] == 1 and r > l:
            r -= 1
        # 在 N[l+1:r] 里 dfs
        left, right, cur_N = N[l], N[r], []
        if l+1 < r:
            cur_N = N[l+1:r]
        #print("begin_cur_N:", cur_N)
        while l+1 < r and len(cur_N) > 2:
            cur_min = min(cur_N)
            cur_N = [left] + cur_N + [right]
            cur_pop = [0, math.inf]
            for i in range(1, len(cur_N)-1):
                if cur_N[i] == cur_min and cur_N[i-1]*cur_N[i]*cur_N[i+1] > cur_pop[0]:
                    cur_pop = [cur_N[i-1]*cur_N[i]*cur_N[i+1], i]
            #print("cur_pop:", cur_pop)
            ans += cur_pop[0]
            cur_N = cur_N[1:cur_pop[1]] + cur_N[cur_pop[1]+1:-1]

        #print("ans:", ans)
        if l != r:
            #print("end here!")
            ans += left*right + max(left, right) * \
                (l+(len(N)-1-r)) + max(left, right)
        else:
            ans += left*(len(N))

        return ans

        # bottom-top dp
        N = [1] + [x for x in N if x > 0] + [1]
        n = len(N)
        dp = [[0 for j in range(n)] for i in range(n)]
        for i in range(2, n):
            for l in range(0, n-i):  # i和j是镜像的
                r = l+i
                for k in range(l+1, r):
                    last_burst = N[l]*N[k]*N[r]
                    dp[l][r] = max(dp[l][r], dp[l][k] + last_burst + dp[k][r])
        return dp[0][n - 1]
