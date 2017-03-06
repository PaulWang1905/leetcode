class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total_sum = sum(nums)
        
        if total_sum & 1:
            return False
        
        target = total_sum / 2
        dp = [True] + [False for i in range(target)]
        
        for num in nums:
            for j in reversed(range(1, target + 1)):
                if j-num >= 0:
                    dp[j] = dp[j] or dp[j-num]

        return dp[target]
