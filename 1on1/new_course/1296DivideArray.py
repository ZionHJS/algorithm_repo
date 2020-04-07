class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        d, m = divmod(n, k)
        if m != 0:
            return False
        nums.sort()

        # Grouping
        for i in range(d):
            if not self.get_nxt_set(nums, k):
                return False
        return True

    def get_nxt_set(self, nums, k):
        cnt, prev = 0, 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if prev == 0:
                    cnt += 1
                    prev = nums[i]
                    nums[i] = 0
                else:
                    if nums[i] == prev + 1:
                        cnt += 1
                        prev = nums[i]
                        nums[i] = 0
            if cnt == k:
                return True
        return False
