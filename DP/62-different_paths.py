import numpy as np
#空间复杂度O(3n)
def uniquePaths(m, n):
        opt = np.zeros([m, n])
        opt[0, :] = 1
        opt[:, 0] = 1
        for i in range(1, m):
            for j in range(1, n):
                opt[i][j] = opt[i][j-1] + opt[i-1][j]
        return opt[m-1, n-1]

uniquePaths(10,10)

#空间复杂度更低的解法O(n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]
        return cur[-1]