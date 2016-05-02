class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        cnt = [0] * (amount + 1)
        for i in range(1, amount + 1):
            min_num = amount
            for co in coins:
                if i - co >= 0:
                    min_num = min(min_num, cnt[i-co])
            cnt[i] = min_num + 1
        return cnt[amount] == amount + 1 and -1 or cnt[amount]
