from typing import Set
class Solution:
    def longestPalindrome(self, s: str) -> int:
        setPool = set()
        count = 0
        for item in s:
            if item in setPool:
                setPool.remove(item)
                count = count + 2
            else:
                setPool.add(item)
        if len(setPool) > 0:
            count = count + 1
        return count       
        

so = Solution()
s = "abccccdd"

print(so.longestPalindrome(s))