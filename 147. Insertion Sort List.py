# https://leetcode.com/problems/insertion-sort-list/
# Medium

# My interpretation of insertion sort of a linked list
# First, you shouldn't use a singly linked list for insertion sort because you often need to go back
# I got around this by removing the node and iterating from the start of the list until I found the correct placement. Such a method would take an extraordinary long time and would probably eliminate the only reason one would use insertion sort in the first place (for a mostly sorted list)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        
        currentNode = head
        
        while currentNode:
            if not currentNode.next:
                break
            
            if currentNode.next.val < currentNode.val:
                ... # Remove, find place, then continue
                removed = currentNode.next
                currentNode.next = removed.next
                
                if removed.val < head.val:
                        removed.next = head
                        head = removed
                else:
                    walker = head
                    while walker:
                        if removed.val < walker.next.val:
                            removed.next = walker.next
                            walker.next = removed
                            break
                        walker = walker.next
            else:
                currentNode = currentNode.next
            
        return head
        