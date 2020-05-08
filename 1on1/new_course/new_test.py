import itertools
import collections

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
