import queue


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        g = collections.defaultdict(list)

        for a, b in connections:
            g[a].append(b)
            g[b].append(a)

        low = [0] * n

        def dfs(level, cur, parent):
            low[cur] = level
            ans = []
            for child in g[cur]:
                if child == parent:
                    continue

                if low[child] == 0:
                    ans += dfs(level + 1, child, cur)
                # update the cur_node level to lowest it can
                low[cur] = min(low[cur], low[child])
                if low[child] > level:  # ans changes here!
                    ans.append([child, cur])

            return ans

        return dfs(1, 0, -1)  # return ans
