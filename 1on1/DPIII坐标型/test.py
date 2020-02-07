for i in range(6):
    for j in range(6):
        if j == 3:
            break
        print("i:", i)
        print("j:", j)
    print()


mid = 1/2
print("mid:", mid)

mid = 1//2
print("mid:", mid)

left = [1, 2, 3, 4, 5]
right = [6, 7, 8, 9, 10]
sum = left + right

print("sum:", sum)

nums1 = [1, 2, 2, 1]
nums2 = [1, 3, 2, 4, 0]

new1 = nums1.sort()
print("nums1:", new1)
