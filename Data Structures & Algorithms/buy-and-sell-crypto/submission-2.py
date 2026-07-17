class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = prices[0]
        maxMargin = 0
        for price in prices:
            buy = min(price, buy)
            sell = max(buy, price)
            maxMargin = max(maxMargin, sell - buy)
        return maxMargin