class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        if not num:
            return []
        num += "//"
        res = set()
        opers = set(["+", "-", "*"])
        visited = set()

        # bfs
        q = [("", "", 0)]  # str pd prev_pd prev_oper sum
        idx = 0
        while idx < len(num):
            nxt_q = []
            while q:
                cur = q.pop()
                if cur[2] == target and cur[0] and ((idx == len(num)-2 and not cur[1]) or (idx == len(num)-1)):
                    res.add(cur[0])
                nxt_pd = cur[1]
                if num[idx] != "/":
                    nxt_pd += num[idx]
                    if nxt_pd[0] != "0":
                        nxt_q.append((cur[0], nxt_pd, cur[2]))
                if nxt_pd:
                    if cur[0]:
                        for oper in opers:
                            nxt_str = cur[0] + oper + nxt_pd
                            nxt_sum = cur[2]
                            if oper == "+":
                                nxt_sum += int(nxt_pd)
                            elif oper == "-":
                                nxt_sum -= int(nxt_pd)
                            elif oper == "*":
                                jdx = len(cur[0])-1
                                while jdx > 0 and cur[0][jdx] not in set(["+", "-"]):
                                    jdx -= 1
                                tail = cur[0][jdx:]
                                tail_sum = 1
                                tmp = ""
                                for i in range(len(tail)+1):
                                    if i < len(tail) and tail[i].isdigit():
                                        tmp += tail[i]
                                    elif i == len(tail) or tail[i] == "*":
                                        tail_sum *= int(tmp)
                                        tmp = ""
                                if jdx == 0:
                                    nxt_sum = tail_sum*int(nxt_pd)
                                elif cur[0][jdx] == "+":
                                    nxt_sum -= tail_sum
                                    nxt_sum += tail_sum*int(nxt_pd)
                                elif cur[0][jdx] == "-":
                                    nxt_sum += tail_sum
                                    nxt_sum -= tail_sum*int(nxt_pd)

                            nxt_q.append((nxt_str, "", nxt_sum))
                    else:
                        nxt_str = nxt_pd
                        nxt_sum = int(nxt_str)
                        nxt_q.append((nxt_str, "", nxt_sum))

            q = nxt_q
            idx += 1

        return list(res)
