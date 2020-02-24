# https://leetcode.com/problems/binary-tree-postorder-traversal/
# Hard? why?
# Notes: Same as preorder but different order

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        
        answer = []
        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)
        if left:
            answer += left
        if right:
            answer += right 
        answer.append(root.val)
        
        return answer