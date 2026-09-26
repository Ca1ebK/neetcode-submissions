class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Dynamic Programming Solution
        # Keep track of the lowest price,
        # calculate the max profit at each iteration,
        # and update the lowest price at each iteration
        # Runtime: O(n)
        # Memory: O(1)
        
        lowestPrice = prices[0]
        maxP = 0

        for i in range(1, len(prices)):
            maxP = max(maxP, prices[i] - lowestPrice)
            if prices[i] < lowestPrice:
                lowestPrice = prices[i]
        
        return maxP