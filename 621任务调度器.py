from typing import List
from collections import defaultdict
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n < 1:
            return len(tasks)
        arrayMap = [0] * 26
        for x in tasks:
            index = ord(x) - ord('A')
            arrayMap[index] += 1
        arrayMap.sort(reverse=True)
        
        index   = 0 
        sumTime = 0
        while index < len(tasks):

            indexN = 0
            # 一轮
            while indexN < n + 1:
                if index >= len(tasks):
                    break
                if indexN >= 26:
                    sumTime = sumTime + n + 1 - indexN 
                    break
                    
                if arrayMap[indexN] >= 1:
                    arrayMap[indexN] -= 1
                    index += 1
                    indexN += 1
                elif arrayMap[indexN] == 0:
                    sumTime = sumTime + n + 1 - indexN 
                    break
                 
                sumTime += 1
            # 重新排序
            arrayMap.sort(reverse=True)   
        return sumTime    

so = Solution()
tasks = ["A","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
n=29
print(so.leastInterval(tasks, n))            
        