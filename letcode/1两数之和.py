from typing import List, Set
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for index in range(len(nums)):
            item1 = nums[index]
            item2 = target - item1
            if item2 in nums[index + 1:len(nums)]:
                res.append(index)
                index += 1
                while index < len(nums):
                    if item2 == nums[index]:
                        res.append(index)
                        return res
                    index += 1
                    
                    

nums = [2,7,11,15]
target = 9
so = Solution()
print(so.twoSum(nums,target))