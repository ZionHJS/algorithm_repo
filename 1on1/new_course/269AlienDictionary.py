import collections
import queue


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # 先把整个words转换成一个长字符串 在用"".join(string) => ["a", "b", "c" ...]
        chars = set("".join(words))
        degrees = {x: 0 for x in chars}
        graph = collections.defaultdict(lambda: [])

        for pair in zip(words, words[1:]):
            # for x, y in zip(*pair):
            for x, y in zip(pair[0], pair[1]):
                if x != y:
                    graph[x].append(y)
                    degrees[y] += 1
                    break

        #stack = filter(lambda x: degrees[x] == 0, degrees.keys())
        # bfs()
        print("degrees:", degrees)
        print("graph:", graph)
        res = ""
        q = queue.Queue()
        for key in degrees:
            if degrees[key] == 0:
                q.put(key)
        if not len(graph) and q.qsize() > 1:
            print("here")
            return ""
        while q.qsize():
            x = q.get()
            res += x
            for y in graph[x]:
                degrees[y] -= 1
                if degrees[y] == 0:
                    q.put(y)

        return res * (set(res) == chars)
