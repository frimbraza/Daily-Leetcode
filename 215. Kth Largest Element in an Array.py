
# https://leetcode.com/problems/kth-largest-element-in-an-array/
# Medium

# fail1: Misunderstood question at first. was easier than I thought

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        return nums[-k]