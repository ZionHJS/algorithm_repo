import heapq


class countToy:
    def toyCount(self, numToys, topToys, toys, numQuotes, quotes):
        toys.sort()
        count_toy = {}
        count_toy_quote = {}

        for toy in toys:
            print("toy:", toy)
            toy_cnt = 0
            quo_toy_cnt = 0
            for quote in quotes:
                if toy in quote.lower():
                    quote = quote.lower()
                    toy_cnt += quote.count(toy)
                    print("toy_cnt:", toy_cnt)
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


numToys = 6
topToys = 2
toys = ["elmo", "elsa", "legos", "drone", "tablet", "warcraft"]
numQuotes = 6
quotes = [
    "Elmo is the hottest of the season! Elmo will be on every kid's wishlist!",
    "The new Elmo dolls are super high quality",
    "Expect the Elsa dolls to be very popular this year, Elsa!",
    "Elsa and Elmo are the toys I'll be buying for my kids, Elsa is good",
    "For parents of older kids, look into buying them a drone",
    "Warcraft is slowly rising in popularity ahead of the holiday season"
]

countToys = countToy()
print("ans:", countToys.toyCount(numToys, topToys, toys, numQuotes, quotes))
