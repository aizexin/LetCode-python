class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[1] * m] + [[1] + [0] * (m - 1) for _ in range(n - 1)]

        
        paths[0][0] = 1
        y = 0
        while y < m:
            x = 0
            while x < n:
                if x == 0 and y == 0:
                    x += 1
                    continue
                path1 = 0
                path2 = 0
                if 0 <= x-1:
                    path1 = paths[x-1][y]
                if 0 <= y-1:
                    path2 = paths[x][y-1]
                paths[x][y] = path1 + path2
                x += 1
            y += 1
        return paths[n-1][m-1]
    
so = Solution()
print(so.uniquePaths(3,2))