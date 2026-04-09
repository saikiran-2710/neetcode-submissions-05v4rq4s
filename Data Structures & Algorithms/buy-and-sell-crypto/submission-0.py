class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxb=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                maxb=max(maxb,prices[j]-prices[i])
        return maxb




        