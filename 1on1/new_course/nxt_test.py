import bisect
import re
review = "I love anacell Best, services; Best services. provided by anacell"
review = re.sub(r"[^a-z0-9 ]", "", review.lower())
print("review:", review)
print("s-review:", review.split(" "))


nums = [1, 1, 1, 2, 7, 9]
print(bisect.bisect_left(nums, 2))

roses = [1, 2, 4, 9, 1, 3, 4, 1]
idx = 0
while idx < len(roses):
    idx = bisect.bisect_left()

words = "Anacell provides the best services in the city"
word = "abcdefghijklmnopqrstuvwxyz"
idx = bisect.bisect_left(word, "km")
print("idx:", idx)


a = "bfcde"
idx = bisect.bisect_left(a, "f")
print("idx:", idx)
idx2 = bisect.bisect_left(a[:idx], "f")
print("idx2:", idx2)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s = set()
ta = tuple(a)
print("ta:", ta)
s.add(ta)
print("s:", s)

n = [0]
N = n[:0] + n[1:]
print("N:", N)

a = [1, [3, [4], [5]]]


str2 = "123 sjhid dhi"
list2 = str2.split()  # or list2 = str2.split(" ")
print list2


def power(x, n=2):
    s = 1
    while n > 0:
        n = n-1
        s = s*x
    return s


print(power(5))

print("2**30:", 2**30)

print(1//2)

a = "abcdefg"
b = "hjklmn"
for (x, y) in zip(a, b):
    print("x,y:", (x, y))

c = "abc"
d = "abca"
print(c > d)
print(d > c)

str = "banana"
print("ana" in str)

str = "1"*10
print("str:", str)

a = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
for row in a:
    row = "".join(row)
    print("row:", row)
print("a:", a)

a = "1+4*2"
print(a[4:-2])
print(a[1:-2])
print(a[4:-2])


print(int(a))

pld = "abcdef"
print("pld:", pld[::-1])

a = ""
a += str(1)
print("a:", a)

for i in range(11, 1):
    print("i:", i)

words = "Anacell provides the best services in the city"
# words_split = words.split(" ")
# print("words_split:", words_split)
a = set(words)
print("a:", a)

words = "Anacell provides the best services in the city"
print("words", words.lower())

word = "Anacell"

words = "Anacell provides the best services in the city"
idx = bisect.bisect_left(" ")
print("idx:", idx)

for i in range(10)[::-1]:
    print("i:", i)


i = 10

for j in range(i+1, i+1):
    print("jk:", j)

print("j:", j)

strg = "a#b#c#d#e#f"
strg = strg.replace("#", "")
print("strg:", strg)

name = "Bob"
print(name.lower())

A = "abcd"
print("min_is:", min(A))

res = "a"*10
print("res:", res)

print("4321" > "3421")

nxt_words = [""]
head = "head"
res = []
for word in nxt_words:
    res.append(head + " " + word)
print("res:", res)

keyboard = "adbcdefghijkldmnopqrstduvwxyz"
print(keyboard.find("d"))

for i in range(100):
    print("i:", i)
    cur = i
    while i < cur+3:
        i += 1

a = [[1, 2], [3, 4], [7, 8]]
t = tuple(a)
s = set()
print("a:", a, "t:", t)
s.add(t)
print("s:", s)

c = "3"
print("int:", int(c) == 3)

A = [[1, 2], [3, 4], [7, 8]]
for a in A:
    a += [0]
print("A:", A)

t = ['2', '9765', '12', '13', '4']
tt = tuple(t)
print("tt:", tt)

a = "empty"

b = "empty too"

c = "another    "

x = -20
print(x % 2 + 1)

y = 20
print(y % (-6))

burst = [3, 1, 5, 8]
print("burst:", burst)


burst = [3, 1, 5, 8]
print("burst:", burst)

word = "xfzdefghjklmn"
print(min(word))

string = "abcdefghjklmnopqrstuvwxyz"
s = set(string)
print("s:", s)

string = "abcdefghjklmnopqrstuvwxyz"
print("s:", string[::-1])

lst = ["1", "2", "3", "4", "5"]
strlist = str(lst)
srlist = "".join(lst)

print("strlist:", strlist)
print("srlist:", srlist)

string = "abcdefghjklmnopqrstuvwxyz"
st = set(string)
print("st:", st)

a = tuple((1, 2, 3, 4))
print("list:", list(a))

a = [4]*5
print("a:", a)

nums = [1, 2, 3, 4, 5]
print("str_nums:", str(nums))

for i in range(10)[::-1]:
    print("i:", i)

ans = []
ds = ((-1, 0), (1, 0), (0, -1), (0, 1)); created = set(); lands = set()
       # iteral
   for p in P:   # O(N)    -> O(N*(N!))
        lands.add((p[0], p[1]))
        for i in range(4):  # O(4)
            x_ = p[0]+ds[i][0]
            y_ = p[1]+ds[i][1]
            if (x_, y_) in created:
                union(p, (x_, y_), lands)  # O(logN)
        created.add((p[0], p[1]))
        ans.append(len(lands))

    return ans


for i in range(10)[::-1]:
    print("i: ", i)


lst = [1,2,3,4,5]
print("str:", str(lst))

for i in range(10, 0, -1):
    print("i:", i)

for i in range(10)[::-1]:
    print("i:", i)

dict = {"b":2, "a":3, "c":6}
if "d" in dict:
    print(dict["d"])
elif "c" in dict:
    print(dict["c"])

nums = [1, 3, 5, 7, 9]

for i in range(10, 0, -1):
    print("i: ", i)

str = "this is string!"
if str.startswith(""):
    print("inside!")

rg = range(10)
print("rg:", rg)

set1 = set({1,2,3})
set2 = set({3,4,5})
print("set1:", set1)
print("set2:", set2)
set1 = set1.union(set2)
print("final set1:", set1)


a=3
a<<=3
print(bin(a))

b=2
b<<=12
print(bin(b))

c = b | a
print(bin(c))

dic = {1:2, 2:3, 4:5, 6:10}
a = sorted(dic.keys())
print(a)

for i in range(10)[::-1]:
    print("i: ", i)

str = "I love anacell Best services; Best services provided by anacell"
if "love" in str:
    print("inside!")

lst = ["1", "2", "3", "4", "5", "6"]
lst_set = set(["1", "2", "3", "4", "5", "6"])

str = "I love anacell Best services; Best services provided by anacell"
lst_set = set(str.split(" "))
print("lst_st:", lst_set)

review = "I love anacell Best services; Best services provided by anacell"
print("is:", review.lower().split(" "))
print("is:", review.lower().replace('[^a-z0-9]', '').split())

a = [2,3,5,1,2,3,5,2,3,57,6,33,776]
b = sorted(a, key=lambda x: x)
print("b:", b)


str = "I love anacell Best, services; Best services. provided by anacell"
review = re.sub(r"[^a-z0-9]", "", review)
print("str:", str)

review = re.sub(r"[^a-z0-9 ]", "", review)
print("str:", str)

l1= [1,2,3,4]
l2 = [5,6,7,8]
l1.append(l2)
print("l1:", l1)

i, j = 0
print("i:", i, "j:", j)


str = "I love anacell Best, services; Best services. provided by anacell"
review = re.sub(r"[^a-z0-9]", "", review)
print("str:", str)

l1= [1,2,3,4]
l2 = [5,6,7,8]
l1.append(l2)
print("l1:", l1)

num = "-239"
print(int(num) == (-239))

a = -239
print(str(a) == "239")

chars = '+-0123456789'
charss = chars.split("")
print(charss)

print("joke" > "dam")

dict = {"a":3, "b":4, "c":5, "g":1}
max1 = max(dict, key=dict.get)
max2 = max(dict.keys()) 
print("max1:", max1, "max2:", max2)
print("dict[max1]", dict[max1])

dict = {"a":3, "b":4, "c":5, "g":1}
print("keys-len:", len(dict))
for key in dict:
    print("key:", key)
