import random


class Solution:
    def __init__(self, w: List[int]):
        self.w = w
        self.sums = sum(w)  # random(1, sums+1)
        self.proportion = []   # random() => [)
        prefix = 0
        for i in range(len(w)):
            self.proportion.append([prefix+1, prefix+w[i]])
            prefix += w[i]

    def pickIndex(self) -> int:
        rnd = random.randint(1, self.sums+1)
        insert_idx = bisect.bisect_right(self.proportion, rnd)
        return self.w[insert_idx]
