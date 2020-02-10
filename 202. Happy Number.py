# 202. Happy Number
# Easy
# https://leetcode.com/problems/happy-number/

# Notes: Weird worded question. Bandaid fixed by setting limit to 10. Need to learn more about flags and underscore.

class Solution:
    def isHappy(self, n: int) -> bool:
        
        def makeDigits(n):
            digits = []
            str_num = str(n)
            for char in str_num:
                digits.append(int(char))
            return digits
        
        for _ in range(10):
            digits = makeDigits(n)
            total = 0
            for digit in digits:
                total += digit * digit
            n = total
            if n == 1: 
                return True
        return False