# https://leetcode.com/problems/gray-code/
# Medium

# complete but slow
# Note: to do faster, probably remove all checking and figure a way to do only by rules
class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        
        base = '0' * n
        answer = [0]
        
        current = base
        
        while len(answer) < pow(2,n):
            for i in range(n):
                if current[i] == '0':
                    new_current = current[:i] + '1' + current[i+1:]
                else:
                    new_current = current[:i] + '0' + current[i+1:]
                
                if int(new_current,2) not in answer:
                    answer.append(int(new_current,2))
                    current = new_current
                    break
        
        return answer