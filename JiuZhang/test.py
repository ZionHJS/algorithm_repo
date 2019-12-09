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


nums_1 = [7, 5, -2, 13, 6, 4]
nums_2 = [1, 2, 3, 4]
nums_2.extend(nums_1)
nums_3 = nums_1 * 2 + nums_2
print(nums_3)
print(len(nums_3))


nums_1 = [7, 5, -2, 13, 6, 4]
nums_2 = [1, 2, 3, 4]
nums_1 += nums_2
print(nums_1)
nums_1.remove(4)
print(nums_1)
nums_1[:4] = ['a', 'b']
print(nums_1)
print(len(nums_1))

nums_1 = [7, 5, -2, 13, 6, 4]
nums_2 = (1, 2, 3, 4, ['a', 'b'])
nums_1.append(20)
nums_2[4].append('w')
nums_1.extend(nums_2)
print(nums_1[5:9])

list_1 = [7, 5, -2, 13, 6, 4, [1, 2]]
list_2 = list_1
list_2[0] = -9
list_2[6].append(100)
list_3 = list_2[6]
list_3.extend(['a', 'b'])
print(list_1[6][2])
print(list_1)

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

stu = Student('Jack', 70)
stu2 = Student('Tom', 80)
stu3 = stu2
stu3.score = 60
stu3 = stu
stu3.score = 50
print(stu.name, stu.score)

str_1 = '1234'
res = 0
for c in str_1:
    res = res * 10 + ord(c) - ord('0')

print(res)