class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0

        for i in range(len(M)):
            for j in range(len(M):
                if j > i:
