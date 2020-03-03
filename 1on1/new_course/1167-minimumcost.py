class Solution:
    def __init__(self):
        self.count = 0

    def connectSticks(self, sticks: List[int]) -> int:
        n = len(sticks)
        if n <= 2:
            return sum(sticks)

        self.dfs(sticks)

        return self.count

    def dfs(self, sticks):
        if len(sticks) <= 2:
            self.count += sum(sticks)
            return

        sticks.sort(reverse=True)
        res = []
        res.append(sticks[-1]+sticks[-2])
        self.count += sticks[-1]+sticks[-2]
        sticks = sticks[:-2]

        while len(sticks):
            if len(sticks) == 1:
                cur_min_res = min(res)
                res.remove(cur_min_res)
                pop = sticks.pop()
                res.append(cur_min_res + pop)
                self.count += cur_min_res + pop
            else:
                if min(res) > sticks[-2]:
                    get_1 = sticks.pop()
                    get_2 = sticks.pop()
                    res.qppend(get_1 + get_2)
                    self.count += get_1 + get_2
                else:
                    get_0 = sticks.pop()
                    cur_min_res = min(res)
                    res.remove(cur_min_res)
                    res.append(cur_min_res + get_0)
                    self.count += cur_min_res + get_0

        return self.dfs(res)
