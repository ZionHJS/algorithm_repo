class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x+y < z:
            return False
        elif x == z or y == z or x+y == z or not z:
            return True
        if x > y:
            x, y = y, x

        dif = y-x

        def dfs(cur_dif, memo):
            nonlocal x, y, z
            if cur_dif == z or cur_dif+x == z or (x >= cur_dif and cur_dif+y == z):
                return True

            # gen new_dif and dfs_check
            if x > cur_dif and (y-(x-cur_dif)) not in memo:
                memo.add(y-(x-cur_dif))
                if dfs(y-(x-cur_dif), memo):
                    return True
            if x > (y-cur_dif) and (x-(y-cur_dif)) not in memo:
                memo.add(x-(y-cur_dif))
                if dfs(x-(y-cur_dif), memo):
                    return True
            if x+cur_dif < y and x+cur_dif not in memo:
                memo.add(x+cur_dif)
                if dfs(x+cur_dif, memo):
                    return True

            return False

        return dfs(dif, set([dif])) or dfs(x, set([x]))
