class Solution:
    def reverseString(self, s: List[str]) -> None:
        if not s:
            return False
        elif len(s) == 1:
            return s

        i, j = 0, len(s)-1
        tmp = [0]

        while i < j:
            tmp[0] = s[i]
            s[i] = s[j]
            s[j] = tmp[0]

            i += 1
            j -= 1

        return s


i, j = 0, 99
while i + 1 < j:
    i += 1
    j -= 1
print(i)
print(j)
