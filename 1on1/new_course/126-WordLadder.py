from collections import deque
import queue


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        self.res = []
        if not wordList:
            return -1
        setwordList = set(wordList)

        # bfs
        q, memo = queue.Queue(), set()
        q.put(beginWord)
        progress = [[beginWord]]
        while q.qsize():
            n, new_list = q.qsize(), []
            for i in range(n):
                cur_word = q.get()
                memo.add(cur_word)
                nxt_words = self.get_nxt_word(cur_word)
                for nxt_word in nxt_words:
                    if nxt_word in setwordList and nxt_word not in memo:
                        #print("nxt_word:", nxt_word)
                        q.put(nxt_word)
                        for record in progress:
                            #print("record:", record)
                            new_record = record
                            new_record.append(nxt_word)
                            #print("new_record:", new_record)
                            new_list.append(new_record)
                            if nxt_word == endWord:
                                self.res.append(new_record)
            progress = new_list
            if self.res:
                return self.res
        return []

    def get_nxt_word(self, word):
        nxt_words = []
        for i in range(len(word)):
            left, right = word[:i], word[i+1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if char != word[i]:
                    nxt_words.append(left+char+right)

        return nxt_words


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        self.res = []
        if not wordList:
            return -1
        setwordList = set(wordList)

        # bfs
        #q, memo= queue.Queue(), set()
        dq, memo = deque(), set()
        dq.append(beginWord)
        # q.put(beginWord)
        #progress = deque([beginWord])
        progress = [[beginWord]]
        # while q.qsize():
        while len(dq) > 0:
            #n, new_progress = q.qsize(), []
            n, new_progress = len(dq), []
            print("dq:", dq, "len_dq:", n, "progress:", progress)
            #print("dq:", dq)
            # for i in range(n-1, -1, -1):
            for i in range(n):
                #cur_word = q.get()
                cur_word = dq.pop()
                #print("cur_word:", cur_word)
                memo.add(cur_word)
                nxt_words = self.get_nxt_word(cur_word)
                #new_record = progress[i][:]
                new_record = progress.pop()
                print("new_record:", new_record)
                for nxt_word in nxt_words:
                    if nxt_word in setwordList and nxt_word not in memo:
                        # q.put(nxt_word)
                        dq.append(nxt_word)
                        # new_record.append(nxt_word)
                        new_progress.append(new_record+[nxt_word])
                        if nxt_word == endWord:
                            self.res.append(new_record+[nxt_word])
            progress = new_progress
            if self.res:
                return self.res

        return []

    def get_nxt_word(self, word):
        nxt_words = []
        for i in range(len(word)):
            left, right = word[:i], word[i+1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if char != word[i]:
                    nxt_words.append(left+char+right)

        return nxt_words
