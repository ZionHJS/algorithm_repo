class Solution(object):
    def removeDuplicates(self, nums):
        if not nums or len(nums) == 1:
            return nums

        tmp = nums[0]
        i, j = 0, 1

        while j <= len(nums) - 1:
            if nums[j] > tmp:
                if i + 1 < j:
                    i += 1
                    tmp = nums[j]
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1
                    continue
                else:
                    j += 1
            else:
                j += 1

        return nums[:i]


tmp = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = tmp.pop(0)
print(a)
print(tmp)
b = tmp.pop(0)
print(b)
print(tmp)
c = tmp.pop(0)
print(c)
print(tmp)
