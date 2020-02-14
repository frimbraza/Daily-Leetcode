# https://leetcode.com/problems/palindrome-linked-list/
# Easy
# Note: Just brute force store in array and run normal algorithm
# Next time try to do using O(1) space

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        
        store = []
        current = head
        
        while current:
            store.append(current.val)
            current = current.next
        
        begin = 0
        ending = len(store) - 1
        
        while begin < ending:
            if store[begin] != store[ending]:
                return False
            begin += 1
            ending -= 1
        
        return True
        
        
        