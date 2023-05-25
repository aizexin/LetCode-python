from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
       
        size = len(cost)
        if size == 1:
            return 0
        elif size == 2:
            return min(cost[0],cost[1])
        index = 2
        minCosLsit  = [0] * size
        minCosLsit[1] = min(cost[0],cost[1])
        while index < size:
            temp1 = minCosLsit[index-1] + cost[index]
            temp2 = minCosLsit[index-2] + cost[index -1]
            minCosLsit[index] = min(temp1,temp2)
            index += 1

        
        return minCosLsit[size-1]
    
cost = [0,1,2,2]
so = Solution()
print(so.minCostClimbingStairs(cost))

# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:

#         # 动态规划
#         # 1. 确定dp数组 dp = []
#         # 2. 递推公式 dp[n] = min(dp[n - 1], dp[n - 2]) + cost[n]
#         # 3. 初始化,初始化两项，分别对应于cost[0]、cost[1]
#         # 4. 顺序，从左到右
#         # 5. 举例推导

#         size = len(cost)
#         dp = [0] * size
#         dp[0] = cost[0]
#         dp[1] = cost[1]

#         # 循环
#         for i in range(2,size):
#             dp[i] = min(dp[i - 1], dp[ i - 2]) + cost[i]
        
#         # 返回的时候，不是返回最后一项，而是最后两项的最小值
#         return min(dp[size - 1], dp[size - 2])

        