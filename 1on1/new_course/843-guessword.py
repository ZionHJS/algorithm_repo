# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:


class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        n, self.cnt, self.target, self.visited, self.prev_cnt = len(
            wordlist), 0, [-1 for _ in range(6)], set(), 0

        while len(wordlist) > 0:
            #print("wordlist:", wordlist)
            cur_word = wordlist[0]
            #print("cur_word:", cur_word)
            self.tryguess(cur_word, master)
            wordlist = self.filterwords(wordlist)

            if self.cnt >= 10:
                break

    def filterwords(self, cur_wordlist):
        new_wordlist = []
        for word in cur_wordlist:
            if word not in self.visited:
                tmp_cnt = 0
                for i in range(6):
                    if self.target[i] != -1 and word[i] != self.target[i]:
                        break
                    tmp_cnt += 1
                if tmp_cnt == 6:
                    new_wordlist.append(word)
        return new_wordlist

    def tryguess(self, word, master):
        self.visited.add(word)
        tmp, tmp_cnt = master.guess(word), 0
        self.cnt += 1
        if tmp == -1 or tmp <= self.prev_cnt:
            return
        self.prev_cnt = tmp
        chars = "abcdefghijklmnopqrstuvwxyz"
        for i in range(6):
            if tmp_cnt + (6-i-1) == tmp:
                for j in range(i, 6):
                    self.target[j] = word[j]
                return
            if self.target[i] == -1:
                tmp_char = word[i]
                for char in chars:  # get random char to replace tmp_char to test
                    if char != tmp_char:
                        new_word = word[:i]+char+word[i+1:]
                        new_tmp = master.guess(new_word)
                        self.cnt += 1
                        if new_tmp < tmp:
                            self.target[i] = tmp_char
                            tmp_cnt += 1
                            if tmp_cnt == tmp:
                                return
                        elif new_tmp > tmp:
                            self.target[i] = char
                            self.prev_cnt = tmp
                        break
