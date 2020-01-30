class Solution:
    def divisorGame(self, N: int) -> bool:
        if N == 0 or N == 1:
            return False

        memo = (False for _ in range(N+1))  # Alice's Results and Bob's Results

        self.dfs(N, memo)
        print('memo:', memo)
        return memo[-1]

    def dfs(self, n, memo):  # N=2 => True
        if n == 0 or n == 1 or memo[n] != False:
            return memo[n]  # False

        #memo[n] = True

        for i in range(1, n):
            if n % i == 0:
                memo[n] = True
                memo[n-i] = self.dfs(n-i, memo)

        return memo[n]
