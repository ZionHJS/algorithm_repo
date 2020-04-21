class Solution:
    def findDiagonalOrder(self, M: List[List[int]]) -> List[int]:
        if not len(M) or not len(M[0]):
            return []
        n, m = len(M), len(M[0])
        cur = (0, 0)
        ans = []
        d = 0
        directions = ((-1, 1), (1, -1))

        while cur != (n-1, m-1):
            #print("cur:", cur)
            if not ans or (M[cur[0]][cur[1]] != ans[-1]):
                ans.append(M[cur[0]][cur[1]])
            if not d:
                nxt_y, nxt_x = cur[0]+directions[0][0], cur[1]+directions[0][1]
            else:
                nxt_y, nxt_x = cur[0]+directions[1][0], cur[1]+directions[1][1]

            if 0 <= nxt_y < n and 0 <= nxt_x < m:  # valid
                cur = (nxt_y, nxt_x)
            else:  # invalid
                if (nxt_y < 0 and 0 <= nxt_x < m):
                    cur = (cur[0], nxt_x)
                elif (nxt_y < 0 and nxt_x >= m):
                    cur = (cur[0]+1, m-1)
                elif (nxt_x < 0 and 0 <= nxt_y < n):
                    cur = (nxt_y, cur[1])
                elif (nxt_x < 0 and nxt_y >= n):
                    cur = (n-1, cur[1]+1)
                elif (nxt_y >= n and 0 <= nxt_x < m):
                    cur = (cur[0], cur[1]+1)
                elif (nxt_x >= m and 0 <= nxt_y < n):
                    cur = (cur[0]+1, cur[1])
                d = 1-d

        ans.append(M[-1][-1])
        return ans
