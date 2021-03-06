import re
import itertools
import collections
import bisect

lst = [0] * 10
print("idx:", bisect.bisect_left(lst, 3, 0, 1))


# a = [[1, 2], [2, 4], [3, 6]]
# b = [[1, 2]]
# print("product:", list(itertools.product(a, b)))

s = "aaabbbcc"
print("counter:", collections.Counter(s))

str = "$50 each. $100, $999"
lst = re.findall(r"\$\d+", str.lower())
print("lst:", lst)


print("find:", str.find("$"))
print("split:", str.split("$"))

lst = [[1, 2], [3, 4], [5, 6]]
for u, v in lst[::-1]:
    print("u:", u, "v:", v)

for i in range(10, -1, -1):
    print("i:", i)

num = "0010"
print("int:", int(num))

print("or:", 10 or 1)

print("test:", []+[[2, 3], [4, 5]])

s = set([1, 2, 3, 4, 5])
print("set:", s)

s = set()
s.add(1)
s.add(3)
print("s:", s)

num = -10
print("str:", str(num))

str = "$50 each. $100, $999"
lst = re.findall(r"\$\d+", str.lower())
print("lst:", lst)

print("bin:", bin(0))

print("who larger:", "abc" < "aaaa")

for i in range(1, 10)[::-1]:
    print("i:", i)

a = "A"
b = "A"
print(a == b and "EQ" or "Not EQ")

a = [[1, 2], [2, 4], [3, 6]]
b = [[1, 2]]

print("zip:", zip(a, b))

lst = ["a", "b"]
set_ = set()
set_.addAll(lst)
print("set_:", set_)

grid = [[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
for g in grid, zip(*grid):
    print("g:", g)
    X = []
    for x, row in enumerate(g):
        print("x:", x, "row:", row, "sum:", sum(row), "[x]*row:", [x]*sum(row))
        X += [x]*sum(row)
    print("X:", X)

for i in range(-10):
    print("i:", i)
lst = [0, 1, 2, 3]*2
print("is:", lst)

print("mod:", -1 % 10)

for i in range(10)[::-1]:
    print("i:", i)

lst_str = "abcdefg"
print("arr is:", list(lst_str))

print("compare:", "3" < "6")

print("is:", ~10)

print("int:", int("0000"))

text = "  walks  udp package   into  bar a"
print("split:", text.split(" "))
print("filter:", list(filter(lambda x: len(x), text.split(" "))))

stack = [[1, 2]]
left, right = stack.pop()
print("left:", left, "right:", right)

print("%:", 9 % 8)
