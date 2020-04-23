import collections


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        prevs = collections.defaultdict(lambda: [])
        prevs[nums[0]] = [0]
        for i in range(1, len(nums)):  # TLE
            for key in prevs:
                if nums[i] < key:
                    for j in range(len(prevs[key])):
                        prevs[key][j] += 1
            if not prevs[nums[i]]:
                prevs[nums[i]] = [0]
            else:
                prevs[nums[i]].append(0)

        res = []
        idx_map = collections.defaultdict(lambda: 0)
        for i in range(len(nums)):
            j = idx_map[nums[i]]
            #print("j:", j, "prevs:", prevs)
            res.append(prevs[nums[i]][j])
            idx_map[nums[i]] += 1

        return res
