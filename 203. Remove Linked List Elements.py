# https://leetcode.com/problems/remove-linked-list-elements/submissions/
# Easy
# Note: If you remove from a linked list, you probably shouldn't move on (consecutive removal)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        # only if given empy list
        if not head:
            return None
        
        # if the head contains the value, then skip it and return the next node.
        if head.val == val:
            return self.removeElements(head.next, val)
        
        # occurs when head exists and is not an item to remove
        prev = head
        next_node = head.next
        
        while next_node:
            if next_node.val == val:
                prev.next = next_node.next
                next_node = prev.next
            else:
                prev = prev.next
                if next_node:
                    next_node = next_node.next
        
        return head
                
        