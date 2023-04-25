from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def midSearch(array: List[int],leftIndex, rightIndex ,tag) -> int:
            if rightIndex - leftIndex <= 1:
                if array[rightIndex] == tag:
                    return rightIndex
                elif array[leftIndex] == tag:
                    return leftIndex
                else:
                    return -1
            midIndex = (rightIndex - leftIndex) // 2 + leftIndex
            mid = array[midIndex]
            if mid == tag:
                return midIndex
            elif mid < tag:
                return midSearch(array,midIndex + 1,rightIndex,tag)
            elif tag < mid:
                return midSearch(array,leftIndex,midIndex - 1, tag)
        # 搜索无序
        def searchNOorder(array: List[int],leftIndex, rightIndex, tag):
            if rightIndex - leftIndex <= 1:
                if array[rightIndex] == tag:
                    return rightIndex
                elif array[leftIndex] == tag:
                    return leftIndex
                else:
                    return -1
            midIndex = (rightIndex - leftIndex)// 2 + leftIndex
            mid = array[midIndex]
            right = array[rightIndex]
            left = array[leftIndex]
            if mid == tag:
                return midIndex
            if midIndex == 0:
                return -1
            if left <= mid:
                #左边有序
                if left <= target and target < mid:
                    resOrder = midSearch(array, leftIndex, midIndex - 1,target)
                    return resOrder
                else: 
                    #搜索右边的无序
                    return searchNOorder(array,midIndex + 1,rightIndex, tag)
            if mid < right:
                #右边有序
                if mid < target and target <= right:
                    resOrder = midSearch(array, midIndex + 1, rightIndex, tag)
                    return resOrder
                else:
                    return searchNOorder(array, leftIndex, midIndex - 1, tag )
        return searchNOorder(nums, 0, len(nums) -1,target)
        
nums = [266,267,268,269,271,278,282,292,293,298,6,9,15,19,21,26,33,35,37,38,39,46,49,54,65,71,74,77,79,82,83,88,92,93,94,97,104,108,114,115,117,122,123,127,128,129,134,137,141,142,144,147,150,154,160,163,166,169,172,173,177,180,183,184,188,198,203,208,210,214,218,220,223,224,233,236,241,243,253,256,257,262,263]

target = 208
so=Solution()
print(so.search(nums,target))