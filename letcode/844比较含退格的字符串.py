class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def backstr(string) -> str:
            res = ''
            for index in range(len(string)):
                if string[index] == '#' and 1 < len(res):
                    res = res[0:len(res) - 1]
                elif string[index] == '#' and len(res) <= 1:
                    res = ''
                else:
                    res = res + string[index]
            return res
        s = backstr(s)
        t = backstr(t)
        return s == t
    
s = "a#c"
t = "d"
so = Solution()
print(so.backspaceCompare(s,t))
