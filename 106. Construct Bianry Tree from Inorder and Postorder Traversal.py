# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# Medium
# Note: Remember that postorder is left, right, root and that all orders are split based on inorder



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        if not postorder or not inorder:
            return None
        
        val = postorder[-1]
        root = TreeNode(val)
        
        mid = inorder.index(val)
        
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid+1:], postorder[mid:-1])
        
        return root