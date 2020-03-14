# https://leetcode.com/problems/unique-paths-ii/
# Medium
# Pretty optimal solution
# Redone in Python


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        height = len(obstacleGrid)
        width = len(obstacleGrid[0])
        
        new_grid = [[0]*width] * height
        
        for i in range(height):
            for j in range(width):
                if obstacleGrid[i][j] == 1:
                    new_grid[i][j] = 0
                elif i == 0 and j == 0:
                    new_grid[i][j] = 1
                elif j == 0:
                    new_grid[i][j] = new_grid[i - 1][j]
                elif i == 0:
                    new_grid[i][j] = new_grid[i][j - 1]
                else:
                    new_grid[i][j] = new_grid[i - 1][j] + new_grid[i][j - 1]
        
        return new_grid[height - 1][width - 1]                