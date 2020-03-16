# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Easy
# Redid in Python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        new_head = head
        tail = head
        
        current = head.next
        while current:
            if current.val != tail.val:
                tail.next = current
                tail = tail.next
                
            current = current.next
            
        tail.next = None
        return new_head
        