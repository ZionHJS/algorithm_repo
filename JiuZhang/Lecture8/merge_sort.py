# coding=utf-8

#merge_sort
#time complexity O(logn)
def merge_sort(array):
    tmp = [0 for _ in range(len(array))]   #把list提到最外面来 所有递归里面都调用这个list
    merge_sort_helper(array, 0, len(array) - 1, tmp)   #tmp => 


def merge_sort_helper(array, left, right, tmp):    # [left, right]
    if left >= right:
        return

    mid = (left + right) // 2    # [left, mid]  [mid + 1, right]
    merge_sort_helper(array, left, mid, tmp)
    merge_sort_helper(array, mid + 1, right, tmp)
    merge_sort(array, left, right, tmp)


def merge_sort(array, left, right, tmp):
    len = right - left + 1

    mid = (left + right) // 2  # [left, mid], [mid + 1, right]
    i, j = left, mid + 1

    for k in range(len):
        if i <= mid and (array[i] <= array[j] or j > right):
            tmp[k] = array[i]
            i += 1
        else:
            tmp[k] = array[j]
            j += 1

    for k in range(len):
        array[left + k] = tmp[k]


if __name__ == '__main__':
    array = [6, 4, 5, 7, 2, 4, 3, 4, 7, 8]
    merge_sort(array)

    for num in array:
        print(num, end=' ')
    print()
