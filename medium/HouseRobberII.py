class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
    
    def helper(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        a = nums[0]
        profit = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            a, profit = profit, max(a + nums[i], profit)
        return profit
