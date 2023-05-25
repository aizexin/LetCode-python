from typing import List
# 快速排序
def quickSort(array :List, leftIndex, rightIndex):
    
    def quickSingle( tempLeftIndex, tempRightIndex):

        if tempLeftIndex == tempRightIndex:
            # print(array)
            return tempLeftIndex
       
        pIndex = tempLeftIndex ;
        # 取出矛点
        mid = array[pIndex]
        
        while 1 < tempRightIndex - tempLeftIndex :
            while tempLeftIndex < tempRightIndex and mid < array[tempRightIndex]:
                tempRightIndex -= 1
            array[pIndex] = array[tempRightIndex]
            pIndex = tempRightIndex
            while tempLeftIndex < tempRightIndex and array[tempLeftIndex] < mid:
                tempLeftIndex += 1
            array[pIndex] = array[tempLeftIndex]
            pIndex = tempLeftIndex

        array[pIndex] = mid
        return pIndex
    
    
    if rightIndex - leftIndex < 2:
        if array[rightIndex] < array[leftIndex]:
                temp = array[rightIndex]
                array[rightIndex] = array[leftIndex]
                array[leftIndex] = temp
        return array
    midIndex = quickSingle( leftIndex, rightIndex)
    if midIndex:
        quickSort(array, leftIndex,midIndex)
        quickSort(array, midIndex+1,rightIndex)
    return array
            
array = [10,1,13,3,2,63,43]
print(quickSort(array,0,len(array)-1))
            
            
    
    