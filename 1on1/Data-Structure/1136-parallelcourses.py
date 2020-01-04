import heapq


class Solution(object):
    def minimumSemesters(self, N, relations):
        if not relations:
            return -1

        relations_dic = {}
        semesters_dic = {}

        for i in range(len(relations)):
            relations_dic[relations[i][0]] = relations[i][1]

        for i in range(N):
            if not len(relations):
                break

            if not semesters_dic.has_key(i):
                semesters_dic[i] = []

            for key in relations_dic.keys():
                semesters_dic[i].append(key)

            for key in relations_dic.keys():
                if relations_dic[key] in semesters_dic[i]:
                    semesters_dic[i].remove(relations_dic[key])  # 只删得到一个

            for key in relations_dic.keys():
                if key in semesters_dic[i]:
                    if not semesters_dic.has_key(i+1):
                        semesters_dic[i+1] = []
                    semesters_dic[i+1].append(relations_dic[key])
                    del relations_dic[key]

        print(semesters_dic)
        if len(relations_dic):
            return -1

        for key in semesters_dic.keys():
            if not semesters_dic[key]:
                del semesters_dic[key]
        print(semesters_dic)

        return len(semesters_dic)


list = ['abc', 'def', 'hij', 'klm', [1, 2], [2, 3]]
for x in list:
    list.remove(x)

print(list)

N = 10
semesters = [[] for _ in range(N)]
print(semesters)
# semesters[9].append(3)
# semesters[9].append(4)
# semesters[9].append(5)
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
print(len(dic))
del dic[2]
del dic[3]
del dic['a']
print(len(dic))


list = []

if not list:
    print('je')


queue = [[x, 1] for x in range(10)]
print(queue)
