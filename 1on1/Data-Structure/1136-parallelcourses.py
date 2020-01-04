import heapq


class Solution(object):
    def minimumSemesters(self, N, relations):
        if not relations:
            return -1

        semesters = [[] for _ in range(N)]
        relations_dic = {}

        for i in range(N):
            if not relations_dic.has_key(i):
                relations_dic[i] = []
            for j in range(len(relations)):
                relations_dic[i].append(relations[j][0])

            for y in relations:
                if y[1] in relations_dic[i]:
                    relations_dic[i].remove(y[1])

                for z in range(len(relations)):
                    if relations[z][0] in relations_dic[i]:
                        relations_dic[i+1] = []
                        relations_dic[i+1].append(relations[z][1])
                        relations.pop(z)

        print(relations_dic)
        if relations:
            return -1

        return len(relations_dic)


list = ['abc', 'def', 'hij', 'klm', [1, 2], [2, 3]]
for x in list:
    list.remove(x)

print(list)

N = 10
semesters = [[] for _ in range(N)]
print(semesters)
semesters[2].append(3)
semesters[2].append(4)
semesters[2].append(5)
print(semesters)
for o in semesters:
    if o == []:
        semesters.remove(o)
print(semesters)
for o in semesters:
    if o == []:
        semesters.remove(o)
print(semesters)
for o in semesters:
    if o == []:
        semesters.remove(o)
print(semesters)
for o in semesters:
    if o == []:
        semesters.remove(o)
print(semesters)


dic = {2: [1], 3: [3], 'a': [4]}
print(dic)
dic['a'].remove(4)
print(dic['a'])
print(dic)
print(len(dic))
