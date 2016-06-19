class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = sum(nums)
        b = sum(list(set(nums))) * 3
        return (b - a) / 2
