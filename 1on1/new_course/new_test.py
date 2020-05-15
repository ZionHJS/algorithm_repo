import itertools
import collections

A = [[1, 2], [3, 4], [5, 6, 0, 1], [7, 8, 9]]
print("a-product:", itertools.product(A))
for a in itertools.product():
    print("a:", a)

M = [0, 1, 2, 3]
for o in itertools.combinations(M, 3):
    print("o:", o)

c = collections.defaultdict(list)
S = "abcde"
for i, char in enumerate(S):
    c[char].append(i)
print("c:", c)

a = [1, 2, 3, 4, 5, 6]
print("res:", itertools.product(*a))

a = "e"
s = a.split(",")
print("s:", s)

b = "{a,b}{c,{d,e}}"
print("s:", b.split("},"))

props = []
a = props.pop()
print("a:", a)

stack = [""]
print("len:", len(stack))

stack = [[]]
print("stack:", stack)


a = ["ncaa", "ncaaiawn", "ncaaown", "ncaaxwn", "ncaer", "ncaia", "ncao", "ncaw", "ncax", "ngaa", "ngaaiawn", "ngaaown", "ngaaxwn", "ngaer", "ngaia", "ngao", "ngaw", "ngax", "nhaa", "nhaaiawn", "nhaaown", "nhaaxwn",
     "nhaer", "nhaia", "nhao", "nhaw", "nhax", "njaa", "njaaiawn", "njaaown", "njaaxwn", "njaer", "njaia", "njao", "njaw", "njax", "nlaa", "nlaaiawn", "nlaaown", "nlaaxwn", "nlaer", "nlaia", "nlao", "nlaw", "nlax"]

b = ["ncaaiawn", "ncaan", "ncaaown", "ncaaxwn", "ncaern", "ncaian", "ncaon", "ncawn", "ncaxn", "ngaaiawn", "ngaan", "ngaaown", "ngaaxwn", "ngaern", "ngaian", "ngaon", "ngawn", "ngaxn", "nhaaiawn", "nhaan", "nhaaown", "nhaaxwn",
     "nhaern", "nhaian", "nhaon", "nhawn", "nhaxn", "njaaiawn", "njaan", "njaaown", "njaaxwn", "njaern", "njaian", "njaon", "njawn", "njaxn", "nlaaiawn", "nlaan", "nlaaown", "nlaaxwn", "nlaern", "nlaian", "nlaon", "nlawn", "nlaxn"]

a = set()
a.add("b")
c = ["a", "b"]
c.append(a)
print("a:", a)


c = ["a", "b", "c"]
if c.index("d"):
    print("try_find:")

row = [1, 2, 3, 4, 5, 6, 7, 8]
mid = int(len(row)/2)
print("mid:", mid)

a = [""]
if a:
    print("is a")
else:
    print("a-false!")

for i in range(10, 3):
    print("bigger?")

s = "abcde"
if "acd" in s:
    print("it is in!")

c = defaultdict(list)
S = "abcde"
for r, i in enumerate(S):
    c[i].append(r)
print("c:", c)

a = bin(0)
b = bin(1)
c = bin(2)
d = bin(3)
f = bin(4)
print("a:", a, "b:", b, "c:", c, "d:", d, "f:", f)
5
for i in range(10, -1, -1):
    print("i:", i)

a = set()
if a:
    print("A!")
else:
    print("not A")

a = bin(1)
print("a:", a)

a = "(let x 2 (mult x (let x 3 y 4 (add x y))))"
b = a.replace(")", " )").replace("(", "( ").split()
print("b:", b)

memo = set()
q = []
q.append((1, 0))
q.append((2, 0))
q.append((3, 0))
tq = tuple(q)
memo.add(tq)
q.append((3, 0))
tq2 = tuple(q)
memo.add(tq2)
print("memo:", memo)


memo = set()
q = set()
q.add((1, 2))
q.add((2, 3))
memo.add(q)
print("memo:", memo)

for i in range(10)[::-1]:
    print("i:", i)

O = [1]
print("exsit or not:", O[:-1])

M = [[0, 1], [1, 0]]
for o in combinations(M, 3):
    print("o:", o)


print("res:", 1//2)

a = "1*2*4*6*7"
print("a:", int(a))

a = 0
if 0 <= a <= 0:
    print("exist")
if 0 <= a < 0:
    print("exist too")

a = "3"
print("torf:", a.isdigit())

for i in range(100)[1::3]:
    print("i:", i)


pc = set()
pc.add((1, 2))
print("pc:", pc)
pc.remove((1, 2))
print("pc:", pc)

s1 = set()
s1.add(1)
s1.add(2)
s2 = set()
s2.add(3)
s2.add(4)
s2.add(1)
print("union:", s1.union(s2))

s = set()
if not s:
    print("not!")


memo = set()
midx = 0
cidx = 1
visited = (2, 3, 4, 5, 6)
memo.add((midx, cidx, visited))
print("memo:", memo)

visited = set()
visited.add(1)
visited.add(2)
visited.add(3)
print("visited:", visited)
memo = set()
memo.add(tuple(visited))
print("tuple:", memo)


m = set()
c = set()
T = False

m.add(1) if T else c.add(2)

print("m:", m, "c:", c)
