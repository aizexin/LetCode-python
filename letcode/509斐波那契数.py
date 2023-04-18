class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        # 循环n -2次
        index = 2
        prefn = 1
        preprefn = 0
        fn = 0
        while index <= n:
            fn = preprefn + prefn
            preprefn = prefn
            prefn = fn
            index += 1
        return fn
            
            
        
    #     def fn(n) -> int:
    #         if n == 0:
    #             return 0
    #         if n == 1:
    #             return 1
    #         return fn(n-1) + fn(n-2)
    #     return fn(n)

so = Solution()
print(so.fib(4))