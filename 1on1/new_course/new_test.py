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

a = -1
if a:
    print("A")

a = set([1, 2])
a.add(3)
print("a:", a)


[[6], [4], [9], [5], [1, 5], [3, 4, 6], [0, 5, 10], [8, 9, 10], [7], [2, 7], [6, 7]]

even = [1 if True, 2 if True, 3 if True, 4 if False]
print("even:", even)

nxt = False
new = !nxt
print("new:", new)

a = [1, 2, 3, 4, 5, 6]
b = a
b.pop()
print("a:", a)

cur = 3
if cur != (1 and 2):
    print("!=")

a = "abcdefghjklmn"
b = "abcdef"
c = "cdefghj"
if b in a:
    print("b in a!")
if c in a:
    print("c in a!")

r1 = True
r2 = True
if not r1 and not r2:
    print("both not")
elif r1:
    print("r1")
elif r2:
    print("r2")

a = []
b = [1, 2, 3, 4, 5]
c = [6, 7, 8, 9]
a.append(b)
a.append(c)
print("a:", a)
e = [1, 2, 3, 4, 5]
if e in a:
    print("can't add repeatly")
f = set()
g = tuple(b)
print("g:", g)
f.add(g)
print("f:", f)

a = tuple((1, 2, 3))
b = tuple((4, 5, 6))
print("+:", a+b)

a = "09"
print(int(a))

for i in range(9, 0, -1):
    print("i:", i)

d = {}
idx = 3
cur = [1, 2, 4]
d[(idx, tuple(cur))] = True

print("d:", d)

a = [1, 2, 3, 4, 5, 6]
t = set()
t.add(a)
print("t:", t)

a = "000"
b = int(a)
print("b:", b)

s = [[]]
if not s:
    print("not s!")
else:
    print("S!")

print(6 % 10)

a = "0"*10
print("a:", a)

for i in range(10)[::-1]:
    print("i:", i)

oper = -
print("oper:", oper)

a = "  13  "
print(int(a))

str = "   "

if not str:
    print("not!!!")

print(int(str))

str = "12+34"
print(int(str))

str = "-223"
print(int(str))

a = "" + 2
print("a:", a)

target = 3
a = 1.5
print(a*2 == target)

print(1 % 2)

a = 3
b = 2
print(a *= b+1)

print(1.5 % 1)

map = {}
if not map:
    print("empty!")

ladder = [set()]
ladder.append(set())
ladder[1].add(3)
print("ladder:", ladder)

cur_num = ""
cur_num += 3
print("cur_num:", cur_num)

a = "-2342"
print(int(a))

a = "ebcdc"
b = "eabcd"
print(min(a, b))

s = "abcd"
s = s[:-1]
print(s)

res = "z"*len(s)
print(res)
nxt_s = s[4:]
print("nxt_s:", nxt_s)

a = "c"
b = "c"
print(min(a, b))
