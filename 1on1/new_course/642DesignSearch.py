import collections


class AutocompleteSystem:
    def __init__(self, S: List[str], T: List[int]):
        self.S = S
        self.T = T
        self.degree = collections.defaultdict(lambda: 0)
        for i in range(len(S)):
            self.degree[S[i]] = T[i]
        self.tmp_his = ""

    def input(self, c: str) -> List[str]:
        if c == "#":
            if not self.tmp_his:
                return []
            self.degree[self.tmp_his] += 1
            self.tmp_his = ""
        else:
            self.tmp_his += c
            q = []
            for s in self.degree:
                if s.startswith(self.tmp_his):
                    q.append((self.degree[s], s))
            if not q:
                return q
            q.sort(key=lambda x: x[0], reverse=True)
            tmp_list = []
            res = []
            prev_key = q[0][0]
            for i in range(len(q)+1):
                if i == len(q) or q[i][0] != prev_key:
                    tmp_list.sort()
                    res += tmp_list
                    if len(res) >= 3 or i == len(q):
                        return res[:3]
                    tmp_list = []
                tmp_list.append(q[i][1])
                prev_key = q[i][0]

            return res[:3]
