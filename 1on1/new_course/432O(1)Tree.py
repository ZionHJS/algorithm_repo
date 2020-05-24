class Trie:
    def __init__(self, val=None):
        self.val = val
        self.children = {}
        self.empty = 0


class AllOne:
    def __init__(self):
        self.dict = {}
        self.max = Trie()
        self.cur_max = 0
        self.min = Trie()
        self.cur_min = 0

    def inc(self, key: str) -> None:
        if key not in self.dict:
            self.dict[key] = 1
            if not self.dict:
                # for min
                self.cur_min = 1
                self.min.children[self.cur_min] = Trie()
                self.min.chidlren[self.cur_min].children[key] = 1
                # for max
                self.cur_max = 1
                self.max.children[self.cur_max] = Trie()
                self.max.children[self.cur_max].children[key] = 1
        else:
            self.dict[key] += 1
            # for min
            if self.dict[key]-1 == self.cur_min:
                del self.min.children[self.cur_min].children[key]
                while self.cur_min > 0 and not self.min.children[self.cur_min].children:
                    self.cur_min -= 1
                if self.cur_min == 0:
                    self.cur_min = self.dict[key]
            # for max
            if self.dict[key] == self.cur_max:
                self.max.children[self.cur_max].children[key] = 1
            elif self.dict[key] > self.cur_max:
                self.cur_max = self.dict[key]
                self.max.children[self.cur_max] = Trie()
                self.max.children[self.cur_max].children[key] = 1
            else:
                self.max.children[self.dict[key]].children[key] = 1

    def dec(self, key: str) -> None:
        if key in self.dict:
            self.dict[key] -= 1
            # for min
            if self.dict[key]+1 <= self.cur_min:
                del self.min.children[dict[key]+1].children[key]
                while not self.min.children[self.cur_min].children:
                    self.cur_min -= 1
            # for max
            del self.max.children[self.dict[key]+1].children[key]
            while self.cur_max > 0 and not self.max.children[self.cur_max].children:
                self.cur_max -= 1
            if self.dict[key] == 0:
                del self.dict[key]

    def getMaxKey(self) -> str:
        if not self.cur_max:
            return ""
        return self.cur_max

    def getMinKey(self) -> str:
        if not self.cur_min:
            return ""
        return self.cur_min
