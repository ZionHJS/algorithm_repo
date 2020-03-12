import heapq


class countToy:
    def toyCount(self, numToys, topToys, toys, numQuotes, quotes):
        toys.sort()
        count_toy = {}
        count_toy_quote = {}

        for toy in toys:
            toy_cnt = 0
            quo_toy_cnt = 0
            for quote in quotes:
                if toy in quote:
                    toy_cnt += quote.count(toy)
                    quo_toy_cnt += 1
            count_toy[toy] = toy_cnt
            count_toy_quote[toy] = quo_toy_cnt

        print("count_toy:", count_toy)
        print("count_toy_quote:", count_toy_quote)
        freqs = {}
        for toy, quo_cnt in count_toy_quote:
            if quo_cnt not in freqs:
                freqs[quo_cnt] = []
            heapq.heappush(freqs[quo_cnt], (-count_toy[toy], toy))
        print("freqs:", freqs)

        keys = freqs.keys()
        res = []
        for k in range(keys[-1], 0, -1):
            if k in freqs:
                for item in freqs[k]:
                    res.append(heapq.heappop(freqs[k]))
            if len(res) == topToys:
                break
        print("res:", res)

        for i in range(1, len(res)):
            for j in range(i, 0, -1):
                if res[j][0] == res[j-1][0]:
                    if res[j][1] < res[j-1][1]:
                        res[j], res[j-1] = res[j-1], res[j]

        # final res
        ans = []
        for o in range(numToys):
            ans.append(res[o][1])
            if len(ans) == numToys:
                return ans
