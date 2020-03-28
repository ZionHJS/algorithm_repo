import queue


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # bfs
        jump = 1
        visited, s = set(), set()
        q = queue.Queue()
        if stones[0] + 1 == stones[1]:
            q.put((1, 1))
        while q.qsize():
            cur_com = q.get()
            if cur_com not in visited:
                visited.add(cur_com)
                cur_idx, last_jump = cur_com[0], cur_com[1]
                s.add(stones[cur_idx])
                if stones[-1] in s:
                    return True
                for i in range(cur_idx+1, len(stones)):
                    if stones[cur_idx] + last_jump-1 == stones[i]:
                        q.put((i, last_jump-1))
                    if (stones[cur_idx] + last_jump) == stones[i]:
                        q.put((i, last_jump))
                    if (stones[cur_idx] + last_jump+1) == stones[i]:
                        q.put((i, last_jump+1))
                    if (stones[cur_idx] + last_jump+1) < stones[i]:
                        break

        return False


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        memo, stones, target = {}, set(stones), stones[-1]
        # dfs

        def dfs(unit, last):
            if unit == target:
                return True
            if (unit, last) not in memo:
                memo[(unit, last)] = any(dfs(unit + move, move)
                                         for move in (last - 1, last, last + 1) if move and unit + move in stones)
            return memo[(unit, last)]

        return dfs(1, 1) if 1 in stones else False
