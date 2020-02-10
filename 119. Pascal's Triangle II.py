# https://leetcode.com/problems/pascals-triangle-ii/
# Easy

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        def buildNext(prev, rowSize):
            output = [1]
            for i in range(rowSize - 2):
                output.append(prev[i] + prev[i+1])
            output.append(1)
            return output
        
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        
        currentRow = 1
        output = [1,1]
        while(currentRow != rowIndex):
            output = buildNext(output, currentRow + 2)
            currentRow += 1
        
        return output
        
        