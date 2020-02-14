import heapq


class Solution:
    def reorganizeString(self, S: str) -> str:
        if not S or len(S) == 1:
            return S

        char_dict = {}
        heap = []
        res = "_"
        temp_char = ""

        for i in range(len(S)):
            if S[i] not in char_dict:
                char_dict[S[i]] = 1
            else:
                char_dict[S[i]] += 1

        self.make_heap(heap, char_dict)
        print("now_heap:", heap)
        while heap[1][0] < 0:
            if heap[0][1] != res[-1]:
                res += heap[0][1]
                heap[0][0] += 1
            else:
                res += heap[1][1]
                heap[1][0] += 1

        if -heap[0][0] > 1:
            print("res:", res)
            print("final_heap:", heap)
            return ""
        else:
            res += heap[0][1]
            return res[1:]

    def make_heap(self, heap, char_dict):
        for key in char_dict:
            heapq.heappush(heap, (-char_dict[key], key))
