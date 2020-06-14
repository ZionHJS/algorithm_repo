class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        if not num:
            return []
        num += "/"
        res = []
        opers = ["+", "-", "*"]
        visited = set()

        # bfs
        # q = [(num[0], "", int(num[0])), ("", num[0], 0)] #cur pending cur_res
        q = [("", "", 0)]
        idx = 0
        while idx < len(num):
            nxt_q = []
            while q:
                cur = q.pop()
                if cur[2] == target:
                    #print("cur:", cur)
                    res.append(cur[0])
                nxt_pd = cur[1]
                if num[idx] != "/":
                    nxt_pd = cur[1] + num[idx]
                    if nxt_pd[0]:
                        nxt_q.append((cur[0], nxt_pd, cur[2]))
                if nxt_pd:
                    for oper in opers:
                        if cur[0]:
                            nxt_str = cur[0] + oper + nxt_pd
                        else:
                            nxt_str = nxt_pd

                        if oper == "+":
                            nxt_sum = cur[2] + int(nxt_pd)
                        elif oper == "-":
                            nxt_sum = cur[2] - int(nxt_pd)
                        elif oper == "*":
                            nxt_sum = cur[2] * int(nxt_pd)
                        nxt_q.append((nxt_str, "", nxt_sum))

            q = nxt_q
            idx += 1

        return res
