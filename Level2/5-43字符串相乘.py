class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        # 单数乘法
        def unitMultiplication(strNum: str, n: int):
            indexNum1 = len(strNum)
            # 补偿位
            complement = 0
            res = ''
            while 0 < indexNum1:
                indexNum1 -= 1
                multiplicand = int(num1[indexNum1])
                temp = multiplicand * n + complement
                complement = temp // 10
                unit = temp % 10 
                res = str(unit) + res
            if complement != 0:
                res = str(complement) + res
            return res
        
        def addFunction(str1 ,str2) -> str:
            res = ''
            maxLen = max(len(str1),len(str2))
            index = 1
            complement = 0
            while index <= maxLen:
                index1 = len(str1) - index
                index2 = len(str2) - index
                num1 = 0
                if 0 <= index1:
                    num1 = int(str1[index1])
                if 0 <= index2:
                    num2 = int(str2[index2])
                temp = num1 + num2 + complement
                complement = temp // 10
                unit = temp % 10 
                res = str(unit) + res
                index += 1
            if complement != 0:
                res = str(complement) + res
            return res

        
        lenNum2 = len(num2)
        index = 1

        tempSum = '0'
        while index <= lenNum2:
            endIndex2 = lenNum2 - index
            temp = unitMultiplication(num1,int(num2[endIndex2]))
            if int(temp) != 0:
                for i in range(index-1):
                    temp = temp + '0'
            else:
                temp = '0'
            tempSum = addFunction(tempSum, temp)
            index += 1
        return tempSum

num1 = "123456789"
num2 = "987654321"
so = Solution()
print(so.multiply(num1,num2))
                
            