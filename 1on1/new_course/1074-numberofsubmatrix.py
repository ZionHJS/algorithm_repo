class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n, m = len(matrix), len(matrix[0])
        # make the matrix to sum_matrix
        for i in range(n):
            for j in range(m):
                #0, 0
                if i == 0:
                    if j != 0:
                        matrix[0][j] += matrix[0][j-1]
                if j == 0:
                    if i != 0:
                        matrix[i][0] += matrix[i-1][0]
                # other
                matrix[i][j] += matrix[i-1][j] + \
                    matrix[i][j-1] - matrix[i-1][j-1]

        # traverse the sum_matrix to see if any submatrices that sum to a target
        self.count = 0
        for i in range(n-1):
            for j in range(m-1):
                self.count_target(i, j, matrix, target, n, m)

        return self.count

    # this travers is kind of brute/ anyway we can make it memorized?
    def count_target(self, y, x, matrix, target, n, m):
        for i in range(y+1, n):
            for j in range(x+1, m):
                dif_sum = matrix[i][j] - matrix[i][j-1] - \
                    matrix[i-1][j] + matrix[x][y]
                if dif_sum == target:
                    self.count += 1
