import queue

q = queue.Queue()
q.put([1, 2])
a, b = q.get()
print("a:", a)
print("b:", b)

res = {1: float("inf")}
print("res:", res)

list = [[1, 2], [2, 3], [3, 4]]
ans = [2, 3]
ans_ = [3, 2]
if ans in list:
    print("ans in here!")

if ans_ in list:
    print("ans_ in here!")
else:
    temp = ans_[0]
    ans_[0] = ans_[1]
    ans_[1] = temp
    print("now ans_:", ans_)
