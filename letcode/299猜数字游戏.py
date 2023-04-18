class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # 记录每个数字出现的次数
        sMapArray = [0]*10
        gMapArray = [0]*10
        bullsNum = 0
        for i in range(len(guess)):
            if secret[i] == guess[i]:
                bullsNum += 1
            else:
                sMapArray[int(secret[i])] += 1
                gMapArray[int(guess[i])]  += 1
        cows = 0
        for i in range(10):
            if sMapArray[i] != 0 and gMapArray[i] != 0:
                cows += min(sMapArray[i],gMapArray[i])
        return  str(bullsNum) + 'A' + str(cows) +'B'
    
secret = "1122"
guess  = "0001"
so = Solution()
print(so.getHint(secret,guess))