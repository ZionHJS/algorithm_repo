import queue


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList:
            return 0
        if beginWord == endWord:
            return 1

        word_list = set()
        for word in wordList:
            word_list.add(word)

        # BFS starts here
        dis = 1
        q = queue.Queue()
        s = set()  # to avoid repeat loop-bfs-
        q.put(beginWord)
        s.add(beginWord)
        while q.qsize():
            dis += 1
            print(dis)
            size = q.qsize()
            for i in range(size):
                word = q.get()
                # all word from nextword dict
                for next_word in self.get_nextword(word):
                    if next_word not in word_list or next_word in s:
                        continue
                    if next_word == endWord:
                        return dis
                    q.put(next_word)
                    s.add(next_word)
        return 0

    # get the next word
    def get_nextword(self, word):
        nextword_list = []
        for i in range(len(word)):
            left, right = word[:i], word[i+1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == char:
                    continue
                nextword_list.append(left + char + right)
        return nextword_list


list_a = [1, 2, 3, 4, 5, 6]
print(list_a[7:])

for char in 'abcdefghijklmnopqrstuvwxyz':
    print(char)
