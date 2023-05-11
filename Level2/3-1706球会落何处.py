from typing import List
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        maxXLen = len(grid)
        

        index = 0
        res = []
        while index < len(grid[0]):
            indexX = 0
            indexY = 0
            indexY = index
            while True:
                # 通过
                if maxXLen <= indexX:
                    res.append(indexY)
                    break
                
                maxYLen = len(grid[indexX])
                
                oprate =grid[indexX][indexY]
                if oprate == 1:
                    tempY = indexY + 1
                    tempX = indexX + 1
                elif oprate == -1:
                    tempY = indexY - 1
                    tempX = indexX + 1
                    
                if tempY < 0 or maxYLen <= tempY:
                    res.append(-1)
                    break
                    
                if grid[indexX][tempY] != (0 - oprate) :
                    indexX = tempX
                    indexY = tempY
                else:
                    res.append(-1)
                    break                
            index += 1
        return res
            
so = Solution()
grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
print(so.findBall(grid))
            