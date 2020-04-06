class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix[0]), len(matrix)
        max_rsl = min(m, n)
        self.ans = []

        # pre_sum
        pre_sum = [[0 for j in range(m+1)] for i in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                pre_sum[i][j] = pre_sum[i-1][j] + pre_sum[i][j-1] - \
                    pre_sum[i-1][j-1] + matrix[i-1][j-1]
                if matrix[i-1][j-1] == target or pre_sum[i][j] == target:
                    return target

        # find the ans
        for i in range(1, n+1):
            for j in range(1, m+1):
                for k in range(i, n+1):
                    for o in range(j, m+1):
                        if k != i or o != j:
                            tmp_sum = self.get_sum(i, j, k, o, pre_sum)
                            if tmp_sum == target:
                                return target
                            elif tmp_sum < target:
                                self.ans.append(tmp_sum)
        if self.ans:
            self.ans.sort(key=lambda x: x)
            return self.ans[-1]
        else:
            return -1

    def get_sum(self, y1, x1, y2, x2, pre_sum):
        return pre_sum[y2][x2]-pre_sum[y1-1][x2]-pre_sum[y2][x1-1]+pre_sum[y1-1][x1-1]
