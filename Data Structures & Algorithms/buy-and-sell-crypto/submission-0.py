class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxProfit = 0

        n = len(prices)
        while r < n:
            if prices[l] <= prices[r]:
                maxProfit = max(maxProfit, prices[r] - prices[l])
                r += 1
            else:
                l += 1
        
        return maxProfit