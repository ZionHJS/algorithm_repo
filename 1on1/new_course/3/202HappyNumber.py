class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 0:
            return False
        elif n == 1:
            return True

        temp_res = 0
        str_n = str(n)
        temp_res = self.turn_num(str_n)

        if temp_res == 1:
            return True
        else:
            self.isHappy(temp_res)

    def turn_num(self, str_n):
        sum = 0
        temp_single = 0
        for i in range(len(str_n)):
            temp_single = int(str_n[i:i+1])
            sum += temp_single**2
        return sum
