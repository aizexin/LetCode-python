from typing import List,Deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        class Postion:
            x: int
            y: int
            def __init__(self, x, y):
                self.x = x
                self.y = y
        
        poolDeque = Deque()
        p = Postion(sr,sc)
        poolDeque.append(p)
        
        maxX = len(image)
        maxY = len(image[0])
        orgColor = image[sr][sc]
        while poolDeque:
            item :Postion = poolDeque.popleft()
            if image[item.x][item.y] == color:
                continue
            image[item.x][item.y] = color
            
            # 上
            x = item.x
            y = item.y - 1
            if y >= 0 and (image[x][y] == orgColor or image[x][y] == color):
                poolDeque.append(Postion(x, y))
            # 下
            x = item.x
            y = item.y + 1
            if y < maxY and (image[x][y] == orgColor or image[x][y] == color):
                poolDeque.append(Postion(x, y))
            # 左
            x = item.x - 1
            y = item.y
            if x >=0 and (image[x][y] == orgColor or image[x][y] == color):
                poolDeque.append(Postion(x, y))
            
            # 右
            x = item.x + 1
            y = item.y
            if x < maxX and (image[x][y] == orgColor or image[x][y] == color):
                poolDeque.append(Postion(x, y))
        return image
    
image = [[1,1,1],[1,1,0],[1,0,1]]
so = Solution()
so.floodFill(image, 1, 1, 2)