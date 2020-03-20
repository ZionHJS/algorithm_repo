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
