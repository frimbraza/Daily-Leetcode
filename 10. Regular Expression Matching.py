# https://leetcode.com/problems/regular-expression-matching/
# Hard
# Note: This was done in class. Was difficult to understand

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        if len(p) == 0:
            return len(s) == 0
        
        if len(p) == 1 or p[1] != '*':
            if len(s) == 0 or s[0] != p[0] and p[0] != '.':
                return False
            else:
                return self.isMatch(s[1:] , p[1:])
        else:
            i = -1
            while i < len(s) and (i < 0 or s[i] == p[0] or p[0] == '.'):
                if self.isMatch(s[i+1:],p[2:]): # fix this
                    return True
                i += 1
        return False