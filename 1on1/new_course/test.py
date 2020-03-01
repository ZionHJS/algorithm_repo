import collections

li = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 6, 8]
left = collections.Counter(li)
end = collections.Counter()
print("left:", left)
print("end:", end)


words = ["hello", "hi", "helo"]
words.remove("hello")
print("words:", words)

word = "something"
print("word_idx:", word[100])
