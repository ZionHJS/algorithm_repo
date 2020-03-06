class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n <= 1:
            return len(chars)
        chars.sort()

        i = 1
        count = 1
        re_idx = 1
        for i in range(n):
            if chars[i] == chars[i-1]:
                count += 1
                if i == n-1:
                    chars[re_idx] = str(count)
            else:
                if count > 1:
                    chars[re_idx] = str(count)
                re_idx = i+1
                count = 1

        #print("chars_s:", chars)
        i, j = 0, 0
        while i < n-1:
            j = i+1  # j<n
            if j == n-1:
                break
            if j+1 < len(chars) and chars[j].isdigit():
                for k in range(int(chars[j])-2):
                    chars.pop(j+1)
                # do something
                i += 2
            else:
                i += 1
        #print("final_chars:", chars)
        return len(chars)
