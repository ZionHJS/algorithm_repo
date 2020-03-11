words = ["cat", "cats", "catsts", "dog", "dogcatsdog",
         "hippop", "rat", "ratc"]
max_word = max(words, key=lambda x: len(x))
max_word_len = len(max(words, key=lambda x: len(x)))
print("word_len:", max_word_len)


word1 = "abcd"
word2 = "acde"
word3 = "abde"
if word1 < word2:
    print("word2 is bigger!")
else:
    print("word1 is bigger")

word1 = "abcd"
word3 = "abde"
if word3 < word1:
    print("word1 is bigger!")
else:
    print("word3 is bigger")


toys = ["sdasds", "elmo", "elsa", "legos",
        "drone", "tablet", "airbullon", "warcraft"]
#sorted_toys = sorted(toys)
toys.sort()
print("sorted_toys:", toys)


dic = {4: "apple", 3: "banana", 2: "watermelon", 1: "pinch"}
print("dic:", dic)
keys = dic.keys()
print("keys:", keys)
print("keys[-1]:", keys[-1])
