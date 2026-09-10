class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for fast in range(1,len(prices)):
            if prices[fast] < buy:
                buy = prices[fast]
            else:
                profit = max(profit,prices[fast] - buy)
        
        return profit