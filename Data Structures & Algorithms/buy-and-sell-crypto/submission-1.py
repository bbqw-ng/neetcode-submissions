class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for l in range(len(prices)):
            r = l+1
            while r <= len(prices)-1:
                print()
                print(prices[l])
                print(prices[r])
                if prices[r] < prices[l]:
                    r += 1
                    continue
                print("calcing profit)")
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
                r += 1
        return max_profit