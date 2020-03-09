# https://leetcode.com/problems/validate-binary-search-tree/
# Medium
# Conquered 2 years later on first try. (Shows you've improved)
# Note: Try to think of it as range and your passing the range tolerance

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        infinity = pow(2,32)
        
        def validMaxMin(root, cur_min, cur_max):
            if not root:
                return True
            
            if root.val >= cur_max:
                return False
            
            if root.val <= cur_min:
                return False
            
            
            return validMaxMin(root.left, cur_min, root.val) and validMaxMin(root.right, root.val, cur_max)
            
        if not root:
            return True
        
        return validMaxMin(root.left, -infinity, root.val) and validMaxMin(root.right, root.val, infinity)
    
    