class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0

        for p in prices[1:]:
            profit = p - minPrice
            if profit > maxProfit:
                maxProfit = profit
            if p < minPrice:
                minPrice = p
        return maxProfit