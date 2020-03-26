preorder = [3, 9, 20, 15, 7]
print("preorder_last:", preorder[-3:-1])


pop = preorder.pop(0)
print("pop:", pop)
print("preorder:", preorder)


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
