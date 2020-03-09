# https://leetcode.com/problems/permutation-sequence/
# Medium

# Try1: permutation out of order - sol was to sort list after
# Try2: sort led to time limit exceeded - used itertools.permutation
# Note: want to write my own permutation function next time
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        perms = list(itertools.permutations(range(1, n + 1)))
        
        answer = ''
        for i in perms[k-1]:
            answer += str(i)
            
        return answer
            