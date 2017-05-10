class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = nums[:1] + [0] * (len(nums)-1)
        
        for i in xrange(1, len(nums)):
            if dp[i-1] <= 0:
                dp[i] = nums[i]
            else:
                dp[i] = nums[i] + dp[i-1]
        return max(dp)
