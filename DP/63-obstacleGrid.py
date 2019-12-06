class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        if n == 1 or m == 1:
            for k in obstacleGrid[0]:
                if k == 1:
                    return 0
            for l in obstacleGrid:
                if l[0] == 1:
                    return 0
                    
        #initialize 1d grid           
        opt = [1]*n
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    opt[j] = 0
                elif opt[j-1] == 0:
                    opt[j] = opt[j]
                elif opt[j] == 0:
                    opt[j] = opt[j-1]
                elif opt[j] == 0 and opt[j-1] == 0:
                    opt[j] = [0]
                else:
                    opt[j] += opt[j-1]
        return opt[-1]

