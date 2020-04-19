class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dic = defaultdict(lambda: [])
        for point in points:
            dic[point[0]].append(point)

        def ratio(p1, p2):
            if p1[1]-p2[1] == 0:
                return 1e9
            elif p1[0]-p2[0] == 0:
                return -1e9
            return (p1[1]-p2[1])/(p1[0]-p2[0])

        keys = list(dic.keys())
        ans = 0
        keys.sort()
        print("keys:", keys, "dic:", dic)
        prevs = []
        lines = defaultdict(lambda: [])
        for key in keys:
            ans = max(ans, len(dic[key]))
            if not prevs:
                prevs = dic[key]
                continue
            else:
                for point in dic[key]:
                    for prev in prevs:
                        cur_ratio = ratio(prev, point)
                        if not lines[cur_ratio]:
                            lines[cur_ratio] += [prev, point]
                        else:
                            print("cur_ratio:", cur_ratio,
                                  "lines_cur_ratio:", lines[cur_ratio])
                            if prev == lines[cur_ratio][-1]:
                                lines[cur_ratio].append(point)
                        ans = max(ans, len(lines[cur_ratio]))
                prevs += dic[key]

        return ans
