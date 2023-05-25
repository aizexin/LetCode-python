class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        rigth = 0
        # 单个相同最长的
        maxLen = 0
        arrayMap = [0] * 26
        while rigth < len(s):
            arrayMap[ord(s[rigth]) - ord('A')] += 1
            
            maxLen = max(maxLen, arrayMap[ord(s[rigth]) - ord('A')])
            if rigth - left + 1 - maxLen > k:
                arrayMap[ord(s[left]) - ord('A')] -= 1
                left += 1
            rigth += 1
        return rigth - left
                
s = "ABBB"
k = 2
so = Solution()
print(so.characterReplacement(s, k))         