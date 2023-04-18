from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        def isInArea(x, y) -> bool:
            maxX = len(grid)
            maxY = len(grid[0])
            if 0 <= x and x < maxX and 0 <= y and y < maxY:
                return True
            else:
                return False
        # 深度便利
        def dfs(x, y):
            if isInArea(x,y) == False:
                return
            # 标记
            if grid[x][y] == '1':
                grid[x][y] = '2'
            elif grid[x][y] == '0':
                return
            elif grid[x][y] == '2':
                return

            # 上
            if isInArea(x, y+1):
                dfs(x, y+1)
            # 下
            if isInArea(x, y-1):
                dfs(x, y-1) 
            # 左
            if isInArea(x-1, y):
                dfs(x-1, y) 
            # 右
            if isInArea(x+1, y):
                dfs(x+1, y)  
        indexX = 0
        while indexX < len(grid):
            indexY = 0
            while indexY < len(grid[indexX]):
                if grid[indexX][indexY] == '1':
                    island += 1
                    # 染色
                    dfs(indexX, indexY)
                indexY += 1
            indexX += 1
        return island
    
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

so = Solution()
print(so.numIslands(grid))
                