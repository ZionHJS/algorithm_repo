import random
import bisect
import collections
a = [1, 1, 1, 1, 9, 9, 9, 9, 3, 3, 3, 3, 4, 4, 5, 6, 7]
bisect.insort(a, 2)
print("a:", a)


test = collections.defaultdict(lambda: [])
for key in test:
    print("key_here!")


memo[((1, 2), "abc")] == "target"
print("res:", memo[(1, 2), "abc"])


list = ["aabbcc", "ddeeff", "gghhii"]
tmp = "".join(list)
print("tmp:", tmp)
res1 = set(tmp)
print("res1:", res1)
res2 = collections.Counter(tmp)
print("res2:", res2)

c = collections.Counter()
print("c:", c)
c["a"] = 3, c["b:", 4]
print("c:", c)

rnd = random.randint(1, 2)
print("rnd:", rnd)

rnd = random.randint(0, 1)
print("rnd:", rnd)

idx = 0
if idx:
    print("if words")
else:
    print("not work")


str1 = "aavvccsdef"
cnt = collections.Counter(str1)
print("cnt:", cnt)


s = "abcdefghijk"
res_s = bisect.bisect_right(s, "d")
print("res_s:", res_s)
list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
res_l = bisect.bisect_right(list, "d")
print("res_list:", res_l)


nums = [1, 3, 2, 2, 5, 2, 3, 7]
dic = collections.Counter(nums)
print("dic:", dic)


preorder = [3, 9, 20, 15, 7]
print("preorder_last:", preorder[-3:-1])


pop = preorder.pop(0)
print("pop:", pop)
print("preorder:", preorder)


s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
s.add(6)
print("s:", s)
list_s = list(s)
print("list_s:", list_s)

inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
print("postorder:", postorder[-4:-1])

inorder = [9, 3, 15, 20, 7]
str_inorder = str(inorder)
print("str_inorder:", str_inorder)
list_inorder = list(str_inorder)
print("list_inorder:", list_inorder)

list1 = [1, 2, 1]
list2 = [1, 2, 1]
print("equalOrNot:", list1 == list2)

num = 232
print("char_num:", chr(num))

test_list = [1, [4, [6]], [1, 1], 2, [1, 1]]
test_list = [4, [6]]
ordered = test_list[::-1]
print("ordered:", ordered)
print("test_list:", test_list)

num1 = 2
num2 = 4
num3 = 7
print("%1:", num1//3)
print("%2:", num2//3)
print("%3:", num3//3)

s = "loveleetcode"
c = "e"
print("idx:", s.index(c))

tmp_list = []
print("tmp:", tmp_list[-1])

pop = -3
tmp = 2
print("res:", pop/tmp)


string1 = "leetcode"
list_str1 = list(string1)
list_str1.sort(cmp=lambda x, y: x < y)
string2 = "codeeelt"
list_str2 = list(string2)
list_str2.sort()
print("list_str1:", list_str1)
print("list_str2:", list_str2)

list = [1, 2, 3, 4, 5, 6, 7, 8]
for i, num in enumerate(list):
    print("i:", i, "num:", num)

str_num = "2*3-4*5"
int_str = int(str_num)
print("int_str:", int_str)

num = 1e9
print("is_digit:", int(num))

s = set()
tu = (1, 2)
tu2 = (3, 4)
s.add(tu)
print("s:", s)
print("bollean:", tu2 not in s)

i = 1
print("%:", i//2)


s = set()
s.add((1, 2))
if (1, 2) in s:
    print("in here!")

list = [(1, 2), (1, 2), (5, 6)]
s_list = set(list)
print("s_list:", s_list)
list_s = list(s_list)
print("list_s:", list_s)

s = "abcdefghijk"
res = bisect.insert(s, "d")
print("res:", res)


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [3, 4, 5, 6, 7, 8, 9, 10, 11]
str_list = str(list1)
print("str_list:", str_list)


union_list = list1.union(list2)
print("union_list:", union_list)

string = ""
res = string+str(3)
print("res:", res)

print("tes:", 2 % 3)
print("test2:", 5 % 3)


memo = [[1, 2], [3, 4], [5, 6]]
for i, j in memo:
    print("i:", i, "j:", j)


a = {'a': 9, 'b': 1, 'c': 5}
l = len(a)
print("length:", l)


wordDict = ["catsss", "cat", "andsss", "sandss", "dogssss"]
print("min:", min(wordDict))

temp = ""
print("res:", temp[1:])

dicts = {1: "a", 2: "b", 3: "c"}
res = dicts.get
print("get:", res)


str1, str2 = "ab", "abc"
print("str2-str1:", str1 in str2)

strs = "sdfasdbasd"
test = strs.split(",")
print("test:", test)

for i in range(10):
    print("i:", i)
    for j in range(10):
        print("j:", j)
        if j == 3:
            break

cor = [1, 0]
val = 1
print("equal_1:", cor == val)
print("equal_2:", cor[0] == val)
print("exist:", val[0])

s = set()
s.add((1, 2))
s.add((3, 4))
s.add((5, 6))
s.add((1, 2))
s.add((5, 6))
print("s:", s)
print("length:", len(s))
s2 = set()

if s and s2:
    print("both!")
elif s or s2:
    print("only!")

s_list = list(s)
print("s_list:", s_list)


hits = [(0, 0)] * 3
print("hits:", hits)
print("%:", 299 % 300)

a = ["a", "b", "c"]
b = ["e", "f", "g"]
print("combine1:", a + b)
c = a.append(b)
print("append:", c)
print("com:", a += b)


x = {'a': [1, 2], 'b': [3, 4, 6]}
y = {'b': [2, 3, 5, 6, 7], 'c': 4}
z = x.copy()
z.update(y)
#o = {**x, **y}
print("com_z:", z.update(y))
print("com_o:", o)


x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

x = {'a': [1, 2], 'b': [3, 4, 6, 9, 10]}
y = {'b': [2, 3, 5, 6, 7], 'c': 4}
z = x.copy()
z.update(y)

print("z:", z)
print("o:", o)


chars = "abcdefghijklmnopqrstuvwxyz"
print("length:", len(chars))

a = [0, 1, 1, 0]
for i, val in enumerate(a):
    print("i:", i, "val", val)


set1 = set((1, 3))
set2 = set((2, 4))
inter = set1.intersection(set2)
print("inter:", inter)
union = set1.union(set2)
print("union:", union)

p1 = (9, (1, 3))
p2 = (12, (3, 5))
print("p1:", p1)
s = set()
s.add(p1)
s.add(p2)
print("s:", s)

p1 = (9, (1, 3))
p2 = (12, (3, 5))
print("p1:", p1)
list = []
list.append(p1)
list.append(p2)
print("list:", list)
list.sort(key=lambda x: x[0], reverse=True)
print("sort_list:", list)
list.remove((9, (1, 3)))
print("new_list:", list)


list = [1, 2, 3, 34, 5, 5]
sums = sum(list)
print("sums:", sums)

rnd = random.randint(1, 2)
print("rnd:", rnd)


S = "abcdebddebde", T = "bde"
print("inornot:", T in S)

print("inornot:", (1 or 2 or 3 or 4) == 4)

s = "abc"
print("exist:", s[3:])

s = "123456789"
print("ord_s_i:", ord("1"))

print("res:", 1//3)

str = "123456789"
print("reverse:", str[::-1])


list = [2, 9, 3, 5, 4, 6, 8, 1]
list.sort(reverse=True)
print("sort_True:", list)


a = "asdfghkju"
la = list(a)
print("list:", la)
a.sort()
print("sorted:", a)

a = [1, 2, 3, 4]
b = [3, 2, 4, 1]
c = [1, 2, 3, 4]
print("equal:", a == b)
print("equal:", a == c)

list = [["JFK", "SFO"], ["JFK", "ATL"]]
print("list:", list)
list.sort()
print("list:", list)

a = "abcdef"
print("statOrnot:", a.startswith("abc"))

a = "efghjkl"
b = "egk"
if b in a:
    print("in")
else:
    print("notIn")


dp = {'a': 1, 'b': 1, 'ba': 2, 'bca': 3, 'bda': 3, 'bdca': 4}
print("max_val:", max(dp.values()))
print("max_key:", max(dp.keys()))

tmp = []
print("max:", max(tmp))

list = ["a", "b", "c"]
print("str:", str(list))

a = []
a.append("")
print("a:", a)

a = "eftg"
b = "uil"
zip_ = zip(a, b)
print("zip_:", zip_)
for pair in zip_:
    print("pair:", pair)

a = "aabbcc"
res = set(a)
print("res:", res)

list = ["aabbcc", "ddeeff", "gghhii"]
tmp = "".join(list)
print("tmp:", tmp)
res1 = set(tmp)
print("res1:", res2)
res2 = collections.Counter(tmp)
print("res2:", res2)


res = set("".join(list))
print("res:", res)


res = "abcdef"
re1 = res*1
print("re1:", re1)
re2 = res*0
print("re2:", re2)

word = "abcdfsaaa"
s_w = set(word)
print("s_w:", s_w)

memo = {}
memo[((1, 2), "abc")] = "target"
print("res:", memo[(1, 2), "abc"])
print("check:", memo["abc"])

memo = {}
memo[(1, 2, "abc")] = "target"
print("res:", memo[(1, 2, "abc")])

memo = {}
memo["a"] = "target"
print("res:", memo["a"])

a = [1, 2, 3]
b = [4, 5, 6]
print("+:", a+b)

a = 5
print("divide:", a/2)

s = -1
str_s = str(s)
print("str_s:", str_s)


s = [-1]
e = [-3, -4, -5]
print("sum:", s+e)

a = 3
l_a = list(a)
print("l_a:", l_a)


l = ["izw", "ironman", "i love leetcode", "island", "iwo"]
l.sort()
print("l:", l)

s1 = "i love leetcode"
s2 = "ironman"
print("largert?:", s1 < s2)

for i in range(10)[::-1]:
    print("i:", i)

a = [[1], [2], [3]]
b = [[4]]
c = a+b
print("c:", c)

print("res:", 11//3)

a = "abcdfg"
print("left:", a[:-0])

cur = ['This    ', 'is    ', 'an']
res1 = "".join(cur)
res2 = str(cur)
print("res:", res1)
print("res2:", res2)

print("tmp:", 3 % 1)


s = set()
print("len_s:", len(s))

pq = [3, 3, 3, 4, 5, 5, 6, 2, 2, 2]
pq.remove(3)
print("pq:", pq)

a = "abasdads"
list_a = list(a)
print("list_a:", list_a)

s = "aaaabbbbcdefgdddccchjklmn"
cnt = s.count("esd")
print("cnt:", cnt)
new_s = s.split("e")
print("new_s:", new_s)


s_s = set(s)
print("set:", s_s)

t = "1+2*3"
print("t:", t)
new_t = int(t)
print("new_t:", new_t)

op1 = 3
op2 = 5
f = {"+": +, "-": -, "*": *, "/": / }
print("res:", op1f["*"]op2)

t = "1+2*3+(5*7)"
res = eval(t)
print("res:", res)

t = ["4", "13", "5", "/", "+"]
res = [t]*2
print("res:", res)

a = "abcdef"
a_ = a[::-1]
print("a_:", a_)

i = 5
for j in range(i)[::-1]:
    print("j:", j)

a = "# a # b # a # a # b # a #"
b = a.split("#")
print("b:", b)

a = "-"
b = "sfg"
c = a.join(b)
print("c:", c)

a = [1, 1, 1, 1, 3, 3, 3, 3, 4, 4, 5, 6, 7]
bisect.insort(a, 2)
print("a:", a)


for i in range(10, -1, -1):
    print("i:", i)


dic = {}
if not dic:
    print("not inside!")
else:
    print("dict")

print("here!")


r1 = 3/2
r2 = 9/6
r3 = 7/5
print("r1:", r1, "r2:", r2, "r3:", r3)
print("equal:", r1 == r2, "notequal:", r3 == r1)

a = [(1, 2), (3, 4), (5, 6)]
s = set(a)
print("s_1:", s[1])

print("s:", s)
if (5, 2) in s:
    print("in here!")

a = [[1, 2], [3, 4], [5, 6], []]
print("a:", a)
print("a[3]:", a[3])
