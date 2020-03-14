# 129. Sum Root to Leaf Numbers
# Medium
# Kinda slow, Finished using recursion. Remember to stop using functions as variables (sum, pow, etc...)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        
        def sumLeaf(root, path):
            if not root:
                return 0
            new_path = path + [root.val]
            if not root.left and not root.right:
                new_sum = 0
                place = len(path)
                for digit in new_path:
                    new_sum += pow(10,place) * digit
                    place -= 1
                # print(new_sum)
                return new_sum
            else:
                sumRight = 0
                sumLeft = 0
                if root.right:
                    sumRight = sumLeaf(root.right, new_path)
                if root.left:
                    sumLeft = sumLeaf(root.left, new_path)
                return sumRight + sumLeft
        
        return sumLeaf(root, [])
        