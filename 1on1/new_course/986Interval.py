class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not B:
            return []

        res = []
        if A[0][0] > B[0][0]:
            A, B = B, A
        pairs = []
        cur_j = 0
        for i in range(len(A)):
            for j in range(cur_j, len(B)):
                if A[i][1] >= B[j][0] and A[i][0] <= B[j][1]:  # if intersection
                    pairs.append([A[i], B[j]])
                elif A[i][1] < B[j][0]:
                    break

        def merge(pair, res):
            p1 = max(pair[0][0], pair[1][0])
            p2 = min(pair[0][1], pair[1][1])
            res.append([p1, p2])

        for pair in pairs:
            merge(pair, res)

        res.sort()
        return res
