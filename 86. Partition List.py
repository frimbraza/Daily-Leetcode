# 86. Partition List
# https://leetcode.com/problems/partition-list/
# Fast and Efficient but a little messy.
# Medium
# Notes: Beware of cycles. You need to clear the end of the end node if you're gonna make two
# Notes: 1 error because didn't account for case of 1 head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        new_head = None
        first = None
        second_head = None
        second = None
        
        current = head
        while current:
            # print(current.val)
            if current.val < x:
                if not first:
                    first = current
                    new_head = first
                    # print(f'in not first.val: {first.val}')
                else:
                    first.next = current
                    first = first.next
                    # print(f'in else first.val: {first.val}')
            else:
                if not second:
                    second = current
                    second_head = second
                    # print(f'in not second.val: {second.val}')
                else:
                    second.next = current
                    second = second.next
                    # print(f'in else second.val: {second.val}')
            
            current = current.next
        
        # print('out of while')
        if not new_head:
            return second_head
        elif not second_head:
            return new_head
        else:
            first.next = second_head
            second.next = None
            return new_head
        
        
        