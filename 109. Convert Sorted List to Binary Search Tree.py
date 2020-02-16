# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
# Medium
# Note: Copied the array to bst code, and passed in the linked list as an array
# Note2: While fast, it isn't memory effecient. Redo later if you want

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:        
        array = []
        while head:
            array.append(head.val)
            head = head.next
        
        return self.sortedArrayToBST(array)
    
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        middle = len(nums)//2

        root = TreeNode(nums[middle])
        root.left = self.sortedArrayToBST(nums[:middle])

        if middle+1 < len(nums):
            root.right = self.sortedArrayToBST(nums[middle + 1:])

        return root