class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        indexS = 0
        indexT = 0
        comonStr = ''
        while indexT < len(t) and indexS < len(s):
            if s[indexS] == t[indexT]:
                comonStr = comonStr + s[indexS]
                indexS = indexS + 1
            indexT = indexT + 1
        
        return comonStr == s
so = Solution()
s = "ahbgdc"; t = "ahbgdc"
print(so.isSubsequence(s, t))