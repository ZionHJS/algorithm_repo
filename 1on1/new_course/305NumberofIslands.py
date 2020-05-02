class Solution:
    def numIslands2(self, m: int, n: int, P: List[List[int]]) -> List[int]:
        parents = {(p[0], p[1]): (p[0], p[1]) for p in P}
        #print("old_parents:", parents)
        # find

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        # union
        def union(p, land):
            parents[find((p[0], p[1]))] = find(land)

        ans = []
        lands = set()
        ds = ((-1, 0), (1, 0), (0, -1), (0, 1))
        cur_cnt = 0
        # iteral
        for p in P:
            for i in range(4):
                x_ = p[0]+ds[i][0]
                y_ = p[1]+ds[i][1]
                if (x_, y_) in lands:
                    union(p, (x_, y_))
            lands.add((p[0], p[1]))
            #cur = set(find(x) for x in lands)
            cnt = 0
            for land in lands:
                if parents[land] == land:
                    cnt += 1
            ans.append(cnt)

        return ans
