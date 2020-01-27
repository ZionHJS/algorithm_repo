memo = [-1 for _ in range(3)]
print('memo:', memo)
print('memo[2]:', memo[2])
print('range:', memo[1:3])


s = '123'
for i in range(2, len(s)):
    print('i:', i)
    print('s[i]:', s[i])

s = '123'
print(s[0:2])


for i in range(10, 1, -1):
    print('i:', i)

s = '123'
print(s[3:3])

list = [0, 1, 2, 3, 4, 5, 6]
print('max:', max(list))
