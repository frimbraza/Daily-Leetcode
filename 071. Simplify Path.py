# 71. Simplifiy Path
# Medium

# first case failed because I didn't know that ... was a valid name even though .. and . aren't
# otherwise. split works find and usual rules.
# overall solution is straightforward

class Solution:
    def simplifyPath(self, path: str) -> str:
        
        canon = []
        words = path.split('/')
        
        for word in words:
            if not word:
                pass
            elif word == '.':
                pass
            elif word == '..':
                if canon:
                    canon.pop()
            else:
                canon.append(word)
            
        answer = '/'
        for word in canon:
            answer += word + '/'
        if len(answer) > 1:
            return answer[:-1]
        else:
            return answer
        
        
        
        
                        
                    