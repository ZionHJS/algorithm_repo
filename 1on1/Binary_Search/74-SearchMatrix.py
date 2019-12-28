def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        elif not matrix[0]:
            return False

        left, right = 0, len(matrix)-1
        target_index = 0

        while left + 1 < right:
            mid = left + (right - left)//2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                target_index = mid
                break
            elif matrix[mid][0] > target:
                right = mid
            else:
                left = mid

        if not target_index:
            if matrix[left][-1] >= target:
                if self.target_helper(matrix[left], target):
                    return True
                else:
                    return False
            else:
                if self.target_helper(matrix[right], target):
                    return True
                else:
                    return False
        else:
            if self.target_helper(matrix[target_index], target):
                return True
            else:
                return False

    def target_helper(self, array, target):
        if not array:
            return False
        left, right = 0, len(array)-1
        while left+1 < right:
            mid = left + (right-left)//2
            if array[mid] >= target:
                right = mid
            else:
                left = mid
        if array[right] == target:
            return True
        if array[left] == target:
            return True
        return False
