class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = maxP = 0
        for i in range(1, len(prices)):
            if prices[i] >= prices[buy]:
                curP = prices[i] - prices[buy]
                maxP = max(maxP, curP)
            else:
                buy = i
        return maxP
