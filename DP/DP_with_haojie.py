import numpy as np

#1 Given Array and a Number and from the max combination of the Array(No Adjacent Number)
arr = [1,2,4,1,7,8,3]
#recursive
def OPT(arr, i):
    if i == 0:
        return arr[0]
    elif i == 1:
        return max(arr[0], arr[1])
    else:
        A = OPT(arr, i-2) + arr[i]
        B = OPT(arr, i-1)
        return max(A, B)
OPT(arr, 6)
#memory DP
def dpOPT(arr):
    opt = np.zero(len(arr))
    opt[0] = arr[0]
    opt[1] = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        A = opt[i-2] + arr[i]
        B = opt[i-1]
        opt[i] = max(A,B)
    return opt[len(arr)-1]
dpOPT(arr)



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

#memory DP
def dp_subset(arr, S):
    subset = np.zeros((len(arr), S+1), dtype=bool) #create the j array / dtype = data type 这里全部保存boolean type的数据
    subset[0, :] = False   #0 row at all postions are False
    subset[:, 0] = True   #all rows at postion 0 all True
    if arr[0] <= S+1:
        subset[0, arr[0]] = True   #get the one that is true out

    for i in range(1, len(arr)):
        for s in range(1, S + 1):
            if arr[i] > s:
                subset[i,s] = subset[i-1, s]
            else:
                A = subset[arr, i-1, s-arr[i]]
                B = subset[i-1, s]
                subset[i, s] = A or B
    r,c = subset.shape
    return  subset[r-1, c-1]

dp_subset(arr, 9)

#memory DP same but simple version
def dp_subset(arr, S):
    subset = np.zeros((len(arr), S+1), dtype=bool)   #create 2D array  datatype = Boolean
    subset[0, :] = False   #fill the first row
    subset[:, 0] = True   #fill the first col
    subset[0, arr[0]] = True  #find the one in row-1 that is true

    for i in range(1, len(arr)):
        for s in range(1, S+1):  #注意 这里是从二维数组内向外长的
            if arr[i] > s:
                subset[i,s] = subset[i-1, s]
            else:
                A = subset[i-1, s-arr[i]]   #start from i-1 = 0
                B = subset[i-1, s]
                subset[i, s] = A or B   #只要一个为true就为ture 都为False就是False
    return  subset[len(arr)-1, s]

print(dp_subset(arr, 9))
