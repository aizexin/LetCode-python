from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        midIndex   = 0
        endIndex   = len(nums)
        totalSum   = self.sumRange(nums, 0, endIndex)
        preSum     = 0
        while midIndex < endIndex:
            tempSum = preSum * 2 + nums[midIndex]
            if tempSum == totalSum:
                return midIndex
            else:
                preSum   = preSum + nums[midIndex]
                midIndex = midIndex + 1
        return -1
    
    def sumRange(self, nums: List[int], startIndex, endIndex) -> int:
        sum = 0
        while startIndex < endIndex:
            sum = nums[startIndex] + sum
            startIndex = startIndex + 1
        return sum
    
so = Solution()
nums = [2,1,-1]
print(so.pivotIndex(nums))