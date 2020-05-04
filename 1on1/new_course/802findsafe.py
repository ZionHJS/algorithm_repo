import queue


class Solution:
    def eventualSafeNodes(self, G: List[List[int]]) -> List[int]:
        edges = defaultdict(lambda: [])
        nodes = set()
        memo = defaultdict(lambda: True)

        for i in range(len(G)):
            nodes.add(i)
            for j in range(len(G[i])):
                edges[i].append(G[i][j])
                nodes.add(G[i][j])
        ans = []
        for node in nodes:
            if node not in edges:
                ans.append(node)
                continue
            if memo[node]:
                q = queue.Queue()
                q.put(node)
                visited = set()
                valid = True
                while valid:
                    n = len(q)
                    for i in range(n):
                        cur = q.get()
                        visited.add(cur)
                        for nxt in edges[cur]:
                            if nxt in visited:
                                memo[cur] = False
                                memo[node] = False
                                valid = False
                                break
                            q.append(nxt)
                        if not valid:
                            break

        return sorted(ans)
