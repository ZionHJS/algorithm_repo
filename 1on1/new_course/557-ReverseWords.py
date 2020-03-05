class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        if not n <= 1:
            return s

        res = ""
        temp = ""
        for i in range(n):
            if s[i] != " ":
                temp += s[i]
            else:
                print("now_reverse:", self.reverse(temp))
                if len(temp):
                    res += self.reverse(temp)
                    temp = ""
                res += " "

    def reverse(self, word):
        n = len(word)
        new_word = ""
        if n == 1:
            return word
        else:
            for i in range(n-1, -1, -1):
                new_word += word[i]
        print("new_word:", new_word)
        return new_word
