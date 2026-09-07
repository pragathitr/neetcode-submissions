class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = prices[0] #essentially the left pointer
        for day, price in enumerate(prices):
            if price < minPrice:
                minPrice = price #updating the left pointer
            tempP = price - minPrice #difference of the right pointer value and left pointer value
            if tempP > maxProfit:
                maxProfit = tempP
        return maxProfit
