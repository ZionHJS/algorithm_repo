class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x == y != z or x+y < z:
            return False
        elif x == z or y == z:
            return True
        elif x+y == z:
            return True

        dif = abs(y-x)  # =>dfs until new_dif == 0

        def dfs(cur_dif, memo):
            nonlocal x, y, z
            if cur_dif == z or (cur_dif+x == z or cur_dif+y == z):
                return True
            elif y-(x-cur_dif) == z or x-(y-cur_dif) == z:
                return True
            elif cur_dif == x or cur_dif == y:
                return False

            # gen_new_dif
            y_, x_ = False, False
            if (y-(x-cur_dif)) > 0 and (y-(x-cur_dif)) not in memo:
                memo.add(y-(x-cur_dif))
                y_ = dfs(y-(x-cur_dif), memo)
            if (x-(y-cur_dif)) > 0 and (x-(y-cur_dif)) not in memo:
                memo.add(x-(y-cur_dif))
                x_ = dfs(x-(y-cur_dif))

            return (y_ or x_)

        return dfs(dif, set())
