class MyCalendar:
    def __init__(self):
        self.begins = []
        self.internvals = {}

    def book(self, start: int, end: int) -> bool:
        i = bisect.bisect_left(self.begins, start)
        j = bisect.bisect_right(self.begins, start)
        if i - 1 >= 0 and self.internvals[self.begins[i - 1]] > start:
            return False
        elif i < len(self.begins) and self.begins[i] == start:
            return False
        if j < len(self.begins) and self.begins[j] < end:
            return False
        bisect.insort(self.begins, start)
        self.internvals[start] = end

        return True
