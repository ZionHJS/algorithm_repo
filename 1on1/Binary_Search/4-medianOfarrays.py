# binary search -> unfinished
import math


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if not nums_1 and not nums_2:
            return -1

        if nums_1[-1] <= nums_2[0]:
            return (nums_1[-1]+nums_2[0])/2
        elif nums_2[-1] <= nums_1[0]:
            return (nums_2[-1]+nums_1[0])/2
        else:
            len_1 = len(nums1)
            len_2 = len(nums2)

            min_num = math.min(nums1[0], nums2[0])
            max_num = math.max(nums1[-1], nums2[-1])

            left, right = min_num, max_num

            while left + 1 < right:
                mid = left + (right-left)//2


tmp_list = [0 for _ in range(4+5)]
print(tmp_list)


# 暴力解 不过关


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if not nums1 and not nums2:
            return -1

        index_1 = 0
        index_2 = 0
        len_1 = len(nums1)
        len_2 = len(nums2)

        tmp_list = [0 for _ in range(len_1+len_2)]

        for k in range(len_1+len_2):
            if (nums1[index_1] <= nums2[index_2] and index_1 < len_1 and index_2 < len_2) or index_2 >= len_2:
                tmp_list[k] = nums1[index_1]
                index_1 += 1
            else:
                tmp_list[k] = nums2[index_2]
                index_2 += 1

        if ((len_1 + len_2)//2) % 2:
            mid = (len_1 + len_2)//2
            return (tmp_list[mid] + tmp_list[mid+1])/2
        else:
            mid = (len_1 + len_2)//2
            return tmp_list[mid]


list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list_1 = list_1[5:]   #[6, 7, 8, 9]
# list_1 = list_1[:5]   #[1, 2, 3, 4, 5]
print(list_1)
