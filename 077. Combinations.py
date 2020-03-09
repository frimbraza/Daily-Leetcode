# https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        def permu(index,temp):
            if len(temp)==k:
                ans.append(temp)
            for i in range(index+1,n+1):
                permu(i,temp+[i])
        permu(0,[])
        return ans