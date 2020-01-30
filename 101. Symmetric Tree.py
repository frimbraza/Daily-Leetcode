# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        return self.rootSym(root.left, root.right)

    def rootSym(self, left: TreeNode, right: TreeNode) -> bool:
        if not left and not right:
            return True
        elif not left or not right:
            return False
        elif left.val != right.val:
            return False

        return self.rootSym(left.left, right.right) & self.rootSym(left.right, right.left)