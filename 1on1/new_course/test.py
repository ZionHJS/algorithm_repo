A = [34, 23, 1, 24, 75, 33, 1, 34, 24, 8, 54, 8]
A.sort()
print("A1:", A)
A = set(A)
print("A2:", A)


class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        n = len(A)
        if n == 1:
            return -1

        A.sort()  # initialize the list
        res = []
        i, j = 0, n-1  # two pointer i and j from the left and right
        while i+1 <= j:
            cur_sum = A[i] + A[j]
            j -= 1 if cur_sum >= K else res.append(cur_sum) i += 1

        return max(res) if res else return -1
