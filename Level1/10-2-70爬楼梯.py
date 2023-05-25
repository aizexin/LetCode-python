class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        index = 3
        # 2个台阶的时候
        preN = 2
        prepreN = 1
        stepN = 0
        while index <= n:
            stepN = preN + prepreN
            prepreN = preN
            preN = stepN
            index += 1
        return stepN
    
so = Solution()
print(so.climbStairs(3))
            