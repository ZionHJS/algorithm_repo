nums = (1, 5, 2, -4)
nums.append(3)
print(nums)

nums = [1,5,2,-5,2,4,-6,8]
nums = (1,5,2,-5,2,4,-6,8)
for (i, score) in enumerate(nums):
    print(i, score)

aList = [123, 'Google', 'Runoob', 'Taobao', 'Facebook',223, 12, 2, 1, 0, 'zion']
aList.sort()
print(aList)
aList.reverse()
print(aList)

#list生成器
result = [i for i in range(101) if i % 5 == 0]
print(result)

#翻转字符串
s = 'jiuzhang'
result = ''
print(s[9:1:-1])
