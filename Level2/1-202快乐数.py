from typing import Set
class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sumPinfang(number) -> int:
            sum = 0
            for x in number:
                sum = sum + int(x) * int(x)
            return sum
        
        sumSet = set()
        temp = n
        while True:
            temp = sumPinfang(str(temp))
            if temp == 1:
                return True
            elif temp in sumSet:
                return False
            else:
                sumSet.add(temp)

so = Solution()
print(so.isHappy(2))