class Solution(object):
    def peakIndexInMountainArray(self, A):
        if not A or len(A) < 3:
            return False

        left, right = 0, len(A) - 1

        while left + 1 < right:
            mid = (left+right)//2

            if A[mid] < A[mid-1]:
                right = mid
            elif A[mid] > A[mid+1]:
                right = mid
            elif A[mid] < A[mid+1]:
                left = mid
            else:
                left = mid

        if A[left] < A[right]:
            return right
        else:
            return left
