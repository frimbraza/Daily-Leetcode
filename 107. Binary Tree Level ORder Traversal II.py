# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# Easy
# Notes: Used iterative approach with a queue. Worked well

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        solution = []
        
        level = 0
        queue = [(root, level)]
        
        while queue:
            queue_object = queue[0]
            queue = queue[1:]           # Reduce Queue
            
            node = queue_object[0]
            level = queue_object[1]
            
            if level >= len(solution):  # make room in solution if needed
                solution.append([])
            
            solution[level].append(node.val)
            
            # Add to Queue
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
                
        return reversed(solution)