class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(pushed)
        if n == 0:
            return True

        store = []
        i, j = 0, 0
        while j < n:
            if len(store) == 0:
                store.append(pushed[i])
                i += 1
            elif store[-1] != popped[j] and i < n:
                store.append(pushed[i])
                i += 1
            else:
                store.pop()
                j += 1

            if i > n:
                print("store:", store)
                print("j:", j)
                return False

        return True
