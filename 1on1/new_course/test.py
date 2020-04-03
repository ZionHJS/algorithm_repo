
import bisect
import collections
str1 = "aavvccsdef"
cnt = collections.Counter(str1)
print("cnt:", cnt)


s = "abcdefghijk"
res_s = bisect.bisect_right(s, "d")
print("res_s:", res_s)
list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
res_l = bisect.bisect_right(list, "d")
print("res_list:", res_l)


nums = [1, 3, 2, 2, 5, 2, 3, 7]
dic = collections.Counter(nums)
print("dic:", dic)


preorder = [3, 9, 20, 15, 7]
print("preorder_last:", preorder[-3:-1])


pop = preorder.pop(0)
print("pop:", pop)
print("preorder:", preorder)


s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
s.add(6)
print("s:", s)
list_s = list(s)
print("list_s:", list_s)

inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
print("postorder:", postorder[-4:-1])

inorder = [9, 3, 15, 20, 7]
str_inorder = str(inorder)
print("str_inorder:", str_inorder)
list_inorder = list(str_inorder)
print("list_inorder:", list_inorder)

list1 = [1, 2, 1]
list2 = [1, 2, 1]
print("equalOrNot:", list1 == list2)

num = 232
print("char_num:", chr(num))

test_list = [1, [4, [6]], [1, 1], 2, [1, 1]]
test_list = [4, [6]]
ordered = test_list[::-1]
print("ordered:", ordered)
print("test_list:", test_list)

num1 = 2
num2 = 4
num3 = 7
print("%1:", num1//3)
print("%2:", num2//3)
print("%3:", num3//3)

s = "loveleetcode"
c = "e"
print("idx:", s.index(c))

tmp_list = []
print("tmp:", tmp_list[-1])

pop = -3
tmp = 2
print("res:", pop/tmp)


string1 = "leetcode"
list_str1 = list(string1)
list_str1.sort(cmp=lambda x, y: x < y)
string2 = "codeeelt"
list_str2 = list(string2)
list_str2.sort()
print("list_str1:", list_str1)
print("list_str2:", list_str2)

list = [1, 2, 3, 4, 5, 6, 7, 8]
for i, num in enumerate(list):
    print("i:", i, "num:", num)

str_num = "2*3-4*5"
int_str = int(str_num)
print("int_str:", int_str)

num = 1e9
print("is_digit:", int(num))

s = set()
tu = (1, 2)
tu2 = (3, 4)
s.add(tu)
print("s:", s)
print("bollean:", tu2 not in s)

i = 1
print("%:", i//2)


s = set()
s.add((1, 2))
if (1, 2) in s:
    print("in here!")

list = [(1, 2), (1, 2), (5, 6)]
s_list = set(list)
print("s_list:", s_list)
list_s = list(s_list)
print("list_s:", list_s)

s = "abcdefghijk"
res = bisect.insert(s, "d")
print("res:", res)


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [3, 4, 5, 6, 7, 8, 9, 10, 11]
str_list = str(list1)
print("str_list:", str_list)


union_list = list1.union(list2)
print("union_list:", union_list)

string = ""
res = string+str(3)
print("res:", res)

print("tes:", 2 % 3)
print("test2:", 5 % 3)


memo = [[1, 2], [3, 4], [5, 6]]
for i, j in memo:
    print("i:", i, "j:", j)


a = {'a': 9, 'b': 1, 'c': 5}
l = len(a)
print("length:", l)


wordDict = ["catsss", "cat", "andsss", "sandss", "dogssss"]
print("min:", min(wordDict))

temp = ""
print("res:", temp[1:])

dicts = {1: "a", 2: "b", 3: "c"}
res = dicts.get
print("get:", res)


str1, str2 = "ab", "abc"
print("str2-str1:", str1 in str2)

strs = "sdfasdbasd"
test = strs.split(",")
print("test:", test)

for i in range(10):
    print("i:", i)
    for j in range(10):
        print("j:", j)
        if j == 3:
            break

cor = [1, 0]
val = 1
print("equal_1:", cor == val)
print("equal_2:", cor[0] == val)
print("exist:", val[0])

s = set()
s.add((1, 2))
s.add((3, 4))
s.add((5, 6))
s.add((1, 2))
s.add((5, 6))
print("s:", s)
print("length:", len(s))
s2 = set()

if s and s2:
    print("both!")
elif s or s2:
    print("only!")

s_list = list(s)
print("s_list:", s_list)


hits = [(0, 0)] * 3
print("hits:", hits)
print("%:", 299 % 300)

a = ["a", "b", "c"]
b = ["e", "f", "g"]
print("combine1:", a + b)
c = a.append(b)
print("append:", c)
print("com:", a += b)
