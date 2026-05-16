class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = prices[0]
        
        for i in prices:
            max_profit = max(max_profit, i-min_buy)
            #calcs the smaller price to buy of the two
            min_buy = min(min_buy, i)
        
        return max_profit


