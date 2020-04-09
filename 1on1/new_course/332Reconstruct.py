class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        if not tickets:
            return []

        tickets.sort()
        res = []

        def dfs(dt, cur_t, rest_t):
            nonlocal tickets, res
            if len(cur_t) == len(tickets)+1 or len(rest_t) == 0:
                res = cur_t
                return True

            for i in range(len(rest_t)):
                if rest_t[i][0] == dt:
                    cur_t.append(rest_t[i][1])
                    nxt_t = rest_t[:i] + rest_t[i+1:]
                    if dfs(rest_t[i][1], cur_t, nxt_t):
                        return True
                    cur_t.pop()

            return False

        dfs("JFK", ["JFK"], tickets)
        return res
