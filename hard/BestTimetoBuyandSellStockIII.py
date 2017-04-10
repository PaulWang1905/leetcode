class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        
        dp = [0]
        low, ans_left = prices[0], 0
        for i in xrange(1, len(prices)):
            if prices[i] < low:
                low = prices[i]
            else:
                ans_left = max(ans_left, prices[i]-low)
            dp.append(ans_left)
        
        profit, ans_right = 0, 0
        cur_max = prices[-1]
        for j in range(len(prices)-1)[::-1]:
            if prices[j] > cur_max:
                cur_max = prices[j]
            else:
                ans_right = max(ans_right, cur_max-prices[j])
            profit = max(profit, ans_right+dp[j])
        
        return profit
