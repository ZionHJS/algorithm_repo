import heapq
q = []
heapq.heappush(q, -3)
heapq.heappush(q, -5)
heapq.heappush(q, -2)
heapq.heappush(q, -7)
heapq.heappush(q, -8)
heapq.heappush(q, -1)
heapq.heappush(q, -9)
heapq.heappush(q, -4)
heapq.heappush(q, 0)
heapq.heappush(q, -11)

print("q-1", q[-1])
print("q0", q[0])
print("len:", len(q))

for j in range(10)[::-1]:
    print("j:", j)

cur = "0000"
target = "1111"
new_cur = cur[:1] + target[1] + cur[2:]
print("new_cur:", new_cur)
print("cur[0]", cur[:0])


def tup(s):  # function to turn list=>s to int
    return tuple(map(int, s))


initial = tup("0000")
print(initial)

a = [1, 2, 3, 8]
b = [3, 4, 5]
c = zip(a, b)
print("c:", c)


store = []
store.append(9)
print("store:", store)
print("pop:", store.pop())
