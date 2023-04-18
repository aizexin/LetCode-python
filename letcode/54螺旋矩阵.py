from typing import List, Set, Dict
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        res = []
        indexX = 0
        indexY = 0
        maxX = len(matrix[indexX])
        maxY = len(matrix)
        x = maxX
        y = maxY
        xyMap = set()
        while len(res) < (x * y):
            # 向右
            while True:
                key  = str(indexX) + '-' +str(indexY)
                if indexX >= maxX :
                    indexX -= 1
                    break
                if key not in xyMap:
                    res.append(matrix[indexY][indexX]) 
                    xyMap.add(key)
                    indexX += 1
                else:
                    indexX -= 1
                    break

            # 向下
            indexY += 1
            while True:
                key  = str(indexX) + '-' +str(indexY)
                if indexY >= maxY :
                    indexY -= 1
                    break
                if key not in xyMap:
                    res.append(matrix[indexY][indexX]) 
                    xyMap.add(key)
                    indexY += 1
                else:
                    indexY -= 1
                    break
            
            # 向左
            indexX -= 1
            while True:
                key  = str(indexX) + '-' +str(indexY)
                if 0 > indexX:
                    indexX += 1
                    break
                if key not in xyMap:
                    res.append(matrix[indexY][indexX]) 
                    xyMap.add(key)
                    indexX -= 1
                else:
                    indexX += 1
                    break
            
            # 向上
            indexY -= 1
            while True:
                key  = str(indexX) + '-' +str(indexY)
                if 0 > indexY:
                    indexY += 1
                    break
                if key not in xyMap:
                    res.append(matrix[indexY][indexX]) 
                    xyMap.add(key)
                    indexY -= 1
                else:
                    indexY += 1
                    break
            # 向右
            indexX += 1
        return res
            
so = Solution()
# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# matrix = [[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30]]#[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
matrix = [[1]]
print(so.spiralOrder(matrix))

            