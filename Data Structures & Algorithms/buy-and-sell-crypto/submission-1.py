class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        profit=0
        for price in prices:
            if price<buy:
                buy=price

            current_profit=price-buy

            if current_profit>profit:
                profit=current_profit
        return profit
        






        