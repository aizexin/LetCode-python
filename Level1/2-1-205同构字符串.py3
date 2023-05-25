from typing import List
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        index = 0
        setA = {}
        setB = {}
        if len(s) != len(t):
            return False
        while index < len(s):
            key = s[index]
            if key in setA and setA[key] != t[index]:
                return False
            else:
                setA[key] = t[index]

            tkey = t[index]
            if tkey in setB and setB[tkey] != s[index]:
                return False
            else:
                setB[tkey] = s[index]
            index = index + 1
        return True

so = Solution()
s = "paper"
t = "title"
print(so.isIsomorphic(s, t))