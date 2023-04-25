from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        indexY = 0
        while indexY < m:

            if target <= matrix[indexY][n-1]:
                for x in matrix[indexY]:
                    if x == target:
                        return True
                return False
            else:
                indexY += 1
        return False
                
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]

target = 30
so = Solution()
print(so.searchMatrix(matrix, target))