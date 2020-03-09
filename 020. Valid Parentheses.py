# https://leetcode.com/problems/valid-parentheses/
# Easy
# Just use a stack

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left = ['(', '{', '[']
        right = [')', '}', ']']
        
        for char in s:
            if char in left:
                ind = left.index(char)
                stack.append(right[ind])
            elif char in right:
                if not stack:
                    return False
                    
                if stack[-1] != char:
                    return False
                else:
                    stack.pop()
        if not stack:
            return True
        return False
        