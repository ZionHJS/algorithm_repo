import numpy as np

arr = [1,2,4,1,7,8,3]

def rec_opt(arr, i):
    if i == 0:
        return arr[0]
    elif i == 1:
        return max(arr[0], arr[1])
    else:
        A = rec_opt(arr, i-2) + arr[i]
        B = rec_opt(arr, i-1)
        return max(A, B)
rec_opt(arr, 6)


def dp_opt(arr, i):
    opt = np.zero(len(arr))
    opt[0] = arr[0]
    opt[1] = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        A = opt[i-2] + arr[i]
        B = opt[i-1]
        opt[i] = max(A,B)
    return opt[len(arr)-1]
dp_opt(arr)



#DP-2 Find the number combination that equals the given number from a given arr
arr = [3, 34, 4, 12, 5, 2]

#recursive 
def rec_subset(arr, i, s):
    if s == 0:
        return True
    elif i == 0:
        return arr[0] == s
    elif arr[i] > s:
        return rec_subset(arr, i-1, s)
    else:
        A = rec_subset(arr, i-1, s-arr[i])
        B = rec_subset(arr, i-1, s)
        return A or B
rec_subset(arr, len(arr)-1, 9)

#memory 
def 