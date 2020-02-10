# https://leetcode.com/problems/contains-duplicate-ii/
# Contains Dup II
# Easy
# First try time exceeded. Did Binary Search
# Second approach (this), uses a dict to store latest index and min dist. Completes in n instead of n^2

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        holder = dict()
        
        i = 0
        for num in nums:
            if num not in holder.keys():
                holder[num] = (i, k+1)
            else:
                holder[num] = (i, min(holder[num][1], i - holder[num][0])) # the least min found
            
            if holder[num][1] <= k:
                return True
            
            i += 1
            
        return False