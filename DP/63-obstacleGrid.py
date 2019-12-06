class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        n = len(obstacleGrid)   #all-row list_length
        m = len(obstacleGrid[0])  #single-row list_length
        if n == 1 or m == 1:
            for k in obstacleGrid[0]:
                if k == 1:
                    return 0
            for l in obstacleGrid:
                if l[0] == 1:
                    return 0
        if obstacleGrid[0][0] == 1:
            return 0
                    
        #initialize 1d grid           
        opt = [1]*n
        for k in range(0, n):
            if obstacleGrid[k][0] == 1:
                for o in range(k, n):
                    opt[o] = 0
        for i in range(1, m):
            for j in range(0, n):
                if obstacleGrid[j][i] == 1:
                    opt[j] = 0
                elif opt[j-1] != None:
                    opt[j] += opt[j-1]
        return opt[-1]

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        for row in range(m):
            for col in range(n):
                if obstacleGrid[row][col] == 1:
                    obstacleGrid[row][col] = 0
                    continue
                if row == 0 and col == 0:
                    obstacleGrid[row][col] = 1
                elif row == 0 or col == 0:
                    obstacleGrid[row][col] = obstacleGrid[row][col-1] if row == 0 else obstacleGrid[row-1][col]
                else:
                    obstacleGrid[row][col] = obstacleGrid[row][col-1] + obstacleGrid[row-1][col]
        return obstacleGrid[-1][-1]