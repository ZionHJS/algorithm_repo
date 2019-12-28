class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return []
        res = [0, 0]

        i, j = 0, len(numbers) - 1
        two_sum = 0

        while i < j:
            two_sum = numbers[i] + numbers[j]
            if two_sum < target:
                i += 1
            elif two_sum > target:
                j -= 1
            else:
                res[0] = i + 1
                res[1] = j + 1
                break

        return res
