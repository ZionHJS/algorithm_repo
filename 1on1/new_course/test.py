from collections import deque

dq = deque()
dq.append(0)
dq.append(1)
dq.append(2)
dq.append(3)

print("size:", len(dq))
o

res = [12, 23, 54, 231, 13, 54]
print("res_min:", res.pop(min(res)))


res = [1, 2, 3, 4, 5, 6]
print("cur:", res[:-2])


s1 = "q2 31 23"
s2 = "q231 23"
s3 = "sa da sd"
if s1 == s2:
    print("s1==s2")
if s2 == s3:
    print("s2==s3")
