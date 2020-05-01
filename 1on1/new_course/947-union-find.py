class Solution:
    def removeStones(self, S: List[List[int]]) -> int:
        def find(x):  # typical find(x)
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):  # where is the rank union(x, y) all together then we can judge if two point are in same
            parents[find(x)] = find(y)

        parents = list(range(20000))  # x=>0~9999 y=>10000~19999

        for i, j in S:
            union(i, j+10000)
            #union(i, j)

        return len(S) - len(set(find(x) for x, y in S))
