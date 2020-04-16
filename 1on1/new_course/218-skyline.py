import heapq


class Solution:
    def getSkyline(self, B: List[List[int]]) -> List[List[int]]:
        #B.sort(); ans = []; tmp = []; tmp_ans = []; tmp_right = 0
        B.sort()
        ans = []
        tmp = []
        heap = []
        tmp_right = 0
        for i in range(len(B)):
            if not tmp_ans:
                tmp_ans.append([B[0][0], B[0][2]])
                tmp.append([B[0][1], B[0][2]])
                continue
            if B[i][0] <= tmp_right:
                if B[i][2] > tmp_ans[-1][1]:
                    tmp_ans.append([B[i][0], B[i][2]])
                    tmp.append([B[i][1], B[i][2]])
                elif B[i][2] == tmp_ans[-1][1]:
                    tmp.append([B[i][1], B[i][2]])
                else:
                    tmp_height = 0
                    for cube in tmp:
                        if cube[0] >= B[i][1]:
                            tmp_height = max(tmp_height, cube[1])
                    if tmp_height == 0:
                        tmp_ans.append([B[i][1], tmp_height])
                        ans += tmp_ans
                        tmp_ans = []
                        continue
                    tmp_ans.append([B[i][0], tmp_height])
            else:
                tmp_ans.append([B[i-1][1], 0])
                ans += tmp_ans
                tmp_ans = [[B[i][1], B[i][2]]]
            tmp_right = max(tmp_right, B[i][1])

        return ans


class Solution:
    def getSkyline(self, B: List[List[int]]) -> List[List[int]]:
        if not B:
            return []
        B.sort()
        ans = []
        heap = []
        tmp_right = [0, 0, 0]
        ans.append([B[0][0], B[0][2]])
        heapq.heappush(heap, [-B[0][2], B[0][1]])
        tmp_right = B[0]

        for i in range(1, len(B)):
            heapq.heappush(heap, [-B[i][2], B[i][1]])
            if B[i][0] <= tmp_right[1]:
                if B[i][0] <= B[i-1][1]:  # 前后相交
                    if B[i][2] > B[i-1][2]:
                        ans.append([B[i][0], B[i][2]])
                    elif B[i][2] < B[i-1][2]:
                        height = 0
                        while len(heap):
                            if B[i-1][2] <= -heap[0][0] or heap[0][1] <= B[i-1][1]:
                                heapq.heappop(heap)
                        height = -heap[0][0] or 0
                        ans.append([B[i-1][1], height])
                else:  # 前后不相交
                    if B[i][2] > -heap[0][0]:
                        ans.append(B[i][0], B[i][2])
            else:
                heap = []
                ans.append([tmp_right[1], 0])
            if B[i][1] > tmp_right[1]:
                tmp_right = B[i]

        if B[-1][1] < tmp_right[1]:
            ans.append([tmp_right[0], tmp_right[2]])

        return ans
