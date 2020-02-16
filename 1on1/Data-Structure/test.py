import queue

q = queue.Queue()
q.put([1, 2])
a, b = q.get()
print("a:", a)
print("b:", b)
