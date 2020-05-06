class Solution:
    def racecar(self, target: int) -> int:
        self.res = math.inf
        # build distance_map
        dis = defaultdict(lambda: math.inf)
        left = target
        speed = 1
        steps = 0
        while left-speed > 0:
            steps += 1
            left = left-speed
            dis[left] = steps
            speed *= 2

        def helper(start, target, prev_steps):
            if prev_steps >= self.res:
                return
            speed = 1
            pos = start
            D = True
            steps = 0
            while pos < target:
                prev_pos = pos
                pos += speed
                speed *= 2
                steps += 1
            if pos == target:
                self.res = min(self.res, prev_steps+steps)
                return
            # for left
            #case01-stop and restart
            helper(prev_pos, target, prev_steps+steps+1)
            # case02-reverse and find the closest records
            tmp_speed = 1
            l_steps = 0
            while prev_pos > 0:
                prev_pos -= tmp_speed
                tmp_speed *= 2
                l_steps += 1
                if prev_pos in dis:
                    self.res = min(self.res, prev_steps+steps +
                                   l_steps+1+dis[prev_pos])

            # for right
            new_pos = target-(pos-target)
            #case01-reverse and restart
            helper(new_pos, target, prev_steps+steps+1)
            # case02-continue until find the closest records
            r_steps = 0
            while new_pos > 0:
                new_pos -= speed
                speed *= 2
                r_steps += 1
                if new_pos in dis:
                    self.res = min(self.res, prev_steps +
                                   steps+r_steps+1+dis[new_pos])

        helper(0, target, 0)

        return self.res
