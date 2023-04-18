from typing import List
import math
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        minIndex = 0
        maxIndex = length - 1
        halfIndex = length // 2
        while minIndex <= maxIndex:
            if nums[halfIndex] == target:
                return halfIndex
            elif nums[halfIndex] < target:
                minIndex = halfIndex
                minIndex += 1
            elif target < nums[maxIndex]:
                maxIndex = halfIndex
                maxIndex -= 1
            halfIndex = (maxIndex - minIndex) // 2 + minIndex
        return -1
                
nums = [5]
target = 5
so = Solution()
print(so.search(nums,target))
            
            