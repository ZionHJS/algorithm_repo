class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return ''

        nums = []
        strs = []

        num = 0
        cur_string = ''

        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10 + int(s[i])  # num*10???
                # num = 0 + int(s[i])   #num*10???
            elif s[i] == '[':
                nums.append(num)
                strs.append(cur_string)
                num = 0
                cur_string = ''
            elif s[i] == ']':
                repeat_times = nums.pop()
                temp_string = strs.pop()
                for i in range(repeat_times):
                    temp_string += cur_string
                cur_string = temp_string
            else:
                cur_string += s[i]
                print('cur_string is:', cur_string)

        return cur_string
