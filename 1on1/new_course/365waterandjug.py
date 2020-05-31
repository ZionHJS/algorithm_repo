class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x+y < z:
            return False
        elif x == z or y == z:
            return True
        elif x+y == z:
            return True

        dif = abs(y-x)  # =>dfs until new_dif == 0

        def dfs(cur_dif, memo):
            nonlocal x, y, z
            if cur_dif == z:
                return True
            elif (y >= cur_dif and cur_dif+x == z) or (x >= cur_dif and cur_dif+y == z):
                return True
            elif (x >= cur_dif and y-(x-cur_dif) == z) or (y >= cur_dif and x-(y-cur_dif) == z):
                return True
            elif cur_dif == x or cur_dif == y:
                return False

            # gen_new_dif
            y_, x_ = False, False
            if x >= cur_dif:
                if (y-(x-cur_dif)) > 0 and (y-(x-cur_dif)) not in memo:
                    memo.add(y-(x-cur_dif))
                    y_ = dfs(y-(x-cur_dif), memo)
                elif (x-cur_dif)-y not in memo:
                    memo.add((x-cur_dif)-y)
                    y_ = dfs((x-cur_dif)-y, memo)
            elif cur_dif-x not in memo:
                memo.add(cur_dif-x)
                y_ = dfs(cur_dif-x, memo)
            if y >= cur_dif:
                if (x-(y-cur_dif)) > 0 and (x-(y-cur_dif)) not in memo:
                    memo.add(x-(y-cur_dif))
                    x_ = dfs(x-(y-cur_dif), memo)
                elif (y-cur_dif)-x not in memo:
                    memo.add((y-cur_dif)-x)
                    x_ = dfs((y-cur_dif)-x, memo)
            elif cur_dif-y not in memo:
                memo.add(cur_dif-y)
                x_ = dfs(cur_dif-y, memo)

            return (y_ or x_)

        return dfs(dif, set())
