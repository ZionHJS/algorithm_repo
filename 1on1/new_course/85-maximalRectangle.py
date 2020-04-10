class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n, res = len(matrix[0]), len(matrix), 0

        # pre_sum
        pre_sum = [[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if j == 0:
                    pre_sum[i][j] = int(matrix[i][j])
                else:
                    pre_sum[i][j] = pre_sum[i][j-1]+int(matrix[i][j])

        for y1 in range(m):
            for y2 in range(y1, m):
                tmp_times, times, i = 0, 0, 0
                while i < n:
                    if matrix[i][y1] != "0" and matrix[i][y2] != "0":
                        if pre_sum[i][y2]-pre_sum[i][y1] == y2-y1:
                            tmp_times += 1
                        else:
                            times = max(times, tmp_times)
                            tmp_times = 0
                        if y1 == 2 and y2 == 4:
                            print("y1:", y1, "y2:", y2)
                            print("tmp_times:", tmp_times, "times:", times)
                    i += 1
                res = max(res, times*(y2-y1+1))

        return res

        class Solution:

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix[0]), len(matrix)
        height = [0] * (m + 1)  # 这个就是所谓的桶排序??? BucketSort
        ans = 0

        for row in matrix:  # O(n*(2*m))
            for i in range(m):
                height[i] = height[i] + 1 if row[i] == '1' else 0
                #print("height:", height)
            stack = [-1]
            for i in range(m + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    ans = max(ans, h * w)
                stack.append(i)
        return ans
