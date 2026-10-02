class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        left = 0
        right = 1
        max_profit = 0
        while (left<right and right<size):
            profit = prices[right] - prices[left]
            if prices[right]<prices[left]:
                left = right
            elif profit > 0 and max_profit < profit:
                max_profit = profit
            right+=1

        return max_profit
        
        