# https://leetcode.com/problems/binary-tree-preorder-traversal/
# Medium
# Notes: Used recursion
# Good memory usage but only faster than 65.33% faster
# Next step probably to use iteration

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        if not root:
            return None
        
        answer = []
        answer.append(root.val)
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        if left:
            answer += left
        if right:
            answer += right 
        
        return answer