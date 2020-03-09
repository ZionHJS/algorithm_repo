# 这个方法太过于暴力了 遭遇TLE
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n, m = len(matrix), len(matrix[0])
        self.count = 0
        # 1.make the matrix to sum_matrix
        for i in range(n):
            for j in range(m):
                #0, 0
                if i == 0 and j != 0:
                    matrix[0][j] += matrix[0][j-1]
                elif i != 0 and j == 0:
                    matrix[i][0] += matrix[i-1][0]
                elif i != 0 and j != 0:
                    matrix[i][j] += matrix[i-1][j] + \
                        matrix[i][j-1] - matrix[i-1][j-1]

        # 2.traverse the sum_matrix to see if any submatrices that sum to a target
        for i in range(n):
            for j in range(m):
                self.count_target(i, j, matrix, target, n, m)

        return self.count

    # this travers is kind of brute/ anyway we can make it memorized?
    def count_target(self, y, x, matrix, target, n, m):
        for i in range(y, n):
            for j in range(x, m):
                if y != 0 and x != 0:
                    cur_sum = matrix[i][j] - matrix[y-1][j] - \
                        matrix[i][x-1] + matrix[y-1][x-1]
                elif y == 0 and x != 0:
                    cur_sum = matrix[i][j] - matrix[i][x-1]
                elif y != 0 and x == 0:
                    cur_sum = matrix[i][j] - matrix[y-1][j]
                else:
                    cur_sum = matrix[i][j]

                if cur_sum == target:
                    self.count += 1


def numSubmatrixSumTarget(self, A, target):
    m, n = len(A), len(A[0])
    for row in A:
        for i in xrange(n - 1):
            row[i + 1] += row[i]
    res = 0
    for i in xrange(n):
        for j in xrange(i, n):
            c = collections.defaultdict(int)
            cur, c[0] = 0, 1
            for k in xrange(m):
                cur += A[k][j] - (A[k][i - 1] if i > 0 else 0)
                res += c[cur - target]
                c[cur] += 1
    return res
