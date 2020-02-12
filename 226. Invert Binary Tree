# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# https://leetcode.com/problems/invert-binary-tree/
# Easy
# Note Just make a new tree with left & right child switched

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        this_root = TreeNode(root.val)
        this_root.left = self.invertTree(root.right)
        this_root.right = self.invertTree(root.left)
        
        return this_root