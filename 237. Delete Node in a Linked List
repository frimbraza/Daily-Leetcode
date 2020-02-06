# https://leetcode.com/problems/delete-node-in-a-linked-list/submissions/
# Easy

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if not node:
            return
        
        current = node
        
        while current.next:
            current.val = current.next.val            
            if not current.next.next:
                current.next = None
            else:
                current = current.next
            