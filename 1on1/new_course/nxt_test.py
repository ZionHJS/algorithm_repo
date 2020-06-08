import bisect
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
