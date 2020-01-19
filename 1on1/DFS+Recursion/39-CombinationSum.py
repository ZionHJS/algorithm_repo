class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates or not target:
            return []

        candidates.sort()
        res = []
        temp = []

        self.dfs(res, temp, 0, candidates, target)
        return res

    def dfs(self, res, temp, index, candidates, target):
        if target < 0:
            return
        if target == 0:
            res.append(temp[:])
            return

        for i in range(index, len(candidates)):
            if candidates[i] > target:  # new target = target - candidates[i]
                break

            # if i > 0 and candidates[i] == candidates[i-1]:   #this part is checking the duplicates
                # continue

            temp.append(candidates[i])
            self.dfs(res, temp, i, candidates, target - candidates[i])
            temp.pop()
