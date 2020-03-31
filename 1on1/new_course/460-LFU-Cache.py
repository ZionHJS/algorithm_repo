import collections


class LFUCache:
    def __init__(self, capacity: int):
        self.dict = {}
        self.cnt_dict = collections.defaultdict(lambda: 0)
        self.order = collections.defaultdict(lambda: [])
        self.capacity = capacity
        self.min_cnt = 1

    def get(self, key: int) -> int:
        if key in self.dict:
            self.cnt_dict[key] += 1
            cur_cnt = self.cnt_dict[key]
            self.order[cur_cnt].append(key)
            if cur_cnt > 1:
                self.order[cur_cnt-1].remove(key)
                if not self.order[self.min_cnt]:
                    self.min_cnt += 1
            return self.dict[key]
        else:
            return -1

    def put(self, key: int, val: int) -> None:
        if len(self.dict) < self.capacity:
            if key not in self.dict:
                self.min_cnt = 0
            self.dict[key] = val
            self.cnt_dict[key] += 1
            cur_cnt = self.cnt_dict[key]
            self.order[cur_cnt].append(key)
            if cur_cnt > 1:
                self.order[cur_cnt-1].remove(key)
                if not self.order[self.min_cnt]:
                    self.min_cnt += 1
        else:
            while not self.order[self.min_cnt]:
                self.min_cnt += 1
            remove_key = self.order[self.min_cnt].pop(0)
            del self.cnt_dict[remove_key]
            del self.dict[remove_key]
            self.put(key, val)
