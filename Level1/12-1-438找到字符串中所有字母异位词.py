from filecmp import cmp
from typing import List,Dict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)
        if s_len < p_len:
            return []
        res = []
        s_count = [0] * 26
        p_count = [0] * 26
        for i in range(p_len):
            s_count[ord(s[i])-97] += 1
            p_count[ord(p[i])-97] += 1
        if s_count == p_count:
            res.append(0)
        
        for i in range(s_len - p_len):
            s_count[ord(s[i])-97] -= 1
            s_count[ord(s[i + p_len]) - 97] += 1
            if s_count == p_count:
                res.append(i+1)
        
        return res
                    
s = "cbaebabacd"
p = "abc"
so = Solution()
print(so.findAnagrams(s, p))