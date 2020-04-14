import collections
import heapq


class AutocompleteSystem:
    def __init__(self, S: List[str], T: List[int]):
        self.S = S
        self.T = T
        self.degree = collections.defaultdict(lambda: 0)
        for i in range(len(S)):
            self.degree[S[i]] = T[i]
        self.s = set(S)
        self.tmp_his = ""

    def input(self, c: str) -> List[str]:
        #print("degree:", self.degree)
        if c == "#":
            if not self.tmp_his:
                return []
            self.s.add(self.tmp_his)
            self.degree[self.tmp_his] += 1
            res = self.tmp_his
            self.tmp_his = ""
            return [res]
        else:
            self.tmp_his += c
            heap = []
            for s in self.degree:
                if s.startswith(self.tmp_his):
                    if len(heap) < 3:
                        if heap and self.degree[s] == heap[0][0]:
                            if heap[0][1] > s:
                                tmp = heapq.heappop(heap)
                                heapq.heappush(heap, (self.degree[s], s))
                                heapq.heappush(heap, tmp)
                        heapq.heappush(heap, (self.degree[s], s))
                    elif len(heap) == 3:
                        if self.degree[s] == heap[0][0]:
                            if heap[0][1] > s:
                                heapq.heappop(heap)
                                heapq.heappush(heap, (self.degree[s], s))
                        elif self.degree[s] > heap[0][0]:
                            heapq.heappop(heap)
                            heapq.heappush(heap, (self.degree[s], s))
            #print("heap:", heap)

            res = []
            for i in range(3):
                if heap:
                    res.append(heapq.heappop(heap))
                else:
                    break
            res.sort(reverse=True)
            res = list(filter(lambda x: x[0], res))
            return res
