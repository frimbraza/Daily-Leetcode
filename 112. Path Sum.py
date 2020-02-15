# https://leetcode.com/problems/path-sum/
# Easy
# Notes: Weird empty root condition, but otherwise easy recursion problem

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        
        sum = sum - root.val
        
        if not root.left and not root.right:
            if sum != 0:
                return False
            else:
                return True
        
        return self.hasPathSum(root.right, sum) or self.hasPathSum(root.left, sum)