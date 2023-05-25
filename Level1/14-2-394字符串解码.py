from typing import List,Deque
class Solution:
    def decodeString(self, s: str) -> str:
        strDeque = list()
        numDeque = list()
        num = 0
        res = ''
        index = 0
        while index < len(s):
            x = s[index]
            if x.isdecimal():
                tempDeque = Deque()
                tempIndex = index
                while tempIndex < len(s):
                    if s[tempIndex].isdecimal():
                        tempDeque.append(s[tempIndex])
                        tempIndex += 1
                    else:
                        # 取出数字
                        if tempDeque:
                            tempNum = int(''.join(tempDeque))
                            numDeque.append(tempNum)
                        else:
                            numDeque.append(1)
                        index = tempIndex
                        break
            elif x == '[':
                index += 1
                tempStr = ''
                tempIndex = index
                while tempIndex < len(s) and s[tempIndex].isalpha():
                    tempStr = tempStr + s[tempIndex]
                    tempIndex += 1
                index = tempIndex
                strDeque.append(tempStr)
            elif x == ']':
                # 取出数字
                if numDeque:
                    num = numDeque.pop()
                itemStr = ''
                if strDeque:
                    itemStr = strDeque.pop()
                subStr = ''
                for i in range(num):
                    subStr += itemStr
                topStr = ''
                if strDeque:
                    topStr = strDeque.pop() + subStr
                else:
                    topStr = subStr
                strDeque.append(topStr)
                index += 1
            else: 
                #直接是字母
                tempIndex = index
                tempStr = ''
                while tempIndex < len(s) and s[tempIndex].isalpha():
                    tempStr = tempStr + s[tempIndex]
                    tempIndex += 1
                # strDeque.append(tempStr)
                # numDeque.append(1)
                topStr = ''
                if strDeque:
                    topStr = strDeque.pop() + tempStr
                else:
                    topStr = tempStr
                strDeque.append(topStr)
                index = tempIndex
        
        while strDeque:
            if numDeque:
                num = numDeque.pop()
            else:
                num = 1
            itemStr = strDeque.pop()
            subStr = ''
            for i in range(num):
                subStr += itemStr
            if strDeque:
                topStr = strDeque.pop() + subStr
                strDeque.append(topStr)
            else:
                res = res + subStr
            
        return res
s = "2[4[2[jk]e1[f]]]ef"
so = Solution()
print(so.decodeString(s))

                        
                