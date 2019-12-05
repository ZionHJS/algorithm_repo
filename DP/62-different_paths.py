import numpy as np

def uniquePaths(m, n):
        opt = np.zeros([m, n])
        opt[0, :] = 1
        opt[:, 0] = 1
        for i in range(1, m):
            for j in range(1, n):
                opt[i][j] = opt[i][j-1] + opt[i-1][j]
        return opt[m-1, n-1]
        
uniquePaths(10,10)
        