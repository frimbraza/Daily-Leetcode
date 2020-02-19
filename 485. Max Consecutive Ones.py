# https://leetcode.com/problems/max-consecutive-ones/submissions/
# Easy
# Notes: Litteraly just iterate thru

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        count = 0
        max = 0
        for digit in nums:
            if digit:
                count += 1
                if count > max:
                    max = count
            else:
                count = 0
        
        return max