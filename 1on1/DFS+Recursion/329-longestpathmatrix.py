from collections import deque


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        res = []

        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                res_ = []
                temp_res = [matrix[y][x]]
                self.dfs(matrix, y, x, res_, temp_res)
                # longest element in res_
                print('for loop res_is:', res_)
                length = self.findlongest(res_)
                res.append(length)

        return max(res)

    # dfs => get all result form a single node
    def dfs(self, matrix, y, x, res_, temp_res):
        help_y = [0, 0, -1, 1]
        help_x = [-1, 1, 0, 0]

        for i in range(4):
            next_y = y + help_y[i]
            next_x = x + help_x[i]
            if self.is_valid(matrix, next_y, next_x) and matrix[next_y][next_x] > matrix[y][x]:
                temp_res.append(matrix[next_y][next_x])
                self.dfs(matrix, next_y, next_x, res_, temp_res)
                temp_res.pop()
            else:
                if temp_res not in res_:
                    if len(res_) == 0:
                        res_.append(temp_res[::])
                    else:
                        if len(temp_res) > len(res_[-1]):  # 去重 节省空间
                            res_.append(temp_res[::])

                print('res_ is:', res_)

    def is_valid(self, matrix, y, x):
        y_, x_ = len(matrix), len(matrix[0])
        return 0 <= y < y_ and 0 <= x < x_

    def findlongest(self, list):
        length, item = max([(len(x), x) for x in list])
        return length


max_length, longest_element = max([(len(x), x) for x in ('a', 'b', 'aa')])
print('max_length:', max_length)
print('longest_element:', longest_element)

length, item = max([(len(x), x) for x in ('a', 'b', 'aa')])
print('item:', item)
print('length:', length)


res_ = []
print('res:', res_)
print('res -1 :', res_[-1])


haha = []
print('sorted:', haha[0])  # index out of range
