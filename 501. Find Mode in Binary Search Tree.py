# https://leetcode.com/problems/find-mode-in-binary-search-tree/
# Easy

# Note: 1st fail was because I forgot to change the max

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        count = dict()
        stack = [root]
        
        while stack:
            item = stack.pop()
            if item.val not in count.keys():
                count[item.val] = 0
            count[item.val] += 1
            
            if item.left:
                stack.append(item.left)
            if item.right:
                stack.append(item.right)
        
        cur_max = 0
        answer = []
        for key in count.keys():
            if count[key] > cur_max:
                answer = [key]
                cur_max = count[key]
            elif count[key] == cur_max:
                answer.append(key)
            else:
                pass
        
        return answer
                    
        
                
        
            
            