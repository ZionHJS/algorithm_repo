import re
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


quotes = [
    "Elmo is the hottest of the season! Elmo will be on every kid's wishlist!",
    "The new Elmo dolls are super high quality",
    "Expect the Elsa dolls to be very popular this year, Elsa!",
    "Elsa and Elmo are the toys I'll be buying for my kids, Elsa is good",
    "For parents of older kids, look into buying them a drone",
    "Warcraft is slowly rising in popularity ahead of the holiday season"
]
toys = ["elmo", "elsa", "legos", "drone", "tablet", "warcraft"]
N = 3

# create a dictionary --> toy:[count, quote_count]
toys_freq = {toy: [0, 0] for toy in toys}
for quote in quotes:
    # for each quote, initiate toy occurence to False
    quote_toy = {toy: False for toy in toys}
    # convert quote to lower case,split
    for word in quote.lower().split():
        # remove anything other than lower cased letters in each word
        word = re.sub('[^a-z]', '', word)
        # increment count of toy if it exists in toys dictionary
        if word in toys_freq:
            toys_freq[word][0] += 1
            # if toy found in a quote, set to True and increment quote_count--> we do it only once for a toy in a quote
            if not quote_toy[word]:
                quote_toy[word] = True
                toys_freq[word][1] += 1
# print toy, count, quote_count
print(toys_freq.items())
# sort by count descending, quote_count descending, alphabetically
result = [w[0] for w in sorted(
    toys_freq.items(), key=lambda x: (-x[1][0], -x[1][1], x[0]))[:N]]
print(result)


# final final


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
        for key, val in count_toy_quote.items():
            if val not in freqs:
                freqs[val] = []
            freqs[val].append([count_toy[key], key])

        for key in freqs:
            print("key:", key, "freqs_key:", freqs[key])

        ans = []
        count = 0
        for i in range(numToys, -1, -1):
            if i in freqs:
                freqs[i] = self.sort_toy_arr(freqs[i], count_toy)
                for toy in freqs[i]:
                    ans.append(toy)
            if len(ans) >= topToys:
                break
        print("ans:", ans)

        return [toy[1] for toy in ans[:topToys]]

    def sort_toy_arr(self, arr, count_toy):
        for i in range(len(arr)):
            for j in range(i, 0, -1):
                if arr[j][0] > arr[j-1][0]:
                    arr[j], arr[j-1] = arr[j-1], arr[j]
                elif arr[j][0] == arr[j-1][0]:
                    if arr[j][1] < arr[j-1][1]:
                        arr[j], arr[j-1] = arr[j-1], arr[i]
        return arr


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