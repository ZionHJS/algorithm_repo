class Solution:
    def minTransfers(self, T: List[List[int]]) -> int:
        #graph = collections.defaultdict(lambda:0)
        B = collections.defaultdict(lambda: 0)

        cnt = 0
        for t in T:
            B[t[0]] -= t[2]
            B[t[1]] += t[2]
        # filter
        cnt_map = collections.defaultdict(lambda: 0)
        for p in B:
            cnt_map[B[p]] += 1

        for c in cnt_map:
            if cnt_map[c] != 0 and -c in cnt_map:
                if cnt_map[-c] >= cnt_map[c]:
                    cnt += cnt_map[c]
                    cnt_map[-c] -= cnt_map[c]
                    cnt_map[c] = 0
                else:
                    cnt += cnt_map[-c]
                    cnt_map[c] -= cnt_map[-c]
                    cnt_map[-c] = 0

        #print("cnt_map:", cnt_map)

        return cnt
