# Single Number II
# https://leetcode.com/problems/single-number-ii/
# Medium

# Solution: Dict -> update -> find value that is 1

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = dict()
        for num in nums:
            if num not in counter.keys():
                counter[num] = 1
            else:
                counter[num] += 1
        
        for key in counter.keys():
            if counter[key] == 1:
                return key