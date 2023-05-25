# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:

    def firstBadVersion(self, n: int) -> int:
        
        def isBadVersion(n):
            return n >= 4
        
        maxGoodV = 0
        minBadV = n
        while minBadV - maxGoodV != 1:
            mid = maxGoodV + (minBadV - maxGoodV) // 2
            if isBadVersion(mid):
                minBadV = mid 
            else:
                maxGoodV = mid
        return minBadV
    
so = Solution()

print(so.firstBadVersion(5))