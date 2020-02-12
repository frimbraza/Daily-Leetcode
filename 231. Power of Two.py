# https://leetcode.com/problems/power-of-two/
# Easy
# Note: Use recursion and take note of edge cases

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 1 or n % 2 == 1:
            return False
        if n == 2:
            return True
        else:
            return self.isPowerOfTwo(n/2)