# 利用cmp 和 lambda()来排序
L = [('a', 3), ('d', 2), ('c', 1), ('b', 4)]
a = sorted(L, cmp=lambda x, y: cmp(x[0], y[0]), reverse=True)
b = sorted(L, cmp=lambda x, y: cmp(x[1], y[1]))
print L
print a
print b

dic = {3: 2, 4: 4, 5: 4, 6: 4}
target = max(dic, key=dic.get)
print("target:", target)
