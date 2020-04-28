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


class Solution:
    def minTransfers(self, T: List[List[int]]) -> int:
        #graph = collections.defaultdict(lambda:0)
        def bfs(non_zero):
            # remove one non_zero_clique
            n = len(non_zero)
            q = collections.deque()
            q.append(([0], non_zero[0]))
            min_zero_set = None

            while q:
                cur_set, cur_sum = q.popleft()
                if cur_sum == 0:
                    min_zero_set = cur_set
                    break
                for j in range(cur_set[-1]+1, n):
                    #print("cur_set+[j]:", cur_set+[j])
                    q.append((cur_set+[j], cur_sum+non_zero[j]))

            #print("min_zero_set:", min_zero_set)
            min_zero_set = set(min_zero_set)
            return [non_zero[i] for i in range(n) if i not in min_zero_set]

        # build the Balancemap
        B = collections.defaultdict(lambda: 0)
        for t in T:
            B[t[0]] -= t[2]
            B[t[1]] += t[2]

        # filter
        non_zero = [B[k] for k in B if B[k] != 0]
        cnt = len(non_zero)
        while len(non_zero) > 0:
            non_zero = bfs(non_zero)  # remove one non_zero_clique
            cnt -= 1

        return cnt
