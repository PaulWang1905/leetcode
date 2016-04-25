class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MAX = MIN = res = nums[0]
        for i in range (1, len(nums)):
            MAX, MIN = max(MAX*nums[i], MIN*nums[i], nums[i]), min(MAX*nums[i], MIN*nums[i], nums[i])
            res = max(MAX, res)
        return res
