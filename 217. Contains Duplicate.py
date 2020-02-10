# Detect Duplicates
# https://leetcode.com/problems/contains-duplicate/submissions/
# Easy
# Notes: Very easy solution. Just make a set and compare lengths.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        copy = set(nums)
        return not len(copy) == len(nums)