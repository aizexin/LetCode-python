from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        leftIndex  = 0
        rightIndex = 0
        listSize   = len(strs)
        
        if len(strs) == 0:
            return ''
        elif len(strs) == 1:
            return strs[0]
        
        minStrLen = len(strs[0])
        index = 0
        while index < listSize:
            minStrLen = min(minStrLen,len(strs[index]))
            index += 1
        strIndex = 0
        
        firstStr = strs[0]

        while strIndex < minStrLen:
            chartSum = 0
            
            for i in range(len(strs)):
                if strs[i][strIndex] == firstStr[strIndex]:
                    chartSum += 1
            if chartSum == listSize:
                rightIndex = strIndex + 1
            else:
                break
            strIndex += 1
        if rightIndex == 0:
            return ''
        return firstStr[0:rightIndex]
        
strs = [""]
so = Solution()
print(so.longestCommonPrefix(strs))
        