from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        index = 0
        
        def selectedMaxIndex(list):
            max = 0
            maxIndex = 0
            index = 0 
            while index < len(list):
                if max < list[index]:
                    max = list[index]
                    maxIndex = index
                index += 1
            return maxIndex
        
        while index < len(stones):
            max1Index = selectedMaxIndex(stones)
            max1 = stones[max1Index]
            stones[max1Index] = 0
            max2Index = selectedMaxIndex(stones)
            max2 = stones[max2Index]
            stones[max2Index] = max1 - max2
            index += 1
            
            
        return stones[selectedMaxIndex(stones)]

so = Solution()
list = [2,7,4,1,8,1]
print(so.lastStoneWeight(list))