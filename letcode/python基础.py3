
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            sum = sum + num
            res.append(sum)
        return res 
        # return [sum(nums[:a+1]) for a in range(len(nums))]
        # newList = []
        # count = 0
        # while count < len(nums):
        #     index = 0
        #     while index < count:
        #         sum = nums[index] + sum
        #         index = index + 1
        #     newList.append(sum)
        #     count = count + 1
        # return newList
so = Solution()
nums = [1,2,3,4]

print(so.runningSum(nums))