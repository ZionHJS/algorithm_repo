import queue


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0

        graph = {}
        res = []
        visited_s = set()
        #circle_count = 0

        # build the graph
        for i in range(len(M)):
            graph[i] = []
            for j in range(len(M)):
                if M[i][j] == 1 and i != j:
                    graph[i].append(j)
        # print(graph)

        # loop the bfs   p => person
        for p in range(len(M)):
            #print('k:', k)
            if p not in visited_s:
                self.bfs(graph, p, res, visited_s)

        return len(res)

    def bfs(self, graph, stu, res, visited_s):
        q = queue.Queue()
        s = set()
        q.put(stu)

        while q.qsize():
            cur_stu = q.get()
            s.add(cur_stu)
            if graph[cur_stu]:
                for friend in graph[cur_stu]:
                    if friend not in s:
                        q.put(friend)

        res.append(s)
        for item in s:
            if item not in visited_s:
                visited_s.add(item)


res = []
s1 = set()
s1.add(0)
s1.add(1)
s1.add(2)
s1.add(3)
res.append(s1)

s2 = set()
s2.add(4)
s2.add(5)
s2.add(6)
s2.add(7)
# res.append(s2)
for item in s2:
    print('item:', item)

print('res is:', res)
print('length res:', len(res))
