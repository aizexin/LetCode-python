from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        index = 0
        maxProfit = 0
        minInProfit = prices[0]
        
        while index < len(prices):
            minInProfit  = min(minInProfit, prices[index])
            maxProfit    = max(maxProfit, prices[index] - minInProfit)
            index = index + 1
        return maxProfit
        # ---------超时-------------
        # inIndex = 0
        # outIndex = 0
        # maxProfit = 0
        # while inIndex < len(prices) - 1:
        #     inPrice = prices[inIndex]
        #     outIndex = inIndex + 1
        #     while outIndex < len(prices):
        #         profit = prices[outIndex]-inPrice
        #         if maxProfit < profit:
        #             maxProfit = profit
        #         outIndex = outIndex + 1
        #     inIndex = inIndex + 1
        # return maxProfit


            
    
list = [7,1,5,3,6,4]
so = Solution()
print(so.maxProfit(list))