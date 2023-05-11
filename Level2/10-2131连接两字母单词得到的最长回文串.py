from typing import List
from collections import defaultdict
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        dict = defaultdict(int)
        for string in words:
            dict[string] += 1
        maxLen = 0
        hasMid = False
        for string in words:
            if dict[string] <= 0:
                continue
            if string[0] != string[1]:
                key = string[1] + string[0]
                if dict[key] > 0:
                    dict[key] -= 1
                    dict[string] -= 1
                    maxLen += 4
            elif string[0] == string[1]:
                if dict[string] >= 2:
                    dict[string] -= 2
                    maxLen += 4
                elif hasMid == False:
                    dict[string] -= 1
                    maxLen += 2
                    hasMid = True
                    
        return maxLen
                    
so = Solution()
words =  ["cc","ll","xx"]
print(so.longestPalindrome(words))
