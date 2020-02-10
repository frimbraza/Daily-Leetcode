# https://leetcode.com/problems/isomorphic-strings/
# Easy 
# Used Dict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        matching = dict()
        
        for a,b in zip(s,t):
            if a not in matching:
                if b not in matching.values():
                    matching[a] = b
                else:
                    return False
            else:
                if matching[a] != b:
                    return False
        return True